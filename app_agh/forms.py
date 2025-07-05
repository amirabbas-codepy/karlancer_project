
from django import forms

class RegisterForm(forms.Form):
    # firstname = forms.CharField(max_length=200, required=True, label='نام')
    # lastname = forms.CharField(max_length=200, required=True, label='نام خانوادگی')
    # phonenumber = forms.CharField(max_length=11, min_length=11,required=True, label='شماره موبایل')
    username = forms.CharField(max_length=200,required=True, label='نام کاربری')
    password = forms.CharField(max_length=200, required=True, label='رمز عبور')

class LoginForm(forms.Form):
    username = forms.CharField(max_length=11, required=True, label='نام کاربری')
    password = forms.CharField(max_length=200, required=True, label='رمز عبور')

class SerchForm(forms.Form):
    value = forms.CharField(max_length=200, required=True, label='جستجو کنید') 

class AdvertisementForm(forms.Form):
    name = forms.CharField(max_length=200, required=True, label='نام ابزار')
    title = forms.CharField(max_length=200, required=True, label='عنوان')
    price = forms.IntegerField(required=True, label='قیمت')
    image = forms.FileField(required=True, label='عکس محصول')
    descripitions = forms.CharField(widget=forms.Textarea(), required=True, label='توصیحات')
    connection_path = forms.CharField(max_length=11, min_length=11,required=True, label='شماره تماس شما')