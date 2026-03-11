from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import Course, Lesson, Category, Enrollment, Progress, User

class LessonInline(admin.TabularInline):
    model = Lesson
    extra = 1


@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):

    list_display = ('title', 'instructor', 'category', 'created_at')

    search_fields = ('title',)

    list_filter = ('category',)

    inlines = [LessonInline]


@admin.register(Enrollment)
class EnrollmentAdmin(admin.ModelAdmin):

    list_display = ('student', 'course', 'enrolled_at')

    search_fields = ('student__username',)


admin.site.register(User)
admin.site.register(Category)
admin.site.register(Lesson)
admin.site.register(Progress)