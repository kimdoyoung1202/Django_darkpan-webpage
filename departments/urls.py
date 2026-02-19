from django.urls import path
from . import views

app_name = "departments"

urlpatterns = [
    path('read/', views.read),
    path('search/',views.search),
    path('search-list/', views.DepartmentsListView.as_view(), name ="department_list"),
    path('add/', views.DepartmentsCreateView.as_view(), name="department_add"),
    path('<str:dept_no>/edit',views.DepartmentsUpdateView.as_view(), name="department_update"),
    path('delete/<str:pk>', views.DepartmentsDeleteView.as_view(), name="department_delete"),
    path('fetch-live/', views.fetch_live),
    path('fetch-sleep/', views.fetch_sleep),
]

