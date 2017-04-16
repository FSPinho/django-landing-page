# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from rest_framework import viewsets

from api.models import Page, Toolbar, SocialLink, ToolbarLink, PageLink, Section
from api.serializers import PageSerializer, ToolbarSerializer, SocialLinkSerializer, ToolbarLinkSerializer, \
    PageLinkSerializer, SectionSerializer


class PageViewSet(viewsets.ModelViewSet):
    queryset = Page.objects.all()
    serializer_class = PageSerializer


class ToolbarViewSet(viewsets.ModelViewSet):
    queryset = Toolbar.objects.all()
    serializer_class = ToolbarSerializer


class PageLinkViewSet(viewsets.ModelViewSet):
    queryset = PageLink.objects.all()
    serializer_class = PageLinkSerializer


class SocialLinkViewSet(viewsets.ModelViewSet):
    queryset = SocialLink.objects.all()
    serializer_class = SocialLinkSerializer


class ToolbarLinkViewSet(viewsets.ModelViewSet):
    queryset = ToolbarLink.objects.all()
    serializer_class = ToolbarLinkSerializer


class SectionViewSet(viewsets.ModelViewSet):
    queryset = Section.objects.all()
    serializer_class = SectionSerializer
