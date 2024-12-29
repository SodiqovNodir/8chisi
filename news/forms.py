from django import forms

from news.models import Course


class CourseForm(forms.Form):
    name = forms.CharField(max_length=50, widget=forms.TextInput())
    content = forms.CharField(widget=forms.Textarea())
    created = forms.DateTimeField(widget=forms.DateTimeInput())
    photo = forms.ImageField(widget=forms.FileInput())

class LessonForm(forms.Form):
    name = forms.CharField(widget=forms.TextInput())
    content = forms.CharField(widget=forms.Textarea())
    created = forms.DateTimeField(widget=forms.DateTimeInput())
    course = forms.ModelChoiceField(queryset=Course.objects.all(), widget=forms.Select())

class RegisterForm(forms.Form):
    username = forms.CharField(max_length=50, widget=forms.TextInput())
    email = forms.EmailField(widget=forms.EmailInput())
    password = forms.CharField(min_length=8, widget=forms.PasswordInput())
    password_repeat = forms.CharField(min_length=8, widget=forms.PasswordInput())

class LoginForm(forms.Form):
    username = forms.CharField(max_length=50, widget=forms.TextInput())
    password = forms.CharField(min_length=8, widget=forms.PasswordInput())

