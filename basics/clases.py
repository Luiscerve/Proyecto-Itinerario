# Ejemplo de clases en Python
class Desarrollador:
    def __init__(self, nombre, especialidad):
        self.nombre = nombre
        self.especialidad = especialidad

    def presentarse(self):
        return f"Soy {self.nombre}, especializado en {self.especialidad}."

dev = Desarrollador("Luis", "Backend con Python")
print(dev.presentarse())
