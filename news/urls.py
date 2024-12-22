from news.views import asosiy, tanlangan, batafsil
from django.urls import path

urlpatterns = [
    path('', asosiy, name = 'asos'),
    path('course/<int:course_id>/', tanlangan, name = 'tanlangan'),
    path('lessons/<int:lesson_id>/', batafsil, name = 'batafsil'),
]