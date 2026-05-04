from django.test import TestCase
import django
# Create your tests here.
class SimpleTest(TestCase):
    @classmethod
    def setUpClass(cls):
        super(SimpleTest,cls).setUpClass()
        django.setup()
    
    def test_basic_addition(self):
        self.assertEqual(1+1,2)