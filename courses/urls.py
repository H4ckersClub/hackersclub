from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('courses/<int:course_id>/', views.course_detail, name='course_detail'),
    path('register/', views.register_view, name='register'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
]