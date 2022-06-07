from django.urls import re_path
from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', views.home, name = 'home'),
    path('movie/', views.movie, name = 'movie'),
    path('director/', views.director, name = 'director'),
    path('actor/', views.actor, name = 'actor'),
    path('recommendation/', views.recommendation, name = 'recommendation'),
    path('insert_data/', views.insert_data, name = 'insert_data'),
    path('insert_data_submission/', views.insert_data_submission, name = 'insert_data_submission'),
    path('new_movie/', views.new_movie, name='new_movie'),
    path('register', views.register, name='register'),
    path('login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='logout.html'), name='logout'),
    re_path(r'^edit_movie/(?P<pk>\d+)/$', views.edit_movie, name='edit_movie'),
    re_path(r'^recommedation/$', views.search, name='search'),
    path('password_reset/', auth_views.PasswordResetView.as_view(), name='password_reset'),
    path('password_reset/done/', auth_views.PasswordResetDoneView.as_view(), name = 'password_reset_done'),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(), name = 'password_reset_confirm'),
    path('reset/done/', auth_views.PasswordResetCompleteView.as_view(), name = 'password_reset_complete'),

]