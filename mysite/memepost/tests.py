""" The files serves to test everything within the memepost app. """

from django.test import TestCase
from memepost.models import memepost, memepostForm
import logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

class memepostTestCase(TestCase):
    def setUp(self):
        memepost.objects.create(title="foo", 
            model_pic="/site_media/media/pic_folder/casual_headshot.jpg", 
            date="2017-06-14")
        memepost.objects.create(title="bar", 
            date="2017-06-14")
            
    def test_memepost_enters_database(self):
        foo = memepost.objects.get("foo")
        bar = memepost.objects.get("bar")
        self.assertEqual(foo.date, "6/15/17")
        logger.debug("foo date is equal to %s", foo.date)
        self.assertEqual(bar.model_pic, "no-img.jpg")
        logger.debug("bar is equal to %s", bar.model_pic)