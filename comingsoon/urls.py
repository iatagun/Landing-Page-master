from django.urls import path
from . import views

app_name = 'comingsoon'

urlpatterns = [
    path('', views.home, name='home'),
    path("team19/", views.team19, name="team19"),
    path("team20/", views.team20, name="team20"),
    path("team21/", views.team21, name="team21"),


]


