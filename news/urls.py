from news.views import asosiy, tanlangan, batafsil, add_course, add_lesson, update_course, update_lesson, register, login_user, logout_user
from django.urls import path

urlpatterns = [
    path('', asosiy, name = 'asos'),
    path('course/<int:course_id>/', tanlangan, name = 'tanlangan'),
    path('lessons/<int:lesson_id>/', batafsil, name = 'batafsil'),
    path('course/<int:course_id>/update', update_course, name = 'update_course'),
    path('lesson/<int:lesson_id>/update', update_lesson, name='update_lesson'),

    path('auth/register/', register, name = 'register'),
    path('auth/login/', login_user, name = 'login_user'),
    path('auth/logout/', logout_user, name='logout'),

    path('course/add/', add_course, name = 'add_course'),
    path('lesson/add/', add_lesson, name = 'add_lesson'),
]