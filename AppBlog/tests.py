from datetime import datetime
from django.test import TestCase
from AppBlog.models import Articulo


class ViewTestCase(TestCase):

    def test_crear_articulo(self):
        Articulo.objects.create(titulo="Ovni en el campo", autor="Juan Cruz")
        todos_los_articulos = Articulo.objects.all()
        assert len(todos_los_articulos) == 1
        assert todos_los_articulos[0].nombre == "test 1234"


    def test_crear_articulo_sin_foto(self):
        Articulo.objects.create(titulo="Ovni en el campo", autor="Juan Cruz")
        todos_los_articulos = Articulo.objects.all()
        assert todos_los_articulos[0].imagen is None


    def test_crear_4_articulos(self):
        Articulo.objects.create(titulo="Ovni en el campo", autor="Juan Cruz")
        Articulo.objects.create(titulo="Ovni en el campo", autor="Juan Cruz")
        Articulo.objects.create(titulo="Ovni en el campo", autor="Juan Cruz")
        Articulo.objects.create(titulo="Ovni en el campo", autor="Juan Cruz")
        Articulo.objects.create(titulo="Ovni en el campo", autor="Juan Cruz")
        todos_los_cursos = Articulo.objects.all()
        assert len(todos_los_cursos) == 4