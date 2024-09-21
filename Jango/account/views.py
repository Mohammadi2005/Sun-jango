from django.shortcuts import render, redirect
from .forms import LoginForm, RegisterForm
from django.contrib.auth import authenticate, login, logout

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
    return render(request, 'register_page.html', {'register_form': register_form})

def log_out(request):
    logout(request)
    print("logged out")
    print("logged out")
    return redirect("home:home")