from django.contrib import admin
from .models import Course, Category

admin.site.site_header = 'Courses Admin panel'
admin.site.site_title = 'Admin panel'
admin.site.index_title = 'Courses area'

class CourseAdmin(admin.ModelAdmin):
    list_display = ['title', 'id', 'category', 'price']

class CoursesInline(admin.TabularInline):
    model = Course
    exclude = ['created_at']
    extra = 0

class CategoryAdmin(admin.ModelAdmin):
    list_display = ['title', 'id', 'created_at']
    fieldsets = [
        (None, {'fields': ['title']}),
        ('Dates', { 'fields': ['created_at'], 'classes': ['collapse'] })
    ]
    inlines = [CoursesInline]

admin.site.register(Category, CategoryAdmin)
admin.site.register(Course, CourseAdmin)
