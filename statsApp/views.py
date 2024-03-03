from django.shortcuts import render, redirect
from django.views import View

from mainApp.models import Mahsulot, Mijoz
from .models import Sotuv


class SotuvlarView(View):
    def get(self, request):
        if request.user.is_authenticated:
            sotuvlar = Sotuv.objects.filter(tarqatuvchi=request.user)
            mahsulotlar = Mahsulot.objects.filter(tarqatuvchi=request.user)
            mijozlar = Mijoz.objects.filter(tarqatuvchi=request.user)
            context = {
                'sotuvlar': sotuvlar,
                'mahsulotlar': mahsulotlar,
                'mijozlar': mijozlar,
                'user': request.user
            }
            return render(request, 'statistikalar.html', context)
        return redirect('login')

    def post(self, request):
        if request.user.is_authenticated:
            Sotuv.objects.create(
                mahsulot=Mahsulot.objects.get(id=request.POST['mahsulot']),
                miqdor=request.POST['miqdor'],
                mijoz=request.POST['mijoz'],
                summa=request.POST['summa'],
                tolandi=request.POST['tolandi'],
            )
