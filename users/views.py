from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import RegisterForm, UserUpdateForm, ProfileUpdateForm


def register(request, *args, **kwargs):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save(*args, **kwargs)
            username = form.cleaned_data.get('username')
            messages.success(request, f'User {username} created, you can log in now!')
            return redirect('login')
    else:
        form = RegisterForm()
    return render(request, 'users/register.html', {'form':form})


@login_required
def profile(request):

    if request.method == 'POST':
        u_form = UserUpdateForm(request.POST, instance=request.user)
        p_form = ProfileUpdateForm(request.POST, instance=request.user.profile, files=request.FILES)
        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            messages.success(request, f'Your profile has been updated')
            return redirect('profile')
    else:
        u_form = UserUpdateForm(instance=request.user)
        p_form = ProfileUpdateForm(instance=request.user.profile)
    
    context = {'u_form':u_form, 'p_form':p_form}
    return render(request, 'users/profile.html', context)
