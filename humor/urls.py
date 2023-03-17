from django.urls import path
from . import views

urlpatterns = [
	path('', views.home, name="home"),
	path('crazy_pics/', views.crazy_pics, name="crazy_pics"),
	path('say_something/', views.say_something, name="say_something"),
	path('upload_image/', views.upload_image, name="upload_image"),
]