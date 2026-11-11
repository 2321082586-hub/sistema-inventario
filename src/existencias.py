from producto import Producto


def agregar_existencia(producto, cantidad):
    producto.existencia += cantidad


def retirar_existencia(producto, cantidad):
    if cantidad > producto.existencia:
        print("No hay suficiente existencia")
        return False
    producto.existencia -= cantidad
    return True


if __name__ == "__main__":
    p = Producto("P002", "Mouse inalámbrico", 279.00, 10)
    agregar_existencia(p, 5)
    retirar_existencia(p, 3)
    p.mostrar_informacion()
