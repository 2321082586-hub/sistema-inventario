"""Programa principal del Sistema de Inventario (consola).

Uso:
    python src/main.py          menú interactivo
    python src/main.py --demo   registra, consulta y muestra productos de ejemplo
"""
import sys

from producto import Producto

inventario = {}


def registrar_producto(codigo, nombre, precio, existencia):
    if codigo in inventario:
        print(f"Ya existe un producto con el código {codigo}.")
        return False
    inventario[codigo] = Producto(codigo, nombre, precio, existencia)
    print(f"Producto {codigo} registrado.")
    return True


def consultar_producto(codigo):
    producto = inventario.get(codigo)
    if producto is None:
        print(f"No existe el producto {codigo}.")
    else:
        producto.mostrar_informacion()
    return producto


def mostrar_inventario():
    if not inventario:
        print("El inventario está vacío.")
        return
    for producto in inventario.values():
        print("-" * 32)
        producto.mostrar_informacion()
    print("-" * 32)
    print(f"Total de productos: {len(inventario)}")


def valor_inventario():
    """Calcula el valor total del inventario (precio x existencia)."""
    total = sum(p.precio * p.existencia for p in inventario.values())
    print(f"Valor total del inventario: ${total:,.2f}")
    return total


def demo():
    print("=== Sistema de Inventario (demostración) ===")
    registrar_producto("P001", "Teclado", 350, 10)
    registrar_producto("P002", "Mouse", 180, 5)
    print("\n>> Consultar P001")
    consultar_producto("P001")
    print("\n>> Inventario completo")
    mostrar_inventario()
    print("\n>> Valor del inventario")
    valor_inventario()
    print("\nSistema funcionando correctamente.")


def menu():
    while True:
        print("\n1) Registrar producto\n2) Consultar producto\n3) Mostrar inventario\n4) Salir")
        opcion = input("Opción: ").strip()
        if opcion == "1":
            try:
                codigo = input("Código: ").strip()
                nombre = input("Nombre: ").strip()
                precio = float(input("Precio: "))
                existencia = int(input("Existencia: "))
            except ValueError:
                print("Precio o existencia no válidos.")
                continue
            registrar_producto(codigo, nombre, precio, existencia)
        elif opcion == "2":
            consultar_producto(input("Código: ").strip())
        elif opcion == "3":
            mostrar_inventario()
        elif opcion == "4":
            print("Hasta luego.")
            break
        else:
            print("Opción no válida.")


if __name__ == "__main__":
    if "--demo" in sys.argv:
        demo()
    else:
        menu()
