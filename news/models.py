from django.db import models
from django.contrib.auth.models import User


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

class Comment(models.Model):
    text = models.CharField(max_length=500)
    author = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    lesson = models.ForeignKey(Lesson, on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.author.username} | {self.lesson.name[:20]} | {self.text[:20]}"