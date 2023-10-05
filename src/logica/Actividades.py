class Actividades:

    listaActividades=[]
    def __init__(self, nombre, tipo, precio, fecha, idioma):
        self.__nombre = nombre
        self.__tipo = tipo
        self.__precio = precio
        self.__fecha = fecha
        self.__idioma = idioma
        Actividades.listaActividades.append(self)

    @staticmethod
    def verActividades():
        print("Actividades disponibles: ")
        for actividades in Actividades.listaActividades:
            print(f"Nombre: {actividades.__nombre}, Tipo: {actividades.__tipo}, Precio: {actividades.__precio}, Fecha: {actividades.__fecha}, Idioma: {actividades.__idioma}")