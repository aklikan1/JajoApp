# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django.urls import path
from .views import login_view, register_user, logout_user
from django.contrib.auth.views import LogoutView

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('login/', login_view, name="login"),
    path('register/', register_user, name="register"),
    path('logout/', logout_user, name="logout")
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
