from django.contrib import admin
from .models import Departments

# Register your models here.
@admin.register(Departments)
class DepartmentAdmin(admin.ModelAdmin) :
    list_display = ("dept_no", "dept_name")
    search_fields = ("dept_no", "dept_name")
    list_filter = ("dept_no",)
    ordering = ("dept_no",)