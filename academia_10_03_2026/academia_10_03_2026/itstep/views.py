from django.shortcuts import render

from .models import Teacher, Course, Student


def home(request):
    """Головна сторінка академії."""
    return render(request, "itstep/home.html")


def teacher_list(request):
    """Уявлення: виведення усіх викладачів."""
    teachers = Teacher.objects.all()
    return render(request, "itstep/teacher_list.html", {"teachers": teachers})


def course_list(request):
    """Уявлення: виведення усіх курсів."""
    courses = Course.objects.all()
    return render(request, "itstep/course_list.html", {"courses": courses})


def student_list(request):
    """Уявлення: виведення усіх студентів."""
    students = Student.objects.all()
    return render(request, "itstep/student_list.html", {"students": students})
