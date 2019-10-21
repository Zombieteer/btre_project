from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'), # root path # home page
    path('about', views.about, name='about')
]