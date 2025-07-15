from django.urls import path
from . import views

app_name = 'course_manager'

urlpatterns = [
    # Add your CRUD paths here
    path('', views.course_list_view, name='course_list'),
    path('courses/', views.course_list_view, name='course_list'),
    path('courses/add', views.course_create_view, name='course_create'),
    path('courses/<int:pk>/', views.course_detail, name='course_detail'),
    path('courses/<int:pk>/edit', views.course_edit_view, name='course_edit'),
    path('courses/<int:pk>/delete/', views.course_delete, name='course_delete'),
    path('courses/<int:pk>/modules/', views.course_modules, name='course_modules'),
    path('modules/', views.module_list_view, name='module_list'),
    path('modules/add/<int:course_id>/', views.module_create, name='module_create'),
    path('modules/<int:module_id>/edit/', views.module_edit, name='module_edit'),
    path('modules/<int:module_id>/delete/', views.module_delete, name='module_delete'),
    path('submodules/', views.submodule_list_view, name='submodule_list'),
    path('submodules/add/<int:module_id>/', views.submodule_create, name='submodule_create'),
    path('submodules/<int:submodule_id>/edit/', views.submodule_edit, name='submodule_edit'),
    path('submodules/<int:submodule_id>/delete/', views.submodule_delete, name='submodule_delete')
]