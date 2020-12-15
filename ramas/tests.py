from django.test import TestCase
from ramas.models import Ramal

# Create your tests here.

class RamalTestCase(TestCase):
    def setUp(self):
        Ramal.objects.create(nombre="Seguridad")
        Ramal.objects.create(nombre="Almacenamiento")
        Ramal.objects.create(nombre="Iluminacion")
        