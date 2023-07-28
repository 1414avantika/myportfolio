
from django.contrib import admin
from django.urls import path
from . import views
urlpatterns = [
    path( 'admin/', admin.site.urls ),
    path( '', views.use,name='use' ),
    path('about', views.test),
    path('contact',views.cat),
    path('resume', views.dog),
    path('portfolio', views.holl),
    path('services', views.moll),
    path('home', views.fall)


]
