from django.urls import path
from . import views

urlpatterns = [
    path('', views.rat, name='home'),
    path('chooseMode/', views.mode, name='mode'),
    path(r'^selection/$', views.selection, name='selection'),
]