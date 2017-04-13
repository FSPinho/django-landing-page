from django.conf.urls import url, include
from rest_framework import routers

from api.views import PageViewSet, ToolbarViewSet, PageLinkViewSet, SocialLinkViewSet, ToolbarLinkViewSet

router = routers.DefaultRouter()
router.register(r'page', PageViewSet)
router.register(r'toolbar', ToolbarViewSet)
router.register(r'page-link', PageLinkViewSet)
router.register(r'social-link', SocialLinkViewSet)
router.register(r'toolbar-link', ToolbarLinkViewSet)

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    url(r'^', include(router.urls))
]