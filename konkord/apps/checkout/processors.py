# -*- coding: utf-8 -*-
from .models import Order
from django.db import transaction
from django.conf import settings
from users.models import User
from mail.utils import send_email, render
from django.shortcuts import redirect, reverse
from django.contrib.sites.shortcuts import get_current_site
from .utils import get_voucher_data_for_user
from .signals import order_created


class BasePaymentProcessor(object):

    user_password_length = 6
    
    password_mail_template =\
        'checkout/background_registration/background_registration_mail.html'
    password_mail_subject =\
        'checkout/background_registration/background_registration_mail_subject.html'
    order_mail_template = 'checkout/order/new_order_mail.html'
    order_mail_subject = 'checkout/order/new_order_mail_subject.html'
    
    def __init__(self, request, cart, checkout_form):
        self.request = request
        self.form = checkout_form
        self.cart = cart
    
    def send_order_created_mail(self, order):
        to_email = self.form.cleaned_data.get('email')
        site = get_current_site(self.request)
        subject = render(
            self.order_mail_subject,
            **{
                'order': order,
                'site': site
            }
        )
        html = render(
            self.order_mail_template,
            **{
                'order': order,
                'site': site
            }
        )
        if to_email:
            send_email(subject=subject, text=html, html=html, to=[to_email])
        if getattr(settings, 'SITE_EMAIL', ''):
            send_email(
                subject=subject, text=html, html=html, to=[settings.SITE_EMAIL])

    def send_password_mail(self, user, password):
        html = render(
            self.password_mail_template,
            **{
                'user': user,
                'password': password
            }
        )
        to_email = self.form.cleaned_data.get('email')
        subject = render(
            self.password_mail_subject,
        )
        if to_email:
            send_email(subject=subject, text=html, html=html, to=[to_email])

    def background_registration(self):
        username = self.form.cleaned_data.get(
            getattr(settings, 'AUTHENTICATE_BY', 'email'))
        password = User.objects.make_random_password(self.user_password_length)
        user = User.objects.register_user(
            username, password,
            self.request,
            self.form.cleaned_data, settings.CHECKOUT_USER_FIELDS)
        self.send_password_mail(user, password)
        return user

    @transaction.atomic
    def process(self):
        user = User.objects.get_user(self.request, self.form.cleaned_data)
        if not user:
            user = self.background_registration()
        shipping_data = {}
        voucher_number = self.request.POST.get('voucher')
        if self.form.cleaned_data.get('city'):
            shipping_data['city'] = self.form.cleaned_data['city'].name
            shipping_data['office'] = self.form.cleaned_data['office'].address
        user_data = {}
        for field_data in settings.CHECKOUT_USER_FIELDS:
            data = self.form.cleaned_data.get(field_data['name'])
            if data:
                user_data[field_data['name']] = data

        order = Order.objects.create(
            user=user,
            status=Order.get_default_status(),
            payment_method=self.form.cleaned_data.get('payment_method'),
            shipping_method=self.form.cleaned_data.get('shipping_method'),
            shipping_data=shipping_data,
            user_data=user_data,
            user_message=self.form.cleaned_data.get('user_message')
        )
        if order.payment_method:
            payment_price = order.payment_method.get_price()
            order.payment_data['price'] = float(payment_price)
            order.price += payment_price
            user.default_payment_method = order.payment_method.id
        if order.shipping_method:
            shipping_price = order.shipping_method.get_price()
            order.shipping_data['price'] = float(shipping_price)
            order.price += shipping_price
            user.default_shipping_method = order.shipping_method.id
        for cart_item in self.cart.items.all():
            order.items.create(
                product=cart_item.product,
                product_amount=cart_item.amount,
                product_name=cart_item.product.name,
                product_price=cart_item.product.get_price()
            )
            order.price += cart_item.get_price()

        if voucher_number:
            voucher_data = get_voucher_data_for_user(
                self.request, voucher_number)
            if voucher_data['voucher_effective']:
                order.voucher = voucher_data['voucher']
                order.voucher_discount = voucher_data['discount']
                order.price -= voucher_data['discount']
        user.save()
        order.save()
        self.cart.delete()
        self.request.session['order_id'] = order.id
        self.send_order_created_mail(order)
        order_created.send(order_id=order.id, sender=None)
        return redirect(reverse('thank_you_page'))
