from django.conf.urls import url, include
from rest_framework import routers

from api.views import PageViewSet,  SocialLinkViewSet

router = routers.DefaultRouter()
router.register(r'page', PageViewSet)
router.register(r'social-link', SocialLinkViewSet)

urlpatterns = [
    url(r'^', include(router.urls))
]