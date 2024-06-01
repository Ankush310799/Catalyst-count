# core/urls.py

from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.user_login, name='login'),
    path('signup/', views.user_signup, name='signup'),
    path('logout/', views.user_logout, name='logout'),
    path('upload/', views.upload_file, name='upload_file'),
    path('query/', views.query_builder, name='query_builder'),
    path('query_count/',views.query_count, name='query_count'),
    path('users/', views.user_list, name='user_list'),
    path('delete_user/<int:user_id>/', views.delete_user, name='delete_user')


]
