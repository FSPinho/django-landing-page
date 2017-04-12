# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.test import TestCase
from api.models import PageLink, Page

class PageLinkTest(TestCase):
    def setUp(self):
        page = Page.objects.create()
        PageLink.objects.create(name='home', apperance='text', page=page)
        PageLink.objects.create(name='google', apperance='button', page=page)
    
    def testPageLinkAreCreated(self):
        pl1 = PageLink.objects.get(name='home')
        pl2 = PageLink.objects.get(name='google')

        self.assertEqual(pl1.apperance, 'text')
        self.assertEqual(pl2.apperance, 'button')