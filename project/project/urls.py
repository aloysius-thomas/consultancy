from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include
from django.urls import path

from accounts.views import home
from services.views import about_us_view
from services.views import contact_us_view

urlpatterns = [
    path('database/', admin.site.urls),
    path('', home, name='home'),
    path('about', about_us_view, name='about'),
    path('contact', contact_us_view, name='contact'),
    path('auth/', include('accounts.urls')),
    path('services/', include('services.urls')),
    path('admin/', include('services.urls_admin')),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
