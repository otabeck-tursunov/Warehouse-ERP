from django.db.models import Q
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.views import View

from mainApp.models import Mahsulot, Mijoz
from .models import Sotuv


class StatistikaView(View):
    def get(self, request):
        if request.user.is_authenticated:
            sotuvlar = Sotuv.objects.filter(tarqatuvchi=request.user).order_by('-sana')
            if request.GET.get('search'):
                sotuvlar = sotuvlar.filter(
                    Q(mahsulot__nom__icontains=request.GET.get('search')) |
                    Q(mahsulot__brend__icontains=request.GET.get('search')) |
                    Q(mijoz__ism__icontains=request.GET.get('search')) |
                    Q(mijoz__dokon__icontains=request.GET.get('search'))
                )
            mahsulotlar = Mahsulot.objects.filter(tarqatuvchi=request.user)
            mijozlar = Mijoz.objects.filter(tarqatuvchi=request.user)
            summa = sum(sotuvlar.values_list('summa', flat=True))
            qarz = sum(sotuvlar.values_list('qarz', flat=True))
            context = {
                'sotuvlar': sotuvlar,
                'mahsulotlar': mahsulotlar,
                'mijozlar': mijozlar,
                'user': request.user,
                'summa': int(summa),
                'qarz': int(qarz)
            }
            return render(request, 'statistikalar.html', context)
        return redirect('login')

    def post(self, request):
        if request.user.is_authenticated:
            mahsulot = Mahsulot.objects.get(id=request.POST.get('mahsulot'))
            mijoz = Mijoz.objects.get(id=request.POST.get('mijoz'))
            if float(request.POST['miqdor']) > Mahsulot.objects.get(id=request.POST['mahsulot']).miqdor:
                return HttpResponse(
                    f"""
                    Ushbu mahsulot {mahsulot.miqdor} {mahsulot.olchov} mavjud! \n
                    <a href="/statistika/">Ortga</a>
                    """
                )
            if float(request.POST['summa']) != float(request.POST['tolandi']) + float(request.POST['qarz']):
                return HttpResponse(
                    f"""
                    To'langan va qarz miqdorlari umumiy summaga mutanosib emas! \n
                    <a href="/statistika/">Ortga</a>
                    """, status=400
                )
            Sotuv.objects.create(
                mahsulot=Mahsulot.objects.get(id=request.POST['mahsulot']),
                mijoz=Mijoz.objects.get(id=request.POST['mijoz']),
                miqdor=request.POST['miqdor'],
                summa=request.POST['summa'],
                tolandi=request.POST['tolandi'],
                qarz=request.POST['qarz'],
                sana=request.POST['sana'],
                tarqatuvchi=request.user
            )
            mahsulot.miqdor = mahsulot.miqdor - float(request.POST['miqdor'])
            mahsulot.save()
            mijoz.qarz = mijoz.qarz + float(request.POST['qarz'])
            mijoz.save()
            return redirect('statistika')
        return redirect('login')


class SotuvEditView(View):
    def get(self, request, pk):
        if request.user.is_authenticated:
            sotuv = Sotuv.objects.get(id=pk)
            mahsulotlar = Mahsulot.objects.filter(tarqatuvchi=request.user)
            mijozlar = Mijoz.objects.filter(tarqatuvchi=request.user)
            context = {
                'sotuv': sotuv,
                'mahsulotlar': mahsulotlar,
                'mijozlar': mijozlar,

            }
            return render(request, 'sotuv-tahrirlash.html', context)
        return redirect('login')

    def post(self, request, pk):
        if request.user.is_authenticated:
            sotuv = Sotuv.objects.get(id=pk)
            mijoz = Mijoz.objects.get(id=sotuv.mijoz.id)
            if float(request.POST['summa']) != float(request.POST['tolandi']) + float(request.POST['qarz']):
                return HttpResponse(
                    f"""
                    To'langan va qarz miqdorlari umumiy summaga mutanosib emas! \n
                    <a href="/statistika/{pk}/tahrirlash/">Ortga</a>
                    """
                )
            sotuv.mahsulot = Mahsulot.objects.get(id=request.POST['mahsulot'])
            sotuv.mijoz = Mijoz.objects.get(id=request.POST['mijoz'])
            sotuv.miqdor = request.POST['miqdor']
            sotuv.summa = request.POST['summa']
            sotuv.tolandi = request.POST['tolandi']
            sotuv.qarz = request.POST['qarz']
            sotuv.sana = request.POST['sana']
            sotuv.save()
            mijoz.qarz = sum(Sotuv.objects.filter(mijoz=mijoz).values_list('qarz', flat=True))
            mijoz.save()
            return redirect('statistika')
        return redirect('login')


class SotuvDeleteView(View):
    def get(self, request, pk):
        if request.user.is_authenticated:
            sotuv = Sotuv.objects.get(id=pk)
            mijoz = Mijoz.objects.get(id=sotuv.mijoz.id)
            sotuv.delete()
            mijoz.qarz = sum(Sotuv.objects.filter(mijoz=mijoz).values_list('qarz', flat=True))
            mijoz.save()
            return redirect('statistika')
        return redirect('login')
