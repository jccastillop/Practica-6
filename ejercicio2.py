class Usuario:
    def __init__(self, nombre, saldo_inicial=0):
        self.nombre = nombre
        self.saldo = saldo_inicial

    def depositar(self, cantidad):
        if cantidad > 0:
            self.saldo += cantidad
            print(f"Depósito de {cantidad} realizado. Saldo actual: {self.saldo}.")
        else:
            print("La cantidad a depositar debe ser mayor que cero.")

    def retirar(self, cantidad):
        if cantidad > 0 and cantidad <= self.saldo:
            self.saldo -= cantidad
            print(f"Retiro de {cantidad} realizado. Saldo actual: {self.saldo}.")
        elif cantidad <= 0:
            print("La cantidad a retirar debe ser mayor que cero.")
        else:
            print("Fondos insuficientes para realizar el retiro.")

    def consultar_saldo(self):
        print(f"Saldo actual de {self.nombre}: {self.saldo}.")

# Ejemplo de uso
usuario1 = Usuario("Juan", saldo_inicial=1000)
usuario1.consultar_saldo()

usuario1.depositar(500)
usuario1.retirar(200)
usuario1.consultar_saldo()
