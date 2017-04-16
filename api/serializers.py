from rest_framework import serializers

from api.models import Page, Toolbar, PageLink, SocialLink, ToolbarLink, Section, ColorPrimary


class SimplePageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Page
        fields = ('id', 'name', 'shortName', 'path', 'mainPage', 'order')

class PageLinkSerializer(serializers.ModelSerializer):
    page = SimplePageSerializer()
    class Meta:
        model = PageLink
        fields = ('id', 'icon', 'appearance', 'openNewTab', 'page')
        depth = 1


class SocialLinkSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = SocialLink
        fields = '__all__'


class ToolbarLinkSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = ToolbarLink
        exclude = ('id', 'toolbar', )


class ToolbarSerializer(serializers.ModelSerializer):
    links = ToolbarLinkSerializer(many=True, read_only=True)

    class Meta:
        model = Toolbar
        fields = ('id', 'name', 'showPageName', 'icon', 'links')


class ColorSerializer(serializers.ModelSerializer):
    class Meta:
        model = ColorPrimary
        fields = '__all__'


class SectionSerializer(serializers.ModelSerializer):
    page = SimplePageSerializer
    backgroundColor = ColorSerializer()
    class Meta:
        model = Section
        fields = ('id', 'name', 'order', 'fullHeight', 'backgroundColor',
                  'backgroundImageSmall', 'backgroundImageMedium', 'backgroundImageLarge', 'backgroundImageXLarge')


class PageSerializer(serializers.ModelSerializer):
    toolbar = ToolbarSerializer()
    sections = SectionSerializer(many=True)
    class Meta:
        model = Page
        fields = ('id', 'name', 'shortName', 'alias', 'path', 'toolbar', 'mainPage', 'sections')


