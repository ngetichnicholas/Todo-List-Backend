from django.urls import path
from .import views as api_views

urlpatterns = [ 
    path('',api_views.index,name="index"),
]