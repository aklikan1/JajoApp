# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django.contrib import admin
from . import models

# Register your models here.
admin.site.register(models.User)
admin.site.register(models.Status)
admin.site.register(models.Products)
admin.site.register(models.Orders)
admin.site.register(models.HoneySize)
admin.site.register(models.Quantity)
