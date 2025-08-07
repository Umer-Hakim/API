from django.urls import path

from . import views


urlpatterns = [
    path('students/', views.studentView),
    path('student/<int:pk>/', views.studentDetialsView),

    path('employees/', views.Employees.as_view()),
    path('employees/<int:pk>/', views.EmployeeDetails.as_view()),
]

