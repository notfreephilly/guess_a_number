from django.urls import path
from . import views



urlpatterns = [
    path('', views.homepage, name='home'),
    path('play', views.number_guessing_game, name='play'),
    path('register/', views.register_request, name='register'),
    path('login/', views.login_request, name='login'),
    path('profile/', views.profile, name='profile'),
]