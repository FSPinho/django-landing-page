# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from imagekit.models import ProcessedImageField
from imagekit.processors import ResizeToFill
from os.path import join

# ----------- CONSTANTS ------------ #

DEFAULT_UPLOAD_FOLDER = 'uploads'
DEFAULT_IMAGE_UPLOAD_FOLDER = join(DEFAULT_UPLOAD_FOLDER, 'images')
DEFAULT_ICON_UPLOAD_FOLDER = join(DEFAULT_UPLOAD_FOLDER, 'icons')

DEFAULT_IMAGE_FORMAT = 'PNG'
DEFAULT_ICON_FORMAT = 'PNG'
DEFAULT_IMAGE_QUALITY = 60
DEFAULT_ICON_QUALITY = 60
DEFAULT_ICON_SIZE = 192

DEFAULT_TEXT_INPUT_MAX_LENGTH = 255
DEFAULT_TEXT_AREA_INPUT_MAX_LENGTH = 1024 * 1024
DEFAULT_PAGE_NAME_LENGTH = 32
DEFAULT_PAGE_SHORT_NAME_LENGTH = 16
DEFAULT_LINK_NAME_LENGTH = 32
DEFAULT_LINK_SHORT_NAME_LENGTH = 16

LINK_APERRANCE_TYPES = (
    ('text', 'Just text'),
    ('button', 'Like a button'),
)
DEFAULT_LINK_APERRANCE_TYPE = 'text'

DEVICE_TYPES = (
    ('small', 'Phones'),
    ('medium', 'Tablets and some phones in landscape'),
    ('large', 'HD Desktops'),
    ('xlarge', 'FullHD desktops'),
)


# ----------- END - CONSTANTS ------------ #


# ----------- MODEL CLASSES ------------ #

class Toolbar(models.Model):
    name = models.CharField(max_length=DEFAULT_TEXT_INPUT_MAX_LENGTH,
                            default=None,
                            null=True,
                            blank=True,
                            help_text='Only visible to you. Use it to manage yours toolbars')
    showPageName = models.BooleanField(default=True)
    icon = ProcessedImageField(null=True, default=None,
                               help_text='The icon should be a square image',
                               upload_to=DEFAULT_ICON_UPLOAD_FOLDER,
                               processors=[ResizeToFill(DEFAULT_ICON_SIZE, DEFAULT_ICON_SIZE)],
                               format=DEFAULT_ICON_FORMAT,
                               options={'quality': DEFAULT_ICON_QUALITY})

    class Meta:
        verbose_name = 'Toolbar'
        verbose_name_plural = 'Toolbars'

    def __unicode__(self):
        return self.name


class Page(models.Model):
    name = models.CharField(max_length=DEFAULT_PAGE_NAME_LENGTH,
                            default=None,
                            null=False,
                            unique=True,
                            blank=False)
    shortName = models.CharField(max_length=DEFAULT_PAGE_SHORT_NAME_LENGTH,
                                 default=None,
                                 null=True,
                                 help_text='Short version of the page name',
                                 blank=True)
    alias = models.SlugField(max_length=DEFAULT_PAGE_NAME_LENGTH,
                             default=None,
                             null=False,
                             unique=True,
                             help_text='Will be used as the page URL',
                             blank=False)
    toolbar = models.ForeignKey(Toolbar, null=True, blank=True)

    class Meta:
        verbose_name = 'Page'
        verbose_name_plural = 'Pages'

    def __unicode__(self):
        return self.name


class Link(models.Model):
    icon = ProcessedImageField(null=True, default=None,
                               upload_to=DEFAULT_ICON_UPLOAD_FOLDER,
                               processors=[ResizeToFill(DEFAULT_ICON_SIZE, DEFAULT_ICON_SIZE)],
                               format=DEFAULT_ICON_FORMAT,
                               options={'quality': DEFAULT_ICON_QUALITY})
    appearance = models.CharField(max_length=DEFAULT_TEXT_INPUT_MAX_LENGTH,
                                  choices=LINK_APERRANCE_TYPES,
                                  default=DEFAULT_LINK_APERRANCE_TYPE,
                                  null=False)
    openNewTab = models.BooleanField(default=True, verbose_name='Open this link in a new tab?')

    class Meta:
        abstract = True


class PageLink(Link):
    page = models.ForeignKey(Page)

    class Meta:
        verbose_name = 'Page Link'
        verbose_name_plural = 'Page Links'

    def __unicode__(self):
        return 'Link to %s page' % self.page


class SocialLink(Link):
    name = models.CharField(max_length=DEFAULT_TEXT_INPUT_MAX_LENGTH, default='', null=False)
    url = models.URLField()

    class Meta:
        verbose_name = 'Social Link'
        verbose_name_plural = 'Social Links'

    def __unicode__(self):
        return 'Social link to %s at %s' % (self.name, self.url)


class ToolbarLink(Link):
    toolbar = models.ManyToManyField(Toolbar, related_name='links')
    name = models.CharField(max_length=DEFAULT_LINK_NAME_LENGTH, default='', null=False)
    shortName = models.CharField(max_length=DEFAULT_LINK_SHORT_NAME_LENGTH, default='', null=True,
                                 help_text='Short version of the name')
    url = models.URLField()

    class Meta:
        verbose_name = 'Toolbar Link'
        verbose_name_plural = 'Toolbar Links'