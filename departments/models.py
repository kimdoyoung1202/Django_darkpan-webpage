from django.db import models

# Create your models here.

class Departments(models.Model) :
    dept_no = models.CharField(max_length=5, primary_key=True)
    dept_name = models.CharField(max_length=40)
    
    class Meta:
        managed = False
        db_table = 'departments'