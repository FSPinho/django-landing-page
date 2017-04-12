# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.test import TestCase
from api.models import PageLink, SocialLink, Page

class PageLinkTest(TestCase):
    def setUp(self):
        page = Page.objects.create(name='home')
        PageLink.objects.create(apperance='text', page=page)
        PageLink.objects.create(apperance='button', page=page)
    
    def testPageLinkCreatedSuccessfully(self):
        pl1 = PageLink.objects.get(apperance='text')
        pl2 = PageLink.objects.get(apperance='button')

        self.assertEqual(pl1.page.name, 'home')
        self.assertEqual(pl2.page.name, 'home')


class SocialLinkTest(TestCase):
    def setUp(self):
        SocialLink.objects.create(name='facebook', url='https://www.facebook.com', apperance='text')
        SocialLink.objects.create(name='twitter', url='https://www.twitter.com', apperance='button')
    
    def testSocialLinkCreatedSuccessfully(self):
        sl1 = SocialLink.objects.get(name='facebook')
        sl2 = SocialLink.objects.get(name='twitter')

        self.assertEqual(sl1.url, 'https://www.facebook.com')
        self.assertEqual(sl1.apperance, 'text')
        self.assertEqual(sl2.url, 'https://www.twitter.com')
        self.assertEqual(sl2.apperance, 'button')