from django.test import TestCase
import django
# Create your tests here.
class ViewTest(TestCase):
    if django.VERSION[:2] >=(1,7):
        @classmethod
        def setUpClass(cls):
            super(ViewTest,cls).setUpClass()
            django.setup()
    
    def test_home(self):
        """Tests the home page"""
        response=self.client.get('/')
        self.assertContains(response,'Home Page',1,200)
    
    def test_contact(self):
        """Tests the contact page"""
        response = self.client.get('/contact')
        self.assertContains(response,'Contact',3,200)
    
    def test_about(self):
        """Tests the about page"""
        response=self.client.get('/about')
        self.assertContains(response,'About',3,200)
