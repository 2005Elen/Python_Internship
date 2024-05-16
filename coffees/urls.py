from django.urls import path

from coffees import views

urlpatterns = [
    path('', views.home,),
]