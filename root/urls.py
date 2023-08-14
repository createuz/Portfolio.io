from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static

from root import settings
from root.settings import STATIC_ROOT, STATIC_URL

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('user.urls')),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
