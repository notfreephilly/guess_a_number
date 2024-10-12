
from django.contrib import admin
from django.urls import path
from guessinggame import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.number_guessing_game, name='home')
]
