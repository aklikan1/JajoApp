# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django.db import models
# from django.contrib.auth.models import User
from django_resized import ResizedImageField


from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    name = models.CharField(max_length=255, null=True, blank=False)
    email = models.EmailField(null=True, unique=True, blank=False)
    phone = models.IntegerField(null=True, blank=False)
    address = models.CharField(max_length=200, null=True, blank=False)
    address_number = models.CharField(max_length=50, null=True, blank=False)
    address_city = models.CharField(max_length=50, null=True, blank=False)
    address_zip = models.CharField(max_length=6, null=True, blank=False)
    username = None

    avatar = ResizedImageField(size=[400, 200], null=True, blank=True, default='avatars/avatar.svg', upload_to='avatars')
    background_photo = ResizedImageField(size=[500, 600], null=True, blank=True, default='backgrounds/background.jpg',
                                         upload_to='backgrounds')
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    class Meta:
        ordering = ['id']


class Status(models.Model):
    status = models.CharField(max_length=100, null=True, blank=True)

    class Meta:
        verbose_name_plural = "Status"

    def __str__(self):
        return self.status


class HoneySize(models.Model):
    honey_size = models.CharField(max_length=20, null=True, blank=False)

    class Meta:
        verbose_name_plural = 'Size'

    def __str__(self):
        return self.honey_size


class Products(models.Model):
    name = models.CharField(max_length=200, null=True, blank=False)
    price = models.IntegerField(null=True, blank=False)
    available = models.BooleanField(null=True, blank=False)
    size = models.ForeignKey(HoneySize, on_delete=models.CASCADE, null=True, blank=True)

    class Meta:
        verbose_name_plural = 'Products'
        ordering = ['id']

    def __str__(self):
        if self.size is not None:
            return self.name + ' - ' + str(self.size)
        else:
            return self.name


class Quantity(models.Model):
    product = models.ForeignKey(Products, on_delete=models.CASCADE, null=True, blank=False)
    quantity = models.IntegerField(null=True, blank=False)
    order = models.ForeignKey('Orders', on_delete=models.CASCADE, null=True, blank=False)

    class Meta:
        verbose_name_plural = 'Quantity'

    def __str__(self):
        return str(self.order.created.date()) + ' : ' + str(self.product)


class Orders(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=False)
    status = models.ForeignKey(Status, on_delete=models.SET_NULL, null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)
    arrival_date = models.ForeignKey('ArrivalDate', on_delete=models.SET_NULL, null=True, blank=False)

    class Meta:
        verbose_name_plural = 'Orders'

    def __str__(self):
        return str(self.arrival_date)+" - order"


class ArrivalDate(models.Model):
    date = models.DateField(null=True, blank=False)

    def __str__(self):
        return str(self.date.day)+"."+str(self.date.month)
