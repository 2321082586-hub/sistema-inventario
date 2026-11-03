class Producto:
    """Representa un producto del sistema de inventario."""

    def __init__(self, codigo, nombre, precio, existencia):
        self.codigo = codigo
        self.nombre = nombre
        self.precio = precio
        self.existencia = existencia

    def mostrar_informacion(self):
        print("Código:     ", self.codigo)
        print("Nombre:     ", self.nombre)
        print(f"Precio:      ${self.precio:,.2f}")
        print("Existencia: ", self.existencia)
        print("Producto registrado")


if __name__ == "__main__":
    producto = Producto("P001", "Teclado USB", 349.90, 25)
    producto.mostrar_informacion()
