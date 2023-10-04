from logica.Habitacion import Habitacion

print("Bienvenido al sistema")

while True:
    opciones=int(input('''¿Que desea hacer?
          1- Crear habitacion
          2- Ver habitaciones disponibles
          3- Hacer una reserva
          4- Cancelar una reserva
          5- Crear actividades
          6- Asignar actividades
          7- Cancelar actividades
          8- Salir del sistema'''))

    if opciones == 1:
        precio = float(input("Ingrese el costo del alquiler de la habitacion: "))
        numero = int(input("Ingrese el numero de la habitacion: "))
        habitacionNueva = Habitacion(precio, numero)
        print("La habitacion fue creada")

    elif opciones == 2:
        Habitacion.verHabitaciones()
    elif opciones == 3:
        # Realizar acción para la opción 3
        pass
    elif opciones == 4:
        pass
    elif opciones == 5:
        pass
    elif opciones == 6:
        pass
    elif opciones == 7:
        pass
    elif opciones == 8:
        print("Usted ha salido del sistema, muchas gracias")
        break
    else:
        print("La opcion ingresada no es valida")

'''error = 0
while error == 0:
    try:
        numero=int(input("Ingrese numero"))
        error=1
        print("Final")
    except ValueError:
        print("Error al escribir numero")'''
