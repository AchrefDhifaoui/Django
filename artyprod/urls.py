from django.urls import path, include
from . import views
from .views import *
urlpatterns = [
    path('', views.index, name='index'),
    path('project/<int:project_id>/', views.project_detail, name='project_detail'),
    path('login', views.login_registration, name='login'),
    path('logout/', logout_view, name='logout'),
    path('demande_project/', views.demande_project, name='demande_project'),
    path('my_projects/', views.my_projects, name='my_projects'),
]
