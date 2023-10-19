import sqlite3

class Conexion:
    def __init__(self, nombreBD):
        self.nombreBD = nombreBD
        self.conexion = sqlite3.connect(nombreBD)
        self.cursor = self.conexion.cursor()

##HABITACIONES
    def crearTablaHabitaciones(self):
        self.cursor.execute(
            "CREATE TABLE IF NOT EXISTS HABITACION("
            "id INTEGER PRIMARY KEY,"
            "precio float,"
            "capacidad int)"
        )
        self.conexion.commit()

    def insertarHabitacion(self, precio, capacidad):
        self.cursor.execute(
            "INSERT INTO HABITACION(precio, capacidad) VALUES (?,?)",
            (precio,capacidad))
        self.conexion.commit()

    def MostrarHabitaciones(self):
        self.cursor.execute("SELECT * FROM HABITACION")
        habitacion = self.cursor.fetchall()
        return habitacion

    def EditarHabitacion(self, id, precio, capacidad):
        self.cursor.execute(
            " UPDATE HABITACION SET precio=? , capacidad=? WHERE id=?",
            (precio, capacidad, id))
        self.conexion.commit()

    def EliminarHabitacion(self, id):
        self.cursor.execute(" DELETE FROM HABITACION WHERE id=?  ", (id))
        self.conexion.commit()

    def FiltrarHabitaciones(self, precio, capacidad):
        self.cursor.execute("SELECT * FROM HABITACION WHERE precio <= ? AND capacidad >= ?",
                            (precio, capacidad))
        habitaciones_filtradas = self.cursor.fetchall()


        for habitacion in habitaciones_filtradas:
            print("Numero de habitación:", habitacion[0])
            print("Precio de la habitacion:", habitacion[1])
            print("Capacidad de la habitacion:", habitacion[2])
            print()

##FIN DE HABITACIONES
    def CerrarConexion(self):
        self.cursor.close()
        self.conexion.close()