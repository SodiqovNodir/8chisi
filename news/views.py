from django.core.handlers.wsgi import WSGIRequest
from django.shortcuts import render

from news.models import Course, Lesson
from .forms import CourseForm, LessonForm

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

def add_course(request: WSGIRequest):

    if request.method == 'POST':
        course = CourseForm(data=request.POST, files=request.FILES)
        if course.is_valid():
            Course.objects.create(**course.cleaned_data)

    courses = CourseForm()
    contexts = {
        'courses' : courses,
    }
    return render(request, 'add_course.html', context = contexts)

def add_lesson(request: WSGIRequest):

    if request.method == 'POST':
        lesson = LessonForm(data=request.POST, files=request.FILES)
        if lesson.is_valid():
            Lesson.objects.create(**lesson.cleaned_data)

    lessons = LessonForm()
    contexts = {
        'lessons' : lessons,
    }
    return render(request, 'add_lesson.html', context = contexts)