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
