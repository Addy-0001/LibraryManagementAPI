from django.shortcuts import render, redirect
from django.contrib.auth import login
from .forms import CustomUserCreationForm
from django.views.generic import TemplateView
from django.contrib.auth import logout


def SignupView(request):
    if request.method == 'POST':
        user_form = CustomUserCreationForm(request.POST)
        if user_form.is_valid():
            user_form.save()
            return redirect('/login/')
    else:
        user_form = CustomUserCreationForm()
    context = {
        'form': user_form
    }
    return render(request, 'registration/signup.html', context)


def logout_page(request):
    logout(request)
    return redirect('/logged-out/')

def logged_out(request):
    template_name = 'registration/logged_out.html'
    return render(request, template_name)


class LoggedInView(TemplateView):
    template_name = 'registration/logged_in.html'
