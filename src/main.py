from datetime import datetime
from logica.Habitacion import Habitacion
from logica.Actividades import Actividades
import sqlite3
from bdd.bd import Conexion
import unittest

'''
class TestHabitacionesDisponibles(unittest.TestCase):

    def setUp(self):
        self.nombreBD = "test_HouseHunter.db"
        self.conexion = Conexion(self.nombreBD)
        self.conexion.crearTablaHabitaciones()

    def tearDown(self):
        self.conexion.CerrarConexion()
    def test_habitaciones_disponibles(self):

        precio = 200
        capacidad = 2
        self.conexion.insertarHabitacion(precio, capacidad)

        habitaciones = self.conexion.MostrarHabitaciones()

        self.assertTrue(len(habitaciones) > 0)


    def test_editarHabitaciones(self):

        precio = 300
        capacidad = 1
        self.conexion.insertarHabitacion(precio,capacidad)

        precioeditar= 400
        capacidadeditar= 3
        id_habitacion= 1

        self.conexion.EditarHabitacion( id_habitacion, precioeditar,capacidadeditar)

        habitacion_editada = self.conexion.MostrarHabitaciones()[0]

        self.assertEqual(habitacion_editada[1], precioeditar)
        self.assertEqual(habitacion_editada[2], capacidadeditar)
'''
if __name__ == "__main__":
    print("Bienvenido al sistema")
    nombreBD = "houseHounter.db"
    conexion = Conexion(nombreBD)
    conexion.crearTablaHabitaciones()
    error = 1
    opciones = 0
    unittest.main()
    while error!= 0:
        try:
            opciones = int(input('''¿Que desea hacer?
                          1- Crear habitacion
                          2- Ver habitaciones disponibles
                          3- Editar habitaciones
                          4- Eliminar habitaciones
                          5- Buscar habitaciones por filtro
                          6- Crear actividades
                          7- Ver actividades
                          8- Cancelar actividades
                          9- Salir del sistema'''))

        except ValueError:
            print("La opcion ingresada no es valida")
            opciones = 0

        if opciones == 1:
            precio = float(input("Ingrese el costo del alquiler de la habitacion: "))
            capacidad = int(input("Ingrese la capacidad de la habitacion"))
            conexion.insertarHabitacion(precio,capacidad)
            print("La habitacion fue creada")

        elif opciones == 2:
            habitaciones = conexion.MostrarHabitaciones()

            if len(habitaciones) > 0:
                print("Lista de habitaciones")
                for habitacion in habitaciones:
                    print(
                        f"Precio: {habitacion[1]}, Capacidad: {habitacion[2]} , Numero: {habitacion[0]}"
                    )

            else:
                print("No hay habitaciones creadas")
        elif opciones == 3:
            id = input("Ingrese el numero de la habitacion a editar")
            precio = input("Ingrese el precio de la habitacion")
            capacidad = input("Ingrese la capacidad de la habitacion")
            conexion.EditarHabitacion(id, precio, capacidad)
            print("La habitacion fue editada con exito")

        elif opciones == 4:
            id = input("Ingrese el id de la habitacion para eliminarla")
            conexion.EliminarHabitacion(id)
            print("La habitacion fue eliminada con exito")

        elif opciones == 5:
            precio_max = float(input("Ingrese el precio máximo que busca en una habitacion"))
            capacidad_min = int(input("Ingrese la capacidad minima que busca en una habitacion"))
            conexion.FiltrarHabitaciones(precio_max,capacidad_min)


        elif opciones == 6:
            nombre = input("Ingrese el nombre de la actividad: ")
            tipo = input("Ingrese el tipo de actividad: ")
            precio = float(input("Ingrese el precio de la actividad: "))
            fechastr = input("Ingrese la fecha y hora de la actividad con el formato 'YYYY-MM-DD HH:MM:SS': ")
            try:
                fecha = datetime.strptime(fechastr, "%Y-%m-%d %H:%M:%S")
                print("Fecha de la actividad: ", fecha)
            except ValueError:
                print("El formato de la fecha ingresada no es valido, use 'YYYY-MM-DD HH:MM:SS' por favor")
            idioma = input("Ingrese el idioma de la actividad: ")
            actividadNueva = Actividades(nombre, tipo, precio, fecha, idioma)

        elif opciones == 7:
            Actividades.verActividades()
        elif opciones == 8:
            pass
        elif opciones == 9:
            print("Usted ha salido del sistema, muchas gracias")
            error=0
            conexion.CerrarConexion()
        else:
            print("La opcion ingresada no es valida")


