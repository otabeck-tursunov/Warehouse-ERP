from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import LoginView
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.views import View


class LoginView(View):
    def get(self, request):
        return render(request, 'login.html')

    def post(self, request):
        user = authenticate(
            username=request.POST['username'],
            password=request.POST['password']
        )
        if user is not None:
            if user.is_superuser:
                return HttpResponse("""
                <h3>Sayt egasi sifatida 'Tarqatuvchi'lar ma'lumotiga kira olmaysiz, faqat <a href='/admin/'>Admin Panel</a> orqali boshqara olasiz!</h3>
                <a href='/'>Login</a> sahifasiga qaytish.
                """, content_type='text/html')
            else:
                login(request, user)
                return redirect('bolimlar')
        return redirect('login')


class LogoutView(View):
    def get(self, request):
        logout(request)
        return redirect('login')
