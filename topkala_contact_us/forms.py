from django import forms
from django.core import validators


class ContactForm(forms.Form):
    full_name = forms.CharField(widget=forms.TextInput(
        attrs={"class": "form-control  <abbr title='required' class='required'>*</abbr>",
               "placeholder": "لطفا نام و نام خانوادگی خود را وارد کنید "}),
        label='نام و نام خانوادگی',
        validators=[validators.MaxLengthValidator(150, 'نام و نام خانوادگی شما نمیتواند بیشتر از 150 کاراکتر باشد')])

    email = forms.EmailField(
        widget=forms.EmailInput(attrs={"class": "form-control", "placeholder": "لطفا ایمیل خود را وارد کنید"}),
        label='ایمیل',
        validators=[validators.MaxLengthValidator(100, 'ایمیل شما نمیتواند بیشتر از 100 کاراکتر باشد')])

    subject = forms.CharField(
        label='عنوان',
        widget=forms.TextInput(attrs={"class": "form-control", "placeholder": "لطفا عنوان پیام خود را وارد کنید"}),
        validators=[validators.MaxLengthValidator(200, 'عنوان پیام شما نمیتواند بیشتر از 200 کاراکتر باشد')])

    text = forms.CharField(
        label='متن پیام',
        widget=forms.Textarea(attrs={"class": "form-control", "placeholder": "لطفا متن پیام خود را وارد کنید"}))
