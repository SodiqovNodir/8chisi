from django.core.handlers.wsgi import WSGIRequest
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.models import User
from django.contrib.auth import login, logout, authenticate
from django.contrib import messages

from news.models import Course, Lesson, Comment
from .forms import CourseForm, LessonForm, RegisterForm, LoginForm, CommentForm

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

def update_course(request:WSGIRequest, course_id):
    
    course = get_object_or_404(Course, pk = course_id)

    if request.method == 'POST':
        form = CourseForm(data=request.POST, files=request.FILES)
        if form.is_valid():
            course.name = form.cleaned_data.get('name')
            course.content = form.cleaned_data.get('content')
            course.photo = form.cleaned_data.get('photo') if form.cleaned_data.get('photo') else course.rasm
            course.created = form.cleaned_data.get('created')
            course.save()


    form = CourseForm(initial={
        'name': course.name,
        'photo': course.photo,
        'content':course.content,
        'created': course.created,
    })

    contexts = {
        'form' : form,
        'photo':course.photo
    }
    return render(request, 'add_course.html', context = contexts)

def update_lesson(request:WSGIRequest, lesson_id):
    lesson = get_object_or_404(Lesson, pk = lesson_id)

    if request.method == 'POST':
        form = LessonForm(data=request.POST, files=request.FILES)
        if form.is_valid():
            lesson.name = form.cleaned_data.get('name')
            lesson.content = form.cleaned_data.get('content')
            lesson.created = form.cleaned_data.get('created')
            lesson.course = form.cleaned_data.get('course')
            lesson.save()


    form = LessonForm(initial={
        'name': lesson.name,
        'content':lesson.content,
        'created': lesson.created,
        'course': lesson.course
    })

    contexts = {
        'form' : form,
    }
    return render(request, 'add_lesson.html', context = contexts)

def register(request):
    if request.method == 'POST':
        form = RegisterForm(data=request.POST)
        if form.is_valid():
            password = form.cleaned_data.get('password')
            password_repeat = form.cleaned_data.get('password_repeat')
            if password_repeat == password:
                user = User.objects.create_user(
                    form.cleaned_data.get('username'),
                    form.cleaned_data.get('email'),
                    password
                )
                messages.success(request, 'Akount yaratildi 😍🥰')
                return redirect('login_user')
    context = {
            'form': RegisterForm()
    }
    return render(request, 'auth/register.html', context)

def login_user(request):
    if request.method == 'POST':
        form = LoginForm(data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username = username, password = password)
            messages.success(request, 'Xush kelibsiz😍☺️')
            login(request, user)
            return redirect('asos')
    context = {
        'form':LoginForm(),
    }
    return render(request, 'auth/login.html', context)

def logout_user(request):
    logout(request)
    return redirect('login_user')

def comment_save(request:WSGIRequest, lesson_id):
    if request.user.authenticated:
        if request.method == "POST":
            comment = CommentForm(data=request.POST)
            if comment.is_valid():
                lesson = get_object_or_404(Lesson, pk = lesson_id)
                com = Comment.objects.create(
                    text = lesson.cleaned_data.get('text'),
                    author = request.user,
                    lesson = lesson,
                )
                messages.success(request, "Comment qo'shildi.")

        return redirect("batafsil", lesson_id = lesson_id)
    messages.error(request, "Avval ro'yhatdan o'ting")
    return redirect('login_user')

def comment_delete(request, comment_id):
    if request.user.is_aauthenticated:
        comment = get_object_or_404(Comment, pk = comment_id)
        if request.user == comment.author or request.user.is_superuser:
            lesson_id = comment.lesson.pk
            comment.delete()
            messages.success(request, "Comment o'chirildi")
            return redirect('batafsil', lessom_id = lesson_id)

    messages.error(request, "Avval ro'yhatdan o'ting")
    return redirect('login_user')

def update_comment(request:WSGIRequest, comment_id):
    comment = get_object_or_404(Comment, pk = comment_id)

    if request.method == 'POST':
        form = CommentForm(data=request.POST, files=request.FILES)
        if form.is_valid():
            comment.author = form.cleaned_data.get('author')
            comment.text = form.cleaned_data.get('text')
            comment.created = form.cleaned_data.get('created')
            comment.lesson = form.cleaned_data.get('lesson')
            comment.save()

    form = CommentForm(initial={
        'author': comment.author,
        'text':comment.text,
        'created': comment.created,
        'lesson': comment.lesson,
    })

    contexts = {
        'form' : form,
    }
    return render(request, 'add_gul.html', context = contexts)




