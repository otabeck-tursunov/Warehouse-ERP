from django.urls import path
from .views import *

urlpatterns = [
    path('', StatistikaView.as_view(), name='statistika'),
    path('<int:pk>/tahrirlash/', SotuvEditView.as_view(), name='sotuv-edit'),
    path('<int:pk>/o\'chirish/', SotuvDeleteView.as_view(), name='sotuv-delete'),
]
