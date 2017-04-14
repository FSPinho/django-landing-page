from django.conf.urls import url, include
from django.conf.urls.static import static
from django.conf import settings
from django.contrib import admin
from api import urls as apiUrls
from . import views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^api/', include(apiUrls)),
    url(r'^landing/', views.WebsiteAppView.as_view())
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
