import unittest
from base import BaseTestCase

from app.models import AsciiArt

class TestFrontPage(BaseTestCase):

	def test_front(self):
		response = self.client.get('/',content_type='html/text')
		self.assertEqual(response.status_code, 200)