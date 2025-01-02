from django.urls import path
from . import views

urlpatterns = [
    path('', views.student_list, name='student_list'),
    path('register/', views.student_register, name='student_register'),
]
