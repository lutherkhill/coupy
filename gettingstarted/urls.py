from django.urls import path, include
from django.contrib import admin
import hello.views as hello_views
import photoStorage.views as photoStorage_views
admin.autodiscover()

# To add a new path, first import the app:
urlpatterns = [
    path("", hello_views.index),
    path("admin/", admin.site.urls),
    path('subscribe/', hello_views.subscribe, name='subscribe'),
    path('photo/<str:pk>/', photoStorage_views.viewPhoto, name='photo'),
    path('add/', photoStorage_views.addPhoto, name='add'),
    path('gallery/', photoStorage_views.gallery, name='gallery'),
    
]


