from django.urls import path, include
from django.contrib import admin
import hello.views as hello_views
admin.autodiscover()

# To add a new path, first import the app:
# import blog
#
# Then add the new path:
# path('blog/', blog.urls, name="blog")
#
# Learn more here: https://docs.djangoproject.com/en/2.1/topics/http/urls/

urlpatterns = [
    path("", hello_views.index),
    path("admin/", admin.site.urls),
    path('subscribe/', hello_views.subscribe, name='subscribe'),
    
]
