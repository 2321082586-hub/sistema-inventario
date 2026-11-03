from producto import Producto


def buscar_productos(productos, texto):
    """Devuelve los productos cuyo nombre o código contienen el texto buscado."""
    texto = texto.lower()
    return [p for p in productos
            if texto in p.nombre.lower() or texto in p.codigo.lower()]


if __name__ == "__main__":
    inventario = [
        Producto("P001", "Teclado USB", 349.90, 25),
        Producto("P002", "Mouse inalámbrico", 279.00, 40),
        Producto("P003", "Monitor 24 pulgadas", 2899.00, 8),
    ]
    for p in buscar_productos(inventario, "mouse"):
        p.mostrar_informacion()
