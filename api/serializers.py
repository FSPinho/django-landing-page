from rest_framework import serializers

from api.models import Page, Toolbar, PageLink, SocialLink, ToolbarLink


class PageSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Page
        fields = '__all__'


class ToolbarSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Toolbar
        fields = '__all__'


class PageLinkSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = PageLink
        fields = '__all__'


class SocialLinkSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = SocialLink
        fields = '__all__'


class ToolbarLinkSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = ToolbarLink
        fields = '__all__'