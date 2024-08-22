from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import Course


def index(request):
    courses = Course.objects.all()
    
    return render(request=request, template_name='shop/courses.html', context={ 'courses': courses })


def single_course(request, course_id):
    course = get_object_or_404(Course, pk=course_id)

    return render(request=request, template_name='shop/single_course.html', context={ 'course': course })