from django import forms

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
