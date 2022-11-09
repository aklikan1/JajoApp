from django.forms import ModelForm
from .models import User, Quantity, ArrivalDate
from django import forms
from bootstrap_modal_forms.forms import BSModalModelForm


class UpdateUserImages(ModelForm, forms.Form):
    avatar = forms.ImageField(label='', widget=forms.FileInput(attrs={'onchange': 'submit();'}))
    background_photo = forms.ImageField(label='', widget=forms.FileInput(attrs={'onchange': 'submit();'}))

    class Meta:
        model = User
        fields = ['avatar', 'background_photo']


class UpdateUserProfile(ModelForm, forms.Form):
    class Meta:
        model = User
        fields = ['name', 'email', 'phone', 'address', 'address_number', 'address_city', 'address_zip']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'id': 'name', 'placeholder': 'Enter your name'}),
            'email': forms.TextInput(attrs={'class': 'form-control', 'id': 'email', 'readonly': 'on'}),
            'phone': forms.NumberInput(attrs={'class': 'form-control', 'id': 'phone',
                                              'placeholder': 'Phone nr...'}),
            'address': forms.TextInput(attrs={'class': 'form-control', 'id': 'address',
                                              'placeholder': 'Home address...'}),
            'address_number': forms.TextInput(attrs={'class': 'form-control', 'id': 'number', 'placeholder': 'No...'}),
            'address_city': forms.TextInput(attrs={'class': 'form-control', 'id': 'city', 'placeholder': 'City...'}),
            'address_zip': forms.TextInput(attrs={'class': 'form-control', 'id': 'zip', 'placeholder': 'Zip code...'}),

        }


class CreateOrder(BSModalModelForm, forms.Form):
    class Meta:
        model = Quantity
        fields = ['product', 'quantity']
        widgets = {
            'product': forms.Select(attrs={'class': 'form-control', 'id': 'product', 'label': 'Product'}),
            'quantity': forms.NumberInput(attrs={'class': 'form-control', 'id': 'quantity', 'label': 'Quantity'}),
        }
