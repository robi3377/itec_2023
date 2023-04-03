from django.urls import path
from django import views
from . import views

urlpatterns = [

    path('0', views.completionApi ),
    path('2', views.mirrorApi),
    path('1', views.themeApi)

]