

from django.urls import path, re_path
from apps.home import views

urlpatterns = [

    # The home page
    path('', views.dashboard_page, name='dashboard'),
    path('home/', views.dashboard_page, name='home'),

    path('user-profile/', views.user_profile, name='user-profile'),
    path('update-user-avatar/', views.update_user_avatar, name='update-user-avatar'),
    path('update-user-background/', views.update_user_background, name='update-user-background'),

    path('products/<str:pk>/<str:parameter>/', views.product_post, name='product_post'),
    path('products/<str:pk>/', views.products_page, name='products'),
    path('orders/', views.orders_page, name='orders'),

    # Matches any html file
    re_path(r'^.*\.*', views.pages, name='pages'),

]