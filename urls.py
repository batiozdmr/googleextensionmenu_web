from django.conf import settings
from django.conf.urls.static import static

from django.contrib import admin

admin.site.site_header = 'Core Yönetimi'
admin.site.index_title = 'Core Yönetimi'
admin.site.site_title = 'Core Yönetim Paneli'

from django.urls import include
from django.contrib import admin
from django.urls import path

from django.conf.urls.i18n import i18n_patterns
from apps.mainpage.views import *

urlpatterns = i18n_patterns(
    path('super/user/admin/', admin.site.urls),
    path('', include(('apps.mainpage.urls'), namespace='mainpage')),
    path('accounts/', include("allauth.urls")),
    path('files/', include(('apps.files.urls'), namespace='files')),
    path('api/', include(('apps.api.urls'), namespace='api')),


    path('parameter/', include("apps.parameter.urls")),
    path('rosetta/lang/trans/', include('rosetta.urls')),
    path('ckeditor-secret/', include('ckeditor_uploader.urls')),

)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
