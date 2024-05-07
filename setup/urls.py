from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.views.generic import RedirectView
from django.conf import settings

urlpatterns = [
    path('', RedirectView.as_view(url='galeria/')),
    path('admin-space/', admin.site.urls),
    path('galeria/', include('apps.galeria.urls')),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

