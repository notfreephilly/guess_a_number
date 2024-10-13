from django.urls import path
from . import views


urlpatterns = [
    path('', views.number_guessing_game, name='home'),
]