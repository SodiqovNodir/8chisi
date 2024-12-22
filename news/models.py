import msilib

from django.conf.global_settings import MEDIA_URL
from django.db import models

class Course(models.Model):
    name = models.CharField(max_length=50)
    content = models.TextField()
    created = models.DateTimeField(auto_now=True)
    photo = models.ImageField(upload_to='course/photo', blank=True, null=True)

    def __str__(self):
        return self.name

class Lesson(models.Model):
    name = models.CharField(max_length=25)
    content = models.TextField()
    created = models.DateTimeField(auto_now=True)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

