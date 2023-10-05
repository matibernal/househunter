from datetime import datetime
from logica.Habitacion import Habitacion
from logica.Actividades import Actividades
print("Bienvenido al sistema")

while True:
    opciones=int(input('''¿Que desea hacer?
          1- Crear habitacion
          2- Ver habitaciones disponibles
          3- Hacer una reserva
          4- Cancelar una reserva
          5- Crear actividades
          6- Ver actividades
          7- Asignar actividades
          8- Cancelar actividades
          9- Salir del sistema'''))

    if opciones == 1:
        precio = float(input("Ingrese el costo del alquiler de la habitacion: "))
        numero = int(input("Ingrese el numero de la habitacion: "))
        habitacionNueva = Habitacion(precio, numero)
        print("La habitacion fue creada")

    elif opciones == 2:
        Habitacion.verHabitaciones()
    elif opciones == 3:
        pass
    elif opciones == 4:
        pass
    elif opciones == 5:
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

    elif opciones == 6:
        Actividades.verActividades()
    elif opciones == 7:
        pass
    elif opciones == 8:
        print("Usted ha salido del sistema, muchas gracias")
        break
    else:
        print("La opcion ingresada no es valida")


