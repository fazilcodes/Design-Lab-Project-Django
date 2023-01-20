from django.contrib import admin
from django.contrib.staticfiles.urls import static, staticfiles_urlpatterns
from django.urls import path, include
from . import settings
import Home.urls
import Admin.urls
import Employee.urls




urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(Home.urls)),
    path('', include(Admin.urls)),
    path('', include(Employee.urls))
]


urlpatterns += staticfiles_urlpatterns()
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
