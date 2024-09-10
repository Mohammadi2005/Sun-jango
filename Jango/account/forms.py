from django import forms

class LoginForm(forms.Form):
    Username = forms.CharField(widget=forms.TextInput(
        attrs={'class':'form-control', 'placeholder':'Enter Username'}))
    Password = forms.CharField(widget=forms.PasswordInput(
        attrs={'class':'form-control', 'placeholder':'Enter your Password'}))