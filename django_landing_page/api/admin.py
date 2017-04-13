# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from api.models import PageLink, SocialLink, ToolbarLink, Toolbar, Page

# Register your models here.

class PageAdmin(admin.ModelAdmin):
    prepopulated_fields = {"alias": ("name",)}

admin.site.register(PageLink)
admin.site.register(SocialLink)
admin.site.register(ToolbarLink)
admin.site.register(Toolbar)
admin.site.register(Page, PageAdmin)