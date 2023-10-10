class Articulo:
    def __init__(self, nombre, cantidad, precio):
        self.nombre = nombre
        self.cantidad = cantidad
        self.precio = precio

    def vender(self, cantidad_a_vender):
        if cantidad_a_vender <= 0:
            print("La cantidad a vender debe ser mayor que cero.")
        elif cantidad_a_vender > self.cantidad:
            print("No hay suficientes unidades disponibles para la venta.")
        else:
            self.cantidad -= cantidad_a_vender
            total_venta = cantidad_a_vender * self.precio
            print(f"Venta realizada: {cantidad_a_vender} unidades de {self.nombre}. Total: {total_venta}.")

    def mostrar_informacion(self):
        print(f"Información del Artículo - Nombre: {self.nombre}, Cantidad: {self.cantidad}, Precio: {self.precio}")

# Ejemplo de uso
articulo_1 = Articulo("Camisa", 50, 20.0)
articulo_1.mostrar_informacion()

articulo_1.vender(10)  # Simula la venta de 10 unidades
articulo_1.mostrar_informacion()

articulo_1.vender(60)  # Intenta vender 60 unidades (más de las disponibles)
articulo_1.mostrar_informacion()

articulo_1.vender(5)   # Simula la venta de 5 unidades restantes
articulo_1.mostrar_informacion()
