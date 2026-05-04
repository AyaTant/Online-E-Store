from django.test import TestCase
import django
# Create your tests here.

class SimpleTest(TestCase):
    """Tests for the application views"""
    #django requires and explicit setup() when running tests in PTVS
    @classmethod
    def setUpClass(cls):
        super(SimpleTest,cls).setUpClass()
        django.setup()
    
    def test_basic_addition(self):
        self.assertEqual(1+1,2)