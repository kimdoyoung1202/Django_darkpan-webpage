from django import forms
from .models import Employees

class EmployeesForm(forms.ModelForm) :
    
    class Meta :
        model = Employees
        fields = ["emp_no", "birth_date", "first_name", "last_name", "gender", "hire_date"]
        widgets = {
            "emp_no" : forms.TextInput(attrs={
                "class" : "form-control",
                "placeholder" : "Employee Number",
                }
            ),
            "birth_date" : forms.DateInput(attrs={
                "class" :  "form-control",
                "type": "date",
                }
            ),
            "first_name" : forms.TextInput(attrs={
                "class" : "form-control",
                "placeholder" : "이름",
                }
            ),
            "last_name" : forms.TextInput(attrs={
                "class" : "form-control",
                "placeholder" : "성",
                }
            ),
            "gender" : forms.TextInput(attrs={
                "class" : "form-control",
                "placeholder" : "성별",
                }
            ),
            "hire_date" : forms.DateInput(attrs={
                "class" : "form-control",
                "type": "date",
                }
            ),
        }