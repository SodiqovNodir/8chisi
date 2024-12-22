from lib2to3.fixes.fix_input import context

from django.core.handlers.wsgi import WSGIRequest
from django.shortcuts import render

from news.models import Course, Lesson


def asosiy(request: WSGIRequest):
    courses = Course.objects.all()
    lessons = Lesson.objects.all()
    contexts = {
        'courses' : courses,
        'lessons': lessons,
    }

    return render(request, 'index.html', context = contexts)

def tanlangan(request, course_id):
    courses = Course.objects.all()
    lessons = Lesson.objects.filter(course = course_id)
    contexts = {
        'courses' : courses,
        'lessons' : lessons,
    }

    return render(request, 'index.html', context = contexts)

def batafsil(request, lesson_id):
    lesson = Lesson.objects.get(id = lesson_id)
    contexts = {
        'lesson': lesson,
    }

    return render(request, 'batafsil.html', context=contexts)