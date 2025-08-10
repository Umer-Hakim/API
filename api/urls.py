from django.urls import path, include
from rest_framework.routers import DefaultRouter

from . import views


router = DefaultRouter()
router.register('employees', views.EmployeeViewset, basename='employee')


urlpatterns = [
    path('students/', views.studentView),
    path('student/<int:pk>/', views.studentDetialsView),

    # path('employees/', views.Employees.as_view()),
    # path('employees/<int:pk>/', views.EmployeeDetails.as_view()),

    path('', include(router.urls)),


    path('blogs/', views.BlogsView.as_view()),
    path('comments/', views.CommentsView.as_view()),

    path('blogs/<int:pk>/', views.BlogDetailsView.as_view()),
    path('comments/<int:pk>/', views.CommentDetailsView.as_view()),
]

