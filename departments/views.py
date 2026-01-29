from django.shortcuts import render
from django.http import JsonResponse
from departments.models import Departments
from django.forms.models import model_to_dict
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy

from .form import DepartmentForm 

# Create your views here.
def read(request) :
    # TODO : 비즈니스 로직 호출
    return JsonResponse({
        "message" : "read called"    
    })
    

def search(request) :
    # TODO : 데이터베이스 조회
    dept_no = request.GET.get("dept_no")
    dept_name = request.GET.get("dept_name")
    
    # 아무것도 없을때
    qs = Departments.objects.all()
    
    # dept_no만 주어졌을때
    if dept_no:
        qs = qs.filter(dept_no=dept_no)
    
    # dept_name만 주어졌을때
    if dept_name:
        qs = qs.filter(dept_name=dept_name)
        
    # 두가지 방법 리스트 내포로 디셔너리로 바로 저장
    # model_to_dict 함수로 날것으로 저장이 아닌 바로 저장
    departments =[{"dept_no":departments.dept_no, "dept_name":department.dept_name} for department in qs]
    
    # list형태로 만들어서 사용
    data = list(qs.values("dept_no", "dept_name"))
    
    return JsonResponse(data, safe=False)

class DepartmentsListView(ListView) :
    model = Departments
    template_name = "departments/department_list.html"
    context_object_name = "departments"
    
    def get_queryset(self):
        queryset = super().get_queryset()
        dept_no = self.request.GET.get("dept_no")

        if dept_no :
            queryset = queryset.filter(dept_no=dept_no)

        queryset = queryset.order_by("dept_no")
        return queryset


class DepartmentsCreateView(CreateView) :
    model = Departments
    #fields = ["dept_no", "dept_name"]
    template_name = "departments/department_form.html"
    success_url = reverse_lazy("departments:department_list")
    form_class = DepartmentForm
    

class DepartmentsUpdateView(UpdateView) :
    model = Departments
    template_name = "departments/department_form.html"
    success_url = reverse_lazy("departments:department_list")
    form_class = DepartmentForm
    pk_url_kwarg = "dept_no"
    
class DepartmentsDeleteView(DeleteView) :
    model = Departments
    success_url = reverse_lazy("departments:department_list")