from django.contrib import admin
from django.urls import path, include
from userApp.views import LoginView

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', LoginView.as_view(), name='login'),
    path('', include('mainApp.urls')),
    path('user/', include('userApp.urls')),
    path('statistika/', include('statsApp.urls')),
]
# + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
