from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse 
from django.core.handlers.wsgi import WSGIRequest
# Create your views here.


def home(request : WSGIRequest) :
    print("--- User Debug Start ---")
    print(f"User: {request.user}")
    print(f"ID: {request.user.id}")
    return render(request, "dashboard/dashboard_chart.html")