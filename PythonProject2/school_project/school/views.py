from django.shortcuts import render, get_object_or_404
from .models import Student, Teacher, Class

def student_get(request, id):
    student = get_object_or_404(Student, id=id)
    return render(request, 'item_detail.html', {'item': student, 'type': 'Student'})


def student_get_all(request):
    students = Student.objects.all()
    return render(request, 'items_list.html', {'items': students, 'type': 'Students'})

def teacher_get(request, id):
    teacher = get_object_or_404(Teacher, id=id)
    return render(request, 'item_detail.html', {'item': teacher, 'type': 'Teacher'})

def teacher_get_all(request):
    teachers = Teacher.objects.all()
    return render(request, 'items_list.html', {'items': teachers, 'type': 'Teachers'})
def class_get(request, id):
    class_item = get_object_or_404(Class, id=id)
    return render(request, 'item_detail.html', {'item': class_item, 'type': 'Class'})

def class_get_all(request):
    classes = Class.objects.all()
    return render(request, 'items_list.html', {'items': classes, 'type': 'Classes'})
