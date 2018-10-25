from django.urls import path, include
from . import views
urlpatterns = [
    path(r'', views.index, name='index'),
    path(r'grey/', views.grey, name='grey'),
    path(r'edge/', views.edge, name='edge'),
	path(r'eyedetect/', views.eyedetect, name='eyedetect'),
    path(r'contact/', views.contact, name='contact'),
    path(r'details/', views.details, name='details'),
]
