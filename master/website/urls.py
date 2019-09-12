from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

from .views import index

admin.site.site_header = "MasterCode"
admin.site.site_title = "MasterCode"
admin.site.index_title = "MasterCode Administration"

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index, name='index'),
    # path('accounts/', include('accounts.urls')),
    path('control/', include('control_panel.urls')),
    path('tutorials/', include('tutorials.urls')),
    path('newsletter/', include('newsletters.urls')),
]
if settings.DEBUG:
        urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
        urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
