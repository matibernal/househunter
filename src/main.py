from datetime import datetime
from logica.Habitacion import Habitacion
from logica.Actividades import Actividades
import sqlite3
from bdd.bd import Conexion
import unittest


'''class TestHabitacionesDisponibles(unittest.TestCase):

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
        self.assertEqual(habitacion_editada[2], capacidadeditar)'''

if __name__ == "__main__":
    print("Bienvenido al sistema")
    nombreBD = "houseHounter.db"
    conexion = Conexion(nombreBD)
    conexion.crearTablaHabitaciones()
    conexion.crearTablaActividad()
    conexion.crearTablaHuesped()
    error = 1
    opciones = 0
    ##unittest.main()
    while error != 0:
        try:
            opciones = int(input('''¿Que desea hacer?
                          1- Crear habitacion
                          2- Ver habitaciones disponibles
                          3- Editar habitaciones
                          4- Eliminar habitaciones
                          5- Buscar habitaciones por filtro
                          6- Crear actividades
                          7- Ver actividades
                          8- Eliminar actividades
                          9- Crear huesped
                          10- Ver huespedes
                          11- Eliminar huesped
                          12- Crear reserva
                          13- Ver reservas
                          14- Salir del sistema'''))

        except ValueError:
            print("La opcion ingresada no es valida")
            opciones = 0

        if opciones == 1:
            while True:
                try:
                    precio = float(input("Ingrese el costo del alquiler de la habitación: "))
                    capacidad = int(input("Ingrese la capacidad de la habitación: "))

                    if precio > 0 and capacidad > 0:
                        conexion.insertarHabitacion(precio, capacidad)
                        print("La habitación fue creada")
                        break
                    else:
                        print("El precio y la capacidad deben ser valores positivos.")
                except ValueError:
                    print("Ingresa valores numéricos válidos para el precio y la capacidad.")


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
            while True:
                try:
                    id = int(input("Ingrese el número de la habitación a editar: "))

                    if id < 0:
                        print("El ID ingresado no es válido. Debe ser mayor o igual a 0.")
                        continue

                    conexion.cursor.execute("SELECT id FROM HABITACION WHERE id=?", (id,))
                    resultado = conexion.cursor.fetchone()

                    if resultado:
                        precio = float(input("Ingrese el nuevo precio de la habitación: "))
                        capacidad = int(input("Ingrese la nueva capacidad de la habitación: "))

                        if precio > 0 and 8>= capacidad >= 0:
                            conexion.EditarHabitacion(id, precio, capacidad)
                            print("La habitación fue editada con éxito.")
                            break

                        else:
                            print("El precio debe ser mayor a cero y la capacidad de 1 a 8 personas.")
                    else:
                        print("El ID ingresado no existe en la base de datos.")
                except ValueError:
                    print("Ingresa valores válidos para ID, precio y capacidad.")

        elif opciones == 4:
            while True:
                try:
                    id = int(input("Ingrese el id de la habitacion para eliminarla"))

                    if id < 0:
                        print("El ID ingresado no es valido")

                    else:
                        conexion.cursor.execute("SELECT id FROM HABITACION WHERE id=?", (id,))
                        resultado = conexion.cursor.fetchone()

                        if resultado:
                            conexion.EliminarHabitacion(id)
                            print("La habitacion fue eliminada con éxito")
                            break
                        else:
                            print("El ID ingresado no existe")
                except ValueError:
                    print("Error")



        elif opciones == 5:

            while True:
                try:
                    precio_max = float(input("Ingrese el precio máximo que busca en una habitación: "))

                    if precio_max <= 0:
                        print("El precio máximo debe ser mayor que cero.")
                        continue

                    capacidad_min = int(input("Ingrese la capacidad mínima que busca en una habitación: "))

                    if capacidad_min <= 0:
                        print("La capacidad mínima debe ser mayor que cero.")
                        continue

                    conexion.FiltrarHabitaciones(precio_max, capacidad_min)
                    break

                except ValueError:
                    print("Ingrese valores válidos para precio máximo y capacidad mínima.")





        elif opciones == 6:
            while True:
                try:
                    actividad = input("Ingrese el nombre de la actividad: ")
                    precio = float(input("Ingrese el precio de la actividad por persona: "))

                    if precio <= 0:
                        print("El precio de la actividad debe ser mayor que cero.")
                        continue

                    cupos = int(input("Ingrese los cupos totales de la actividad: "))

                    if cupos <= 0:
                        print("Los cupos totales deben ser mayores que cero.")
                        continue

                    cant_reservas = 0
                    disponible = 1
                    conexion.InsertarActividad(actividad, precio, cupos, cant_reservas, disponible)
                    print("Actividad creada con éxito.")
                    break

                except ValueError:
                    print("Ingrese valores válidos para precio y cupos.")


        elif opciones == 7:
            actividades = conexion.MostrarActividad()

            if len(actividades) > 0:
                print("Lista de actividades")
                for actividad in actividades:
                    print(
                        f"Numero: {actividad[0]}, Actividad: {actividad[1]} , Precio: {actividad[2]}, Cupos totales: {actividad[3]}, Inscriptos: {actividad[4]}"
                    )

            else:
                print("No hay actividades creadas")

        elif opciones == 8:

            id = input("Ingrese el numero de la actividad para borrarla")
            conexion.EliminarActividad(id)


        elif opciones == 9:

            nombre = input("Ingrese el nombre del huésped: ")
            apellido = input("Ingrese el apellido del huésped: ")

            while True:
                try:
                    dni = int(input("Ingrese el DNI del huésped: "))

                    if len(str(dni)) != 8:
                        print("El DNI debe tener 8 dígitos.")
                        continue
                    break

                except ValueError:
                    print("Ingrese un número de DNI válido.")

            while True:
                try:
                    edad = int(input("Ingrese la edad del huésped: "))

                    if edad <= 16:
                        print("El huésped debe ser mayor de 16 años.")
                        continue
                    break

                except ValueError:
                    print("Ingrese una edad válida.")

            while True:

                sexo = input("Ingrese el sexo del huésped (M/F): ")

                if sexo not in ["M", "F"]:
                    print("Ingrese 'M' para masculino o 'F' para femenino.")
                else:
                    break

            idioma = input("Ingrese el idioma del huésped: ")
            nacionalidad = input("Ingrese la nacionalidad del huésped: ")

            conexion.InsertarHuesped(nombre, apellido, dni, edad, sexo, idioma, nacionalidad)

        elif opciones == 10:
            huespedes = conexion.MostrarHuesped()

            if len(huespedes) > 0:
                print("Lista de huespedes")
                for huesped in huespedes:
                    print(
                        f"Numero: {huesped[0]}, Nombre: {huesped[1]} , Apellido: {huesped[2]}, Edad: {huesped[4]}, Sexo: {huesped[5]}, Nacionalidad: {huesped[7]}"
                    )

            else:
                print("No hay huespedes actualmente")

        elif opciones == 11:
            id = input("Ingrese el id del huesped para eliminarlo")
            conexion.EliminarHuesped(id)

        elif opciones == 12:
            print("Usted ha salido del sistema, muchas gracias")
            error = 0
            conexion.CerrarConexion()
        else:
            print("La opcion ingresada no es valida")