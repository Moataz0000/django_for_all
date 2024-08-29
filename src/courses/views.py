from django.shortcuts import render,get_object_or_404

from .models import Course



def list_of_courses(request):
    courses = Course.objects.filter(status=Course.Status.PUBLISHED)
    return render(request, 'courses/list_courses.html', {'courses':courses})




def course_detail(request, slug):
    course = get_object_or_404(Course, slug=slug, status=Course.Status.PUBLISHED)
    return render(request, 'courses/course_detail.html', {'course':course})