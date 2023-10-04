class Habitacion:

    habitaciones=[]
    def __init__(self, precio, numero):
        self.__precio = precio
        self.__numero = numero
        Habitacion.habitaciones.append(self)

    def verHabitaciones(self, habitaciones):
        print("Habitaciones: ", habitaciones)
