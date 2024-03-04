from django.shortcuts import render, redirect
from django.views import View
from .models import *


class BolimlarView(View):
    def get(self, request):
        if request.user.is_authenticated:
            return render(request, "bo'limlar.html")
        return redirect('login')


class MahsulotlarView(View):
    def get(self, request):
        if request.user.is_authenticated:
            mahsulotlar = Mahsulot.objects.filter(tarqatuvchi=request.user).order_by('kelgan_sana')
            if request.GET.get('search'):
                mahsulotlar = mahsulotlar.filter(nom__icontains=request.GET.get('search')) | mahsulotlar.filter(
                    brend__icontains=request.GET.get('search'))
            context = {
                'mahsulotlar': mahsulotlar,
                'user': request.user
            }
            return render(request, 'mahsulotlar.html', context)
        else:
            return redirect('login')

    def post(self, request):
        if request.user.is_authenticated:
            Mahsulot.objects.create(
                nom=request.POST.get('nom'),
                brend=request.POST.get('brend'),
                narx=request.POST.get('narx'),
                miqdor=request.POST.get('miqdor'),
                olchov=request.POST.get('olchov'),
                kelgan_sana=request.POST.get('kelgan_sana'),
                tarqatuvchi=request.user,
            )
            return redirect('mahsulotlar')
        return redirect('login')


class MahsulotEditView(View):
    def get(self, request, pk):
        if request.user.is_authenticated:
            mahsulot = Mahsulot.objects.get(id=pk)
            context = {
                'mahsulot': mahsulot
            }
            return render(request, 'mahsulot-tahrirlash.html', context)
        return redirect('login')

    def post(self, request, pk):
        if request.user.is_authenticated:
            mahsulot = Mahsulot.objects.get(id=pk)
            mahsulot.nom = request.POST.get('nom')
            mahsulot.brend = request.POST.get('brend')
            mahsulot.narx = request.POST.get('narx')
            mahsulot.miqdor = request.POST.get('miqdor')
            mahsulot.save()
            return redirect('mahsulotlar')
        return redirect('login')


class MijozlarView(View):
    def get(self, request):
        if request.user.is_authenticated:
            mijozlar = Mijoz.objects.all().order_by('-id')
            if request.GET.get('search'):
                mijozlar = (
                        mijozlar.filter(ism__icontains=request.GET.get('search')) |
                        mijozlar.filter(dokon__icontains=request.GET.get('search')) |
                        mijozlar.filter(manzil__icontains=request.GET.get('search'))
                )
            context = {
                'mijozlar': mijozlar,
                'user': request.user
            }
            return render(request, 'mijozlar.html', context)
        else:
            return redirect('login')

    def post(self, request):
        if request.user.is_authenticated:
            Mijoz.objects.create(
                ism=request.POST.get('ism'),
                dokon=request.POST.get('dokon'),
                tel=request.POST.get('tel'),
                manzil=request.POST.get('manzil'),
                qarz=request.POST.get('qarz'),
                tarqatuvchi=request.user
            )
            return redirect('mijozlar')
        return redirect('login')


class MijozEditView(View):
    def get(self, request, pk):
        if request.user.is_authenticated:
            mijoz = Mijoz.objects.get(pk=pk)
            context = {
                'mijoz': mijoz
            }
            return render(request, 'mijoz-tahrirlash.html', context)
        return redirect('login')

    def post(self, request, pk):
        if request.user.is_authenticated:
            mijoz = Mijoz.objects.get(pk=pk)
            mijoz.ism = request.POST.get('ism')
            mijoz.dokon = request.POST.get('dokon')
            mijoz.tel = request.POST.get('tel')
            mijoz.manzil = request.POST.get('manzil')
            mijoz.qarz = request.POST.get('qarz')
            mijoz.save()
            return redirect('mijozlar')
        return redirect('login')


class MahsulotDeleteView(View):
    def get(self, request, pk):
        if request.user.is_authenticated:
            Mahsulot.objects.get(id=pk).delete()
            return redirect('mahsulotlar')
        return redirect('login')


class MijozDeleteView(View):
    def get(self, request, pk):
        if request.user.is_authenticated:
            Mijoz.objects.get(id=pk).delete()
            return redirect('mijozlar')
        return redirect('login')
