from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.admin.views.decorators import staff_member_required
from courses.models import Course
from .models import Module, SubModule


# Create your views here.

@staff_member_required
def course_list_view(request):
    courses = Course.objects.all()
    return render(request, 'course_manager/course_list.html', {'courses': courses})