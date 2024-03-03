from django.urls import path
from .views import *

urlpatterns = [
    path('logout/', LogoutView.as_view(), name='logout')
]
