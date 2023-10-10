class Estudiante:
    def __init__(self, nombre, apellido, carnet, carrera):
        self.nombre = nombre
        self.apellido = apellido
        self.carnet = carnet
        self.carrera = carrera

    def actualizar_nombre(self, nuevo_nombre):
        self.nombre = nuevo_nombre

    def actualizar_apellido(self, nuevo_apellido):
        self.apellido = nuevo_apellido

    def actualizar_carnet(self, nuevo_carnet):
        self.carnet = nuevo_carnet

    def actualizar_carrera(self, nueva_carrera):
        self.carrera = nueva_carrera

    def mostrar_informacion(self):
        print(f"Información del Estudiante:\nNombre: {self.nombre}\nApellido: {self.apellido}\nCarnet: {self.carnet}\nCarrera: {self.carrera}")

# Ejemplo de uso
estudiante1 = Estudiante("Juan", "Perez", "20201234", "Ingeniería Informática")
estudiante1.mostrar_informacion()

# Actualizar información
estudiante1.actualizar_nombre("Ana")
estudiante1.actualizar_apellido("Gomez")
estudiante1.actualizar_carnet("20205678")
estudiante1.actualizar_carrera("Ingeniería de Sistemas")

# Mostrar información actualizada
estudiante1.mostrar_informacion()
