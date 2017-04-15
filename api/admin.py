# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from api.models import PageLink, SocialLink, ToolbarLink, Toolbar, Page

# Register your models here.

class PageAdmin(admin.ModelAdmin):
    list_display = ('name', 'shortName', 'alias', 'path', 'mainPage', 'order')
    prepopulated_fields = {"alias": ("name",)}
    ordering = ('-mainPage', 'order', 'name')

class ToolbarAdmin(admin.ModelAdmin):
    list_display = ('name', 'showPageName',)

# admin.site.register(PageLink)
admin.site.register(SocialLink)
admin.site.register(ToolbarLink)
admin.site.register(Toolbar, ToolbarAdmin)
admin.site.register(Page, PageAdmin)