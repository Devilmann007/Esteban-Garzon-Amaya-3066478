# Clase personaje

class Personaje:
    def __init__(self, nombre, salud):
        self.nombre = nombre
        self.salud = salud

    def recibir_daño(self, cantidad):
        self.salud -= cantidad
        print(f"{self.nombre} ha recibido {cantidad} de daño. Salud restante: {self.salud}")
