from django.shortcuts import render, redirect
from django.contrib import messages, auth
from contact.forms import RegisterForm, RegisterUpdateForm
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required

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

@login_required(login_url='login')
def logout(request):
    auth.logout(request)
    return redirect('login')

@login_required(login_url='login')
def user_update(request):

    form = RegisterUpdateForm(instance=request.user)
    
    if request.method != 'POST':
        return render(
            request,
            'contact/register.html',
            {
                'form': form,
                'site_title': 'Update data',
            }
        )

    form = RegisterUpdateForm(data=request.POST, instance=request.user)

    if not form.is_valid():
        return render(
            request,
            'contact/register.html',
            {
                'form': form,
                'site_title': 'Update data',
            }
        )
    
    form.save()
    messages.success(request, 'Update successful!')
    return redirect('home')