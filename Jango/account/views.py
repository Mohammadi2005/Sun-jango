from django.shortcuts import render, redirect
from .forms import LoginForm, RegisterForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User

# Create your views here.
def log_in(request):
    if request.method == 'GET':
        form = LoginForm()
    else:
        form = LoginForm(request.POST)
        if form.is_valid():
            print(form.cleaned_data)
            username_input = form.cleaned_data.get('Username')
            password_input = form.cleaned_data.get('Password')
            user = authenticate(request, username=username_input, password=password_input)
            if user is not None:
                login(request, user)
                return redirect("home:art_list")
            else:
                form.add_error('Password', 'Incorrect username or password')
    print("error")
    return render(request, 'login_page.html', {'form': form})

def register(request):
    if request.user.is_authenticated:
        return redirect("home:home")
    register_form = RegisterForm()
    if request.method == 'POST':
        register_form = RegisterForm(request.POST)
        if register_form.is_valid():
            # Create a new user
            username = register_form.cleaned_data.get('Username')
            password = register_form.cleaned_data.get('Password')
            first_name = register_form.cleaned_data.get('FirstName')
            last_name = register_form.cleaned_data.get('LastName')
            email = register_form.cleaned_data.get('Email')
            user = User.objects.create_user(username=username, password=password, first_name=first_name, last_name=last_name, email=email)
            # # به دو شکل میشه اطلاعات رو به یوزر داد
            user.save()
            return redirect("home:home")

    return render(request, 'register_page.html', {'register_form': register_form})

def log_out(request):
    logout(request)
    return redirect("home:home")