from django.test import TestCase

class SmokeTest(TestCase):
	def Test_bad_maths(self):
		self.assertEqual(1+1, 3)
