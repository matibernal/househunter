class Habitacion:

    habitaciones=[]
    def __init__(self, precio, numero):
        self.__precio = precio
        self.__numero = numero
        Habitacion.habitaciones.append(self)

    @staticmethod
    def verHabitaciones():
        print("Habitaciones: ")
        for habitacion in Habitacion.habitaciones:
            print(f"Número: {habitacion.__numero}, Precio: {habitacion.__precio}")
