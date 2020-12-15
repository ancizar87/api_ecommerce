from django.test import TestCase
from ramas.models import Ramal

# Create your tests here.

class RamalTestCase(TestCase):
    def setUp(self):
        Ramal.objects.create(nombre="Seguridad")
        Ramal.objects.create(nombre="Almacenamiento")
        Ramal.objects.create(nombre="Iluminacion")
        
    def test_ramas_can_speak(self):
        Seguridad = Ramal.objects.get(name="Seguridad")
        Almacenamiento = Ramal.objects.get(name="Almacenamiento")
        Iluminacion = Ramal.objects.get(name="Iluminacion")
        self.assertEqual(Seguridad.speak(), 'camaras')
        self.assertEqual(Almacenamiento.speak(), 'discosduros')
        self.assertEqual(Iluminacion.speak(), 'luz led')