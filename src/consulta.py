from producto import Producto


def consultar_producto(productos, codigo):
    """Devuelve el producto con el código indicado, o None si no existe."""
    for p in productos:
        if p.codigo == codigo:
            return p
    return None


if __name__ == "__main__":
    inventario = [Producto("P001", "Teclado USB", 349.90, 25)]
    encontrado = consultar_producto(inventario, "P001")
    if encontrado:
        encontrado.mostrar_informacion()
    else:
        print("Producto no encontrado")
