from django.test import TestCase
import django
# Create your tests here.
class SimpleTest(TestCase):
    """Tests for the application views"""

    # Django requires an explicit setup() when running tests in PTVS
    @classmethod
    def setUpClass(cls):
        super(SimpleTest,cls).setUpClass()
        django.setup()
    
    def test_basic_addition(self):
        """tests that 1+1 always equals 2"""
        self.assertEqual(1+1,2)