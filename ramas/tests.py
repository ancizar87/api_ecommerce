from unittest.case import expectedFailure
from django.test import SimpleTestCase
from .views import views

# Create your tests here.

class TestViews(SimpleTestCase):
    def setUp(self):
        
        def test_get_ok(self):
            response = self.client.get('/')
            self.assertEqual(response.status_code, 200)