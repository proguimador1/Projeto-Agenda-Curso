from django.shortcuts import render, redirect
from django.contrib import messages, auth
from contact.forms import RegisterForm
from django.contrib.auth.forms import AuthenticationForm

def register(request):
    form = RegisterForm()

    if request.method == 'POST':
        form = RegisterForm(request.POST)

        if form.is_valid():
            form.save()
            messages.success(request, 'Registration successful!')
            return redirect('home')


    return render(
        request,
        'contact/register.html',
        {
            'form': form,
            'site_title': 'Register',
        }
    )

def login(request):
    form = AuthenticationForm(request)

    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)

        if form.is_valid():
            user = form.get_user()
            auth.login(request, user)
            messages.success(request, 'Login successful!')
            return redirect('home') 


    return render(
        request,
        'contact/login.html',
        {
            'form': form,
            'site_title': 'Login',
        }
    )

def logout(request):
    auth.logout(request)
    return redirect('login')