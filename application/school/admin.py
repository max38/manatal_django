from django.contrib import admin
from .models import School, Student


@admin.register(School)
class SchoolAdmin(admin.ModelAdmin):
    list_display = ('name', 'maximum_student')
    search_fields = ('name',)


@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ('id', 'first_name', 'last_name', 'school',)
    search_fields = ('id', 'first_name', 'last_name',)
    list_filter = ('school',)
