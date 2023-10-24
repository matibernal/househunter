class ReservaActividad:
    def __init__(self,id_actividad, id_huesped, hora_ingreso, hora_salida, fecha, disponible, pago):
        self.__id_actividad=id_actividad
        self.__id_huesped=id_huesped
        self.__hora_ingreso=hora_ingreso
        self.__hora_salida=hora_salida
        self.__fecha=fecha
        self.__disponible=disponible
        self.__pago=pago