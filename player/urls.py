from django.urls import path
from . import views

app_name = 'player'

urlpatterns = [
    path('', views.player_view, name='player'),
    path('<int:course_id>/<int:module_id>/<int:submodule_id>/', views.player_view, name='player_view'),
]