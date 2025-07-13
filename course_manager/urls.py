from django.urls import path
from . import views

app_name = 'course_manager'

urlpatterns = [
    # Add your CRUD paths here
    path('', views.course_list_view, name='course_list'),
    path('courses/', views.course_list_view, name='course_list'),
    path('courses/add', views.course_create_view, name='course_create')
]