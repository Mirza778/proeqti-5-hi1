from django.urls import path
from . import views
urlpatterns = [
    path('student/get/<int:id>/', views.student_get),
    path('student/get-all/', views.student_get_all),
    path('teacher/get/<int:id>/', views.teacher_get),
    path('teacher/get-all/', views.teacher_get_all),
    path('class/get/<int:id>/', views.class_get),
    path('class/get-all/', views.class_get_all),
]
