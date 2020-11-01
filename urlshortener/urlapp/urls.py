from . import views
from django.urls import path

urlpatterns = [
    
    path('', views.index,name='index'),
    path('<str:id>', views.shorten,name='shorten'),
]