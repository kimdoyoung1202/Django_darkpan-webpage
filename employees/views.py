from django.shortcuts import render
from django.http import HttpResponse
from django.core.handlers.wsgi import WSGIRequest
from django.views.decorators.http import require_GET
from django.views import View
from .models import Employees
from django.views.generic import ListView, CreateView
from django.urls import reverse_lazy

from .form import EmployeesForm


# Create your views here.
def read(request) :
    # TODO :  실무라면 service(비즈니스 로직)호출
    return render(request, "employees/list.html", {
        "name" : "doyoung"
    })

def table(request) :
    
    users = [
        {"id" : 1, "first_name" : "KIM", "last_name" : "DoYoung", "email" : "smile4819@email.com"},
        {"id" : 2, "first_name" : "Go", "last_name" : "rani", "email" : "gorani@email.com"},
        {"id" : 3, "first_name" : "an", "last_name" : "sang", "email" : "ansang@email.com"},
    ]
    
    return render(request, "employees/table.html", {"users" : users, "img" : "img/dog.png", "name": "DoYoung", "salary":1000000000})

def search(request : WSGIRequest) :
    
    if request.method == "GET" :
        pass
    elif request.method == "POST" :
        pass
    
    return HttpResponse(request.method)


@require_GET
def search_get(request) :
    pass

# This class likely represents a view for displaying employee information in a web application


class EmployeesView(View) :
    def get(self, request) :
        return render(request, "employees/employee_list.html")
        
    def post(self, request) :
        
        emp_no = request.POST.get("emp_no") 
        first_name = request.POST.get("first_name")
        qs = Employees.objects.all()
        
        if emp_no and emp_no.isdigit():
            qs = qs.filter(emp_no=int(emp_no))
        
        if first_name :
            qs = qs.filter(first_name=first_name)

        # if emp_no and emp_no.isdigit() :
        #     qs = qs.filter(emp_no=int(emp_no))

        context = {"employees" : qs}
        
        
        return render(request, "employees/employee_list.html", context)
        #return render(request, "employees/employee_list.html", context)
        

def child_test(request) :
    return render(request, "employees/child.html")


class EmployeesSearchView(ListView):
    model = Employees
    template_name = "employees/employees_search.html"
    paginate_by = 20
    
    
class EmployeesCreateView(CreateView) :
    model = Employees
    #fields = ["emp_no", "birth_date", "first_name", "last_name", "gender", "hire_date"]
    template_name = "employees/employees_form.html"
    success_url = reverse_lazy("employees:employee_list")
    form_class = EmployeesForm