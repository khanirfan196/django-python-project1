from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpRequest
from .forms import RegistrationForm
from django.contrib.auth import login, authenticate
from django.contrib.auth.decorators import login_required
from .models import Account


# Create your views here.

def myhome(request):
    return render(request, 'userapp/home.html')


def registration_view(request):
    context = {}
    if request.POST:
        form = RegistrationForm(request.POST)
        if form.is_valid():                     # checks whether form is valid or not
            form.save()                         # saves the form
            email = form.cleaned_data.get('email')  # getting email from the html field.
            raw_password = form.cleaned_data.get('password1')   # getting password from the html field.
            account = authenticate(email=email, password=raw_password)  # authenticating the user by email and password
            login(request, account)
            return redirect('home-page')
        else:
            form = RegistrationForm()
    else:
        form = RegistrationForm()
        #context['registration_form'] = form
    return render(request,'userapp/register.html', {'form': form})

@login_required
def success_view(request):
    user_v = Account.objects.first()
    return render(request, 'userapp/success.html',{'user' :user_v.username})