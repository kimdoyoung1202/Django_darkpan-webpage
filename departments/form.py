from django import forms
from .models import Departments

class DepartmentForm(forms.ModelForm) :
    
    class Meta :
        model = Departments
        fields = ["dept_no", "dept_name"]
        widgets = {
            "dept_no" : forms.TextInput(attrs={
                "class" : "form-control",
                "placeholder" : "사원번호",
                }
            ),
            "dept_name" : forms.TextInput(attrs={
                "class" :  "form-control"
                }
            ), 
        }