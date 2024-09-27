from django import forms
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError


class LoginForm(forms.Form):
    Username = forms.CharField(widget=forms.TextInput(
        attrs={'class':'form-control', 'placeholder':'Enter Username'}))
    Password = forms.CharField(widget=forms.PasswordInput(
        attrs={'class':'form-control', 'placeholder':'Enter your Password'}))


class RegisterForm(forms.Form):
    Username = forms.CharField(widget=forms.TextInput(
        attrs={'class':'form-control', 'placeholder':'Enter Username'}))
    Password = forms.CharField(widget=forms.PasswordInput(
        attrs={'class':'form-control', 'placeholder':'Enter your Password'}))
    Password_2 = forms.CharField(widget=forms.PasswordInput(
        attrs={'class':'form-control', 'placeholder':'Enter your Password again'}))
    FirstName = forms.CharField(widget=forms.TextInput(
        attrs={'class':'form-control', 'placeholder':'Enter First Name'}))
    LastName = forms.CharField(widget=forms.TextInput(
        attrs={'class':'form-control', 'placeholder':'Enter Last Name'}))
    Email = forms.EmailField(widget=forms.EmailInput(
        attrs={'class':'form-control', 'placeholder':'Enter Email'}))

# ین تابع بررسی میکنه که یوزر نیم تکراری وارد نشه
    def clean_Username(self):
        username_input = self.cleaned_data['Username'] # یوزر نیمی که کاربر وارد کرده رو میگیره
        user = User.objects.filter(username=username_input)
        # یوزری رو میگیره که یوزر نیمش برابر با یوزر نیم ورودی باشه
        print(f" user is : {user} ")
        if user:
            raise ValidationError('Username already exists')
        return username_input

    def clean_Password_2(self):
        password_input = self.cleaned_data['Password']
        password_input2 = self.cleaned_data['Password_2']
        if password_input != password_input2:
            raise ValidationError('Passwords do not match')
        return password_input

    def clean_Email(self):
        email_input = self.cleaned_data['Email']
        user = User.objects.filter(email=email_input).exists()
        if user:
            raise ValidationError('this Email is exists')
        return email_input


