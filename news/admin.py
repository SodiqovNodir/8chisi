from django.contrib import admin
from django.utils.safestring import mark_safe


from .models import Course, Lesson

class CourseAdmin(admin.ModelAdmin):
    list_display = ('name', 'get_photo','created')
    list_display_links = ('name',)
    search_fields = ('name', 'content', 'created')
    list_filter = ('name',)

    def get_photo(self, course):
        if course.photo:
            return mark_safe(f'<img src="{course.photo.url}" width=150px')
        return '-'

admin.site.register(Course, CourseAdmin)

class LessonAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'created', 'course')
    list_editable = ('course',)
    list_display_links = ('name',)
    list_filter = ('course',)
    search_fields = ('name', 'content', 'created')

admin.site.register(Lesson, LessonAdmin)
