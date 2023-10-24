class Actividades:

    listaActividades=[]
    def __init__(self, id, nombre, tipo, precio, idioma):
        self.__id = id
        self.__nombre = nombre
        self.__tipo = tipo
        self.__precio = precio
        self.__idioma = idioma
        Actividades.listaActividades.append(self)

    @staticmethod
    def verActividades():
        print("Actividades disponibles: ")
        for actividades in Actividades.listaActividades:
            print(f"Nombre: {actividades.__nombre}, Tipo: {actividades.__tipo}, Precio: {actividades.__precio}, Idioma: {actividades.__idioma}")