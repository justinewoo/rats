from django.urls import path
from . import views

urlpatterns = [
    path('', views.rat, name='home'),
]