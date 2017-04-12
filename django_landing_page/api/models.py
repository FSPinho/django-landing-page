# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from imagekit.models import ImageSpecField
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

DEFAULT_TEXT_INPUT_MAX_LENGTH = 255
DEFAULT_TEXT_AREA_INPUT_MAX_LENGTH = 1024 * 1024

LINK_APERRANCE_TYPES = (
    ('text', 'Just text'),
    ('button', 'Like a button'),
)
DEFAULT_LINK_APERRANCE_TYPE = 'text'

# ----------- END - CONSTANTS ------------ #


# ----------- MODEL CLASSES ------------ #

class Page(models.Model):
    pass


class Link(models.Model):
    name = models.CharField(max_length=255, default='', null=False)
    icon = ProcessedImageField(upload_to=DEFAULT_ICON_UPLOAD_FOLDER,
                                processors=[ResizeToFill(192, 192)],
                                format=DEFAULT_ICON_FORMAT,
                                options={'quality': DEFAULT_ICON_QUALITY})
    
    apperance = CharField(max_length=DEFAULT_TEXT_INPUT_MAX_LENGTH, 
                            choices=LINK_APERRANCE_TYPES, 
                            default=DEFAULT_LINK_APERRANCE_TYPE)

    class Meta:
        abstract = True


    def __unicode__(self):
        return '' % self.name


class PageLink(Link):
    page = models.ForeignKey(Page)

    class Meta:
        verbose_name = 'Page Link'
        verbose_name_plural = 'Page Links'


# ----------- END - MODEL CLASSES ------------ #