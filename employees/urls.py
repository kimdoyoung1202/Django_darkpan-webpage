from django.urls import path
from . import views

app_name = 'employees'

urlpatterns = [
    path('read/', views.read),
    path('table/', views.table),
    path('search/', views.search),
    path('search-cbv/', views.EmployeesView.as_view(),name ="employee_list"),
    path('child-test/', views.child_test),
    path('search-list/', views.EmployeesSearchView.as_view()),
    path('add/',views.EmployeesCreateView.as_view()),
]