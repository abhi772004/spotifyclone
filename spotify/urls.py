from django.urls import path
from .views import *
app_name='spotify'

urlpatterns=[
    path('',home.as_view(), name='home'),
   
]


