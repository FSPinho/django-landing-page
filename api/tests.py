# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.test import TestCase
from api.models import PageLink, SocialLink, Page, Toolbar, ToolbarLink

class SocialLinkTest(TestCase):
    def setUp(self):
        SocialLink.objects.create(name='facebook', url='https://www.facebook.com', appearance='text')
        SocialLink.objects.create(name='twitter', url='https://www.twitter.com', appearance='button')

    def testSocialLinkCreatedSuccessfully(self):
        sl1 = SocialLink.objects.get(name='facebook')
        sl2 = SocialLink.objects.get(name='twitter')

        self.assertEqual(sl1.url, 'https://www.facebook.com')
        self.assertEqual(sl1.appearance, 'text')
        self.assertEqual(sl2.url, 'https://www.twitter.com')
        self.assertEqual(sl2.appearance, 'button')


class ToolbarLinkTest(TestCase):
    def setUp(self):
        toolbar = Toolbar.objects.create(name='Main toolbar', showPageName=True)
        tl1 = ToolbarLink.objects.create(name='Google home page', shortName='Google', url='www.google.com')
        tl2 = ToolbarLink.objects.create(name='Facebook home page', shortName='Facebook', url='www.facebook.com')
        tl1.toolbar = [toolbar, ]
        tl2.toolbar = [toolbar, ]
        tl1.save()
        tl2.save()

    def testToolbarLinkCreatedSuccessfully(self):
        tl1 = ToolbarLink.objects.get(shortName='Google')
        tl2 = ToolbarLink.objects.get(shortName='Facebook')

        self.assertEqual(tl1.name, 'Google home page')
        self.assertEqual(tl2.name, 'Facebook home page')


class ToolbarTest(TestCase):
    def setUp(self):
        Toolbar.objects.create(name='Secondary Toolbar', showPageName=True)

    def testToolbarCreatedSuccessfully(self):
        toolbar = Toolbar.objects.get(name='Secondary Toolbar')

        self.assertEqual(toolbar.showPageName, True)


class PageTest(TestCase):
    def setUp(self):
        Page.objects.create(name='Home page', shortName='Home', alias='home page')

    def testPageCreatedSuccessfully(self):
        page = Page.objects.get(name='Home page')


