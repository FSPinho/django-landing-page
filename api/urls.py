from django.conf.urls import url, include
from rest_framework import routers

from api.views import PageViewSet, ToolbarViewSet, PageLinkViewSet, SocialLinkViewSet, ToolbarLinkViewSet

router = routers.DefaultRouter()
router.register(r'page', PageViewSet)
router.register(r'page-link', PageLinkViewSet)
router.register(r'social-link', SocialLinkViewSet)

urlpatterns = [
    url(r'^', include(router.urls))
]