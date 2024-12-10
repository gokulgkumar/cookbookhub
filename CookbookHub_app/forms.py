# forms.py
from django import forms  # type: ignore
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm # type: ignore
from .models import *


class Userform(UserCreationForm):
    first_name = forms.CharField(
        widget=forms.TextInput(attrs={"class": "form-control"})
    )
    last_name = forms.CharField(widget=forms.TextInput(attrs={"class": "form-control"}))
    email = forms.EmailField(widget=forms.EmailInput(attrs={"class": "form-control"}))
    username = forms.CharField(widget=forms.TextInput(attrs={"class": "form-control"}))
    password1 = forms.CharField(
        widget=forms.PasswordInput(attrs={"class": "form-control"})
    )
    password2 = forms.CharField(
        widget=forms.PasswordInput(attrs={"class": "form-control"})
    )

    class Meta:
        model = UserAddData
        fields = [
            "first_name",
            "last_name",
            "email",
            "username",
            "password1",
            "password2",
        ]


class LoginAuthenticate(AuthenticationForm):
    username = forms.EmailField(
        widget=forms.EmailInput(attrs={"class": "form-control w-100"})
    )
    password = forms.CharField(
        widget=forms.PasswordInput(attrs={"class": "form-control w-100 py-1"})
    )


# class Recipesform(forms.ModelForm):
#     categories=[
#         ('appetizer','Appetizer'),('main_dish','Main Dish'),('dessert','Dessert')
#     ]
#     recipe_name=forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))
#     category=forms.ChoiceField(choices=categories,widget=forms.Select(attrs={'class':'form-control'}))
#     incredients=forms.CharField(widget=forms.Textarea(attrs={'class':'form-control ','rows':'7'}))
#     nutrients=forms.CharField(widget=forms.Textarea(attrs={'class':'form-control','rows':'7'}))
#     recipe=forms.CharField(widget=forms.Textarea(attrs={'class':'form-control','rows':'15'}))
#     image=forms.ImageField(widget=forms.FileInput(attrs={'class':'form-control'}))

#     class Meta:
#         model = Recipes
#         fields=['recipe_name','category','incredients','nutrients','recipe','image'

#                 ]
