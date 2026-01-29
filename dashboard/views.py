from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse 
from django.core.handlers.wsgi import WSGIRequest
import logging
# Create your views here.

logger = logging.getLogger(__name__)

def home(request : WSGIRequest) :
    logger.info("Login : " + request.user.first_name + request.user.last_name)
    
    chart_labels = [40, 50, 60, 70, 80, 90, 100]
    chart_data = [10, 9, 8, 7, 8, 9, 10]
    
    return render(request, "dashboard/dashboard_chart.html", {
        "chart_labels" : chart_labels,
        "chart_data": chart_data,
    })