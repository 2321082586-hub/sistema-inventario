"""Pruebas de la funcionalidad Producto (Fase TEST) con unittest."""
import io
import os
import sys
import unittest
from contextlib import redirect_stdout

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "src"))
from producto import Producto  # noqa: E402


def salida_de(producto):
    """Captura lo que imprime mostrar_informacion()."""
    buffer = io.StringIO()
    with redirect_stdout(buffer):
        producto.mostrar_informacion()
    return buffer.getvalue()


def linea(texto, etiqueta):
    """Devuelve la línea de la salida que empieza con la etiqueta indicada."""
    for renglon in texto.splitlines():
        if renglon.startswith(etiqueta):
            return renglon
    return ""


class TestProducto(unittest.TestCase):

    def setUp(self):
        self.producto = Producto("P001", "Teclado", 350, 10)
        self.salida = salida_de(self.producto)

    def test_cp01_crear_producto(self):
        """CP01 - Crear producto"""
        self.assertIsInstance(self.producto, Producto)
        self.assertEqual(
            (self.producto.codigo, self.producto.nombre,
             self.producto.precio, self.producto.existencia),
            ("P001", "Teclado", 350, 10))

    def test_cp02_mostrar_codigo(self):
        """CP02 - Mostrar código"""
        self.assertEqual(self.producto.codigo, "P001")
        self.assertIn("P001", linea(self.salida, "Código"))

    def test_cp03_mostrar_nombre(self):
        """CP03 - Mostrar nombre"""
        self.assertEqual(self.producto.nombre, "Teclado")
        self.assertIn("Teclado", linea(self.salida, "Nombre"))

    def test_cp04_mostrar_precio(self):
        """CP04 - Mostrar precio"""
        self.assertEqual(self.producto.precio, 350)
        self.assertIn("350.00", linea(self.salida, "Precio"))

    def test_cp05_mostrar_existencia(self):
        """CP05 - Mostrar existencia"""
        self.assertEqual(self.producto.existencia, 10)
        self.assertTrue(linea(self.salida, "Existencia").strip().endswith("10"))

    def test_cp06_mostrar_informacion_completa(self):
        """CP06 - Mostrar información completa"""
        for etiqueta, valor in [("Código", "P001"), ("Nombre", "Teclado"),
                                ("Precio", "350.00"), ("Existencia", "10")]:
            with self.subTest(dato=etiqueta):
                self.assertIn(valor, linea(self.salida, etiqueta))

    def test_cp07_crear_segundo_producto(self):
        """CP07 - Crear segundo producto"""
        segundo = Producto("P002", "Mouse", 180, 5)
        salida2 = salida_de(segundo)
        self.assertEqual((segundo.codigo, segundo.nombre, segundo.precio, segundo.existencia),
                         ("P002", "Mouse", 180, 5))
        self.assertIn("Mouse", linea(salida2, "Nombre"))
        self.assertNotIn("Teclado", salida2)
        # El primer producto no debe haber cambiado
        self.assertEqual(self.producto.nombre, "Teclado")


if __name__ == "__main__":
    unittest.main(verbosity=2)
