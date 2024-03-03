from django.urls import path
from .views import *

urlpatterns = [
    path('bolimlar/', BolimlarView.as_view(), name='bolimlar'),
    path('mahsulotlar/', MahsulotlarView.as_view(), name='mahsulotlar'),
    path('mahsulotlar/<int:pk>/tahrirlash/', MahsulotEditView.as_view(), name='mahsulot-edit'),
    path('mahsulotlar/<int:pk>/o\'chirish/', MahsulotDeleteView.as_view(), name='mahsulot-delete'),
    path('mijozlar/', MijozlarView.as_view(), name='mijozlar'),
    path('mijozlar/<int:pk>/tahrirlash/', MijozEditView.as_view(), name='mijoz-edit'),
    path('mijozlar/<int:pk>/o\'chirish/', MijozDeleteView.as_view(), name='mijoz-delete'),
]
