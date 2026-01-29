from django.shortcuts import render
from django.contrib.auth import logout
from django.shortcuts import redirect
from django.urls import reverse

# Create your views here.
def logout_view(request) :
    logout(request)
    login_url = reverse("login")
    return redirect(login_url)