from django.urls import path
from .views import *


urlpatterns = [
    path('', SotuvlarView.as_view(), name='sotuvlar'),
]