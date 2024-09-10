from django.shortcuts import render
from . import forms


# Create your views here.
def login(request):
    if request.method == 'GET':
        form = forms.LoginForm()
    else:
        form = forms.LoginForm(request.POST)
        if form.is_valid():
            pass
    return render(request, 'login_page.html', {'form': form})