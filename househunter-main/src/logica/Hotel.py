class Hotel:
    def __init__(self, nombre, direccion, habitaciones=[]):
        self.__nombre=nombre
        self.__direccion=direccion
        self.__habitaciones = habitaciones

    def agregarHabitacion(self, Habitacion):
        self.__habitaciones.append(Habitacion)

    def eliminarHabitacion(self, Habitacion):
        self.__habitaciones.remove(Habitacion)

    def verHabitacionesDisponibles(self):
        for habitacion in self.__habitaciones:
            print(habitacion)