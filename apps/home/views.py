# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django import template
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.urls import reverse, reverse_lazy
from django.shortcuts import render, redirect

from .forms import UpdateUserImages, UpdateUserProfile, CreateOrder
from .models import Products, Orders, ArrivalDate, Status

from bootstrap_modal_forms.generic import BSModalCreateView

import logging


@login_required(login_url="/login/")
def dashboard_page(request):
    context = {'segment': 'dashboard'}

    return render(request, 'home/dashboard.html', context)


@login_required(login_url="/login/")
def pages(request):
    context = {}
    # All resource paths end in .html.
    # Pick out the html file name from the url. And load that template.
    try:

        load_template = request.path.split('/')[-1]

        if load_template == 'admin':
            return HttpResponseRedirect(reverse('admin:index'))
        context['segment'] = load_template

        html_template = loader.get_template('home/' + load_template)
        return HttpResponse(html_template.render(context, request))

    except template.TemplateDoesNotExist:

        html_template = loader.get_template('home/page-404.html')
        return HttpResponse(html_template.render(context, request))

    except:
        html_template = loader.get_template('home/page-500.html')
        return HttpResponse(html_template.render(context, request))


@login_required(login_url='/login/')
def user_profile(request):
    user = request.user
    images_form = UpdateUserImages(instance=user)
    user_form = UpdateUserProfile(instance=user)

    page_part = 'user_information'

    context = {'segment': 'user_profile', 'images_form': images_form, 'user_form': user_form, 'page_part': page_part}

    if request.method == 'POST':
        form = UpdateUserProfile(request.POST, instance=user)
        if form.is_valid():
            form.save()
            return redirect('user-profile')

    return render(request, 'home/user/user_profile.html', context)


@login_required(login_url='/login/')
def update_user_avatar(request):
    user = request.user

    if request.method == "POST":
        form = UpdateUserImages(request.POST, request.FILES, instance=user)
        if form.is_valid():
            form.save()
            return redirect('user-profile')

    return render(request, 'home/user/user_profile.html', {})


@login_required(login_url='/login/')
def update_user_background(request):
    user = request.user

    if request.method == "POST":
        form = UpdateUserImages(request.POST, request.FILES, instance=user)
        if form.is_valid():
            form.save()
            return redirect('user-profile')

    return render(request, 'home/user/user_profile.html', {})


@login_required(login_url='/login/')
def products_page(request, pk):
    pk = int(pk)
    products = Products.objects.all()
    products_parts = [products[i:i+10] for i in range(0, len(products), 10)]

    product_range_last = 10 * pk
    product_range_first = product_range_last - 9

    counts_products = len(products)
    count_products_part = len(products_parts)

    pk = int(pk)

    context = {'products': products_parts[pk-1], 'counts_parts': range(1, count_products_part+1),
               'counts_products': counts_products, 'pk': pk, 'product_range_first': product_range_first,
               'product_range_last': product_range_last, 'segment': 'products'}
    return render(request, 'home/product_list.html', context)


@login_required(login_url='/login/')
def product_post(request, pk, parameter):

    if parameter == 'next':
        pk = int(pk)+1
    elif parameter == 'previous':
        pk = int(pk)-1

    return redirect('products', pk)


@login_required(login_url='/login/')
def orders_page(request):
    orders = Orders.objects.filter(user=request.user).all().order_by('-id')
    for order in orders:
        pass

    context = {'segment': 'orders', 'orders': orders}
    return render(request, 'home/order/orders.html', context)


class OrderCreateView(BSModalCreateView):
    login_url = '/login/'
    redirect_field_name = 'redirect_to'

    template_name = 'home/order/create-order.html'
    form_class = CreateOrder
    success_message = 'Success: Quantity was created.'
    success_url = reverse_lazy('orders')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        arrival_date = ArrivalDate.objects.all().last()
        context['arrival_date'] = arrival_date
        return context

    def form_valid(self, form):
        if not self.request.is_ajax():
            due = Status.objects.filter(status="Due").last()
            get_form = form.save(commit=False)
            arrival = ArrivalDate.objects.all().last()
            order, created = Orders.objects.get_or_create(status=due,
                                                          defaults={'user': self.request.user, 'status': due,
                                                                    'arrival_date': arrival})
            get_form.order = order
            get_form.save()
        return HttpResponseRedirect(self.success_url)
