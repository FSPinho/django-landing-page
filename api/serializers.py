from rest_framework import serializers

from api.models import Page, Toolbar, PageLink, SocialLink, ToolbarLink


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
        exclude = ('toolbar', )


class ToolbarSerializer(serializers.ModelSerializer):
    links = ToolbarLinkSerializer(many=True, read_only=True)

    class Meta:
        model = Toolbar
        fields = ('name', 'showPageName', 'icon', 'links')


class PageSerializer(serializers.ModelSerializer):
    toolbar = ToolbarSerializer()
    class Meta:
        model = Page
        fields = ('name', 'shortName', 'alias', 'path', 'toolbar')
