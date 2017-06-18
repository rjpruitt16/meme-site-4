""" The files serves to test everything within the memepost app. """

from django.test import TestCase
from memepost.models import memepost, memepostForm
from datetime import date, datetime
from django.db import models
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

class memepostTestCase(TestCase):
    def setUp(self):
        memepost.objects.create(title="foo", 
            model_pic="/site_media/media/pic_folder/casual_headshot.jpg", 
            date=datetime(2017, 05, 14, 5, 11))
        memepost.objects.create(title="bar", 
            date=datetime(2017,05, 13, 0, 0))
            
    def test_memepost_enters_database(self):
        foo = memepost.objects.get(title="foo")
        bar = memepost.objects.get(title="bar")
        self.assertEqual(foo.date.replace(tzinfo=None), datetime(2017, 05, 14, 5, 11))
        logger.debug("foo date is equal to %s", foo.date)
        self.assertEqual(bar.model_pic.name, "pic_folder/no-img.jpg")
        print type(bar.model_pic)
        logger.debug("bar is equal to %s", bar.model_pic)