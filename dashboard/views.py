from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse 
from django.core.handlers.wsgi import WSGIRequest
import logging
# Create your views here.

logger = logging.getLogger(__name__)

def home(request : WSGIRequest) :
    logger.info("Login : " + request.user.first_name + request.user.last_name)
    return render(request, "dashboard/dashboard_chart.html")