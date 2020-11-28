from django.shortcuts import render, redirect
from . forms import RegisterForm, ProfileUpdateForm, UserUpdateForm
from django.contrib.auth.decorators import login_required
from django.contrib import messages

# Create your views here.


# for register users
def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f"account created for {username} !")
            return redirect("login")
    else:
        form = RegisterForm()
    return render(request, 'users/register.html', {'form': form})


# for profile page
@login_required
def Profile(request):
    if request.method == 'POST':
        p_form = ProfileUpdateForm(
            request.POST, request.FILES, instance=request.user.profile)
        u_form = UserUpdateForm(request.POST, instance=request.user)
        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            messages.success(request, f"account has been updated !!!")
            return redirect("profile")
    else:
        u_form = UserUpdateForm(instance=request.user)
        p_form = ProfileUpdateForm(instance=request.user.profile)

    context = {
        'u_form': u_form,
        'p_form': p_form
    }
    return render(request, 'users/profile.html', context)
