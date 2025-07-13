from django.urls import path
from . import views

app_name = 'course_manager'

urlpatterns = [
    # Add your CRUD paths here
    path('', vews.course_list, name='course_list')
]