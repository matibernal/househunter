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
        self.cursor.execute("DELETE FROM HABITACION WHERE id=?", (id,))
        self.conexion.commit()

    def FiltrarHabitaciones(self, precio, capacidad):
        self.cursor.execute("SELECT * FROM HABITACION WHERE precio <= ? AND capacidad >= ?",
                            (precio, capacidad))
        habitaciones_filtradas = self.cursor.fetchall()

        if not habitaciones_filtradas:
            print("No se encontraron habitaciones que cumplan el filtro")
        else:
            for habitacion in habitaciones_filtradas:
                print("Numero de habitación:", habitacion[0])
                print("Precio de la habitacion:", habitacion[1])
                print("Capacidad de la habitacion:", habitacion[2])
                print()

##FIN DE HABITACIONES
    ##HUESPED
    def crearTablaHuesped(self):
        self.cursor.execute(
            "CREATE TABLE IF NOT EXISTS HUESPED("
            "id INTEGER PRIMARY KEY,"
            "nombre text,"
            "apellido text,"
            "dni int,"
            "edad int,"
            "sexo text,"
            "idioma text,"
            "nacionalidad text)"
        )
        self.conexion.commit()

    def InsertarHuesped(self, nombre, apellido, dni, edad, sexo, idioma, nacionalidad):
        self.cursor.execute(
            "INSERT INTO HUESPED (nombre, apellido, dni, edad, sexo, idioma, nacionalidad) VALUES (?,?, ?, ?, ?, ?, ?)",
            (nombre, apellido, dni, edad, sexo, idioma, nacionalidad))
        self.conexion.commit()

    def MostrarHuesped(self):
        self.cursor.execute("SELECT * FROM HUESPED")
        huesped = self.cursor.fetchall()
        return huesped

    def EditarHuesped(self, id, nombre, apellido, dni, edad, sexo, idioma, nacionalidad):
        self.cursor.execute(
            " UPDATE HUESPED SET nombre=? , apellido=?, dni=? , edad=?, sexo=? , idioma=?, nacionalidad=? WHERE id=?",
            (nombre, apellido, dni, edad, sexo, idioma, nacionalidad, id))
        self.conexion.commit()

    def EliminarHuesped(self, id):
        self.cursor.execute("SELECT id FROM HUESPED WHERE id=?", (id,))
        resultado = self.cursor.fetchone()

        if resultado:
            self.cursor.execute("DELETE FROM HUESPED WHERE id=?", (id,))
            self.conexion.commit()
            print("El huesped fue eliminado con éxito")
        else:
            print("El ID ingresado no existe, no se pudo eliminar al huesped")
    ##falta filtro por huesped

    ##NOMBRE DE LAS HABITACIONES --- ## agregar los insert a mano
    def crearTablaNombreHabitaciones(self):
        self.cursor.execute(
            "CREATE TABLE IF NOT EXISTS NOMBRE_HABITACIONES("
            "id INTEGER PRIMARY KEY,"
            "nombre text,"
            "sexo text)"
        )
        self.conexion.commit()

    def InsertarNombreHabitaciones(self, nombre, sexo):
        self.cursor.execute(
            "INSERT INTO NOMBRE_HABITACIONES(nombre, sexo) VALUES (?,?)",
            (nombre, sexo))
        self.conexion.commit()

    def MostrarNombreHabitaciones(self):
        self.cursor.execute("SELECT * FROM NOMBRE_HABITACIONES")
        nombre_habitaciones = self.cursor.fetchall()
        return nombre_habitaciones

    def EditarNombreHabitaciones(self, id, precio, capacidad):
        self.cursor.execute(
            " UPDATE NOMBRE_HABITACIONES SET nombre=? , sexo=? WHERE id=?",
            (precio, capacidad, id))
        self.conexion.commit()

    def EliminarNombreHabitaciones(self, id):
        self.cursor.execute(" DELETE FROM NOMBRE_HABITACIONES WHERE id=?  ", (id))
        self.conexion.commit()

    ## filtro de tipos de reservas

    ##RECEPCIONISTA -- ver si creamos empleado o recepcionista y si puede fiChar o no
    def crearTablaRecepcionista(self):
        self.cursor.execute(
            "CREATE TABLE IF NOT EXISTS RECEPCIONISTA("
            "id INTEGER PRIMARY KEY,"
            "dni int,"
            "nombre text,"
            "apellido text,"
            "sueldo float)"
        )
        self.conexion.commit()

    def InsertarRecepcionista(self, dni, nombre, apellido, sueldo):
        self.cursor.execute(
            "INSERT INTO RECEPCIONISTA(dni, nombre, apellido, sueldo) VALUES (?,?)",
            (dni, nombre, apellido, sueldo))
        self.conexion.commit()

    def MostrarRecepcionista(self):
        self.cursor.execute("SELECT * FROM RECEPCIONISTA")
        recepcionista = self.cursor.fetchall()
        return recepcionista

    def EditarNombreRecepcionista(self, id, precio, capacidad):
        self.cursor.execute(
            " UPDATE RECEPCIONISTA SET dni=? , nombre=?, apellido=?, sueldo=? WHERE id=?",
            (precio, capacidad, id))
        self.conexion.commit()

    def EliminarRecepcionista(self, id):
        self.cursor.execute(" DELETE FROM RECEPCIONISTA WHERE id=?  ", (id))
        self.conexion.commit()

    ##filtrar recepcionistas por sueldo?

    ##FICHAR
    def crearTablaFichaje(self):
        self.cursor.execute(
            "CREATE TABLE IF NOT EXISTS FICHAJE("
            "id INTEGER PRIMARY KEY,"
            "fecha date,"
            "hora_ingreso time,"
            "hora_salida time,"
            "ID_Recepcionista int FOREIGN KEY)"
        )
        self.conexion.commit()

    def InsertarFichaje(self, fecha, hora_ingreso, hora_salida, ID_Recepcionista):
        self.cursor.execute(
            "INSERT INTO FICHAJE(fecha, hora_ingreso, hora_salida, ID_Recepcionista) VALUES (?,?, ?, ?)",
            (fecha, hora_ingreso, hora_salida, ID_Recepcionista))
        self.conexion.commit()

    def MostrarFichaje(self):
        self.cursor.execute("SELECT * FROM FICHAJE")
        fichaje = self.cursor.fetchall()
        return fichaje

    def EditarFichaje(self, id, fecha, hora_ingreso, hora_salida, ID_Recepcionista):
        self.cursor.execute(
            " UPDATE FICHAJE SET fecha=? , hora_ingreso=?, hora_salida=?, ID_Recepcionista=? WHERE id=?",
            (fecha, hora_ingreso, hora_salida, ID_Recepcionista, id))
        self.conexion.commit()

    def EliminarFichaje(self, id):
        self.cursor.execute(" DELETE FROM FICHAJE WHERE id=?  ", (id))
        self.conexion.commit()

    ## filtrar fichajes por fecha

    ##FORMA RESERVA ##agregar insert a mano
    def crearTablaForma_Reserva(self):
        self.cursor.execute(
            "CREATE TABLE IF NOT EXISTS FORMA_RESERVA("
            "id INTEGER PRIMARY KEY,"
            "nombre text)"
        )
        self.conexion.commit()

    def InsertarForma_Reserva(self, nombre):
        self.cursor.execute(
            "INSERT INTO FORMA_RESERVA(nombre) VALUES (?)",
            (nombre))
        self.conexion.commit()

    def MostrarForma_Reserva(self):
        self.cursor.execute("SELECT * FROM FORMA_RESERVA")
        forma_reserva = self.cursor.fetchall()
        return forma_reserva

    def EditarForma_Reserva(self, nombre):
        self.cursor.execute(
            " UPDATE FORMA_RESERVA SET nombre=? WHERE id=?",
            (nombre, id))
        self.conexion.commit()

    def EliminarForma_Reserva(self, id):
        self.cursor.execute(" DELETE FROM FORMA_RESERVA WHERE id=?  ", (id))
        self.conexion.commit()

    ##RESERVA
    def crearTablaTiposReserva(self):
        self.cursor.execute(
            "CREATE TABLE IF NOT EXISTS TIPOS_RESERVA("
            "id INTEGER PRIMARY KEY,"
            "tipo int,"
            "descripcion text)"
        )
        self.conexion.commit()

    def InsertarTiposReserva(self, precio, capacidad):
        self.cursor.execute(
            "INSERT INTO TIPOS_RESERVA(tipo, descripcion) VALUES (?,?)",
            (precio, capacidad))
        self.conexion.commit()

    def MostrarTiposReserva(self):
        self.cursor.execute("SELECT * FROM TIPOS_RESERVA")
        tipos_reserva = self.cursor.fetchall()
        return tipos_reserva

    def EditarTiposReserva(self, id, precio, capacidad):
        self.cursor.execute(
            " UPDATE TIPOS_RESERVA SET tipo=? , descripcion=? WHERE id=?",
            (precio, capacidad, id))
        self.conexion.commit()

    def EliminarTiposReserva(self, id):
        self.cursor.execute(" DELETE FROM TIPOS_RESERVA WHERE id=?  ", (id))
        self.conexion.commit()

    ## falta filtro de reserva

    ##RESERVA HABITACION
    def crearTablaReservaHabitacion(self):
        self.cursor.execute(
            "CREATE TABLE IF NOT EXISTS RESERVA_HABITACION("
            "id INTEGER PRIMARY KEY,"
            "desde date,"
            "hasta date,"
            "check_in time,"
            "chek_out time,"
            "cantidad_personas int,"
            "terminada boolean,"
            "llave_entregada boolean DEFAULT 0,"
            "confirmada boolean DEFAULT 0,"
            "pago float,"
            "pago_realizado boolean,"
            "cancelada boolean DEFAULT 0,"
            "ID_huesped int,"
            "ID_habitacion int,"
            "ID_formareserva int,"
            "FOREIGN KEY (ID_huesped) REFERENCES HUESPED(id),"
            "FOREIGN KEY (ID_habitacion) REFERENCES HABITACION(id))"
        )
        self.conexion.commit()

    def InsertarReservaHabitacion(self, desde, hasta, check_in, chek_out, terminada, llave_entregada, confirmada, pago,
                                  pago_realizado, cancelada, ID_huesped, ID_habitacion, ID_formareserva):
        self.cursor.execute(
            "INSERT INTO RESERVA_HABITACION (desde, hasta, check_in, chek_out, terminada, llave_entregada, confirmada, pago, pago_realizado, cancelada, ID_huesped, ID_habitacion, ID_formareserva) VALUES (?,?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)",
            (desde, hasta, check_in, chek_out, terminada, llave_entregada, confirmada, pago, pago_realizado, cancelada,
             ID_huesped, ID_habitacion, ID_formareserva))
        self.conexion.commit()

    def MostrarReservaHabitacion(self):
        self.cursor.execute("SELECT * FROM RESERVA_HABITACION")
        reserva_habitacion = self.cursor.fetchall()
        return reserva_habitacion

    def EditarReservaHabitacion(self, id, desde, hasta, check_in, chek_out, terminada, llave_entregada, confirmada,
                                pago, pago_realizado, cancelada, ID_huesped, ID_habitacion, ID_formareserva):
        self.cursor.execute(
            " UPDATE HABITACION SET desde=? , hasta=?, check_in=? , chek_out=?, terminada=? , llave_entregada=?, confirmada=? , pago=?, pago_realizado=?, cancelada=?, ID_huesped=?, ID_habitacion=? , ID_formareserva=? WHERE id=?",
            (desde, hasta, check_in, chek_out, terminada, llave_entregada, confirmada, ID_huesped, pago, pago_realizado,
             cancelada, ID_habitacion, ID_formareserva, id))
        self.conexion.commit()

    def EliminarReservaHabitacion(self, id):
        self.cursor.execute(" DELETE FROM HABITACION WHERE id=?  ", (id))
        self.conexion.commit()

    ##falta filtro de las reservas de las habitaciones

    ##ACTIVIDADES -- ## agregar los insert a mano

    def crearTablaActividad(self):
        self.cursor.execute(
            "CREATE TABLE IF NOT EXISTS ACTIVIDAD("
            "id INTEGER PRIMARY KEY,"
            "actividad text,"
            "precio float,"
            "cupos int,"
            "cant_reservas int,"
            "disponible boolean DEFAULT 1)"
        )
        self.conexion.commit()

    def InsertarActividad(self, actividad, precio, cupos, cant_reservas, disponible):
        self.cursor.execute(
            "INSERT INTO ACTIVIDAD (actividad, precio, cupos, cant_reservas, disponible) VALUES (?, ?, ?, ?, ?)",
            (actividad, precio, cupos, cant_reservas, disponible))
        self.conexion.commit()

    def MostrarActividad(self):
        self.cursor.execute("SELECT * FROM ACTIVIDAD")
        actividad = self.cursor.fetchall()
        return actividad

    def EditarActividad(self, id, actividad, precio, cupos, cant_reservas, disponible):
        self.cursor.execute(
            " UPDATE ACTIVIDAD SET actividad=? , precio=?, cupos=? , cant_reservas=?, disponible=? WHERE id=?",
            (actividad, precio, cupos, cant_reservas, disponible, id))
        self.conexion.commit()

    def EliminarActividad(self, id):
        self.cursor.execute("SELECT id FROM ACTIVIDAD WHERE id=?", (id,))
        resultado = self.cursor.fetchone()

        if resultado:
            self.cursor.execute("DELETE FROM ACTIVIDAD WHERE id=?", (id,))
            self.conexion.commit()
            print("La actividad fue eliminada con éxito")
        else:
            print("El ID ingresado no existe, no se pudo eliminar la actividad")

    ##falta filtro de las actvidades
    def crearTablaReservaActividad(self):
        self.cursor.execute(
            "CREATE TABLE IF NOT EXISTS RESERVA_ACTIVIDAD("
            "id INTEGER PRIMARY KEY,"
            "fecha date,"
            "hora_ingreso time,"
            "hora_salida time,"
            "confirmada boolean DEFAULT 0,"
            "cancelada boolean DEFAULT 0,"
            "disponible boolean,"
            "pago_realizado boolean,"
            "ID_actividad int,"
            "ID_huesped int ,"
            "ID_forma_reserva int ,"
            "FOREIGN KEY (ID_actividad) REFERENCES ACTIVIDAD(id),"
            "FOREIGN KEY (ID_huesped) REFERENCES HUESPED(id),"
            "FOREIGN KEY (ID_forma_reserva) REFERENCES FORMA_RESERVA(id))"
        )
        self.conexion.commit()

    def InsertarReservaActividad(self, fecha, hora_ingreso, hora_salida, confirmada, cancelada, disponible,
                                 pago_realizado, ID_actividad, ID_huesped, ID_forma_reserva):
        self.cursor.execute(
            "INSERT INTO RESERVA_HABITACION (fecha, hora_ingreso, hora_salida, confirmada, cancelada, disponible, pago_realizado, ID_actividad, ID_huesped, ID_forma_reserva) VALUES (?,?, ?, ?, ?, ?, ?, ?, ?, ?)",
            (fecha, hora_ingreso, hora_salida, confirmada, cancelada, disponible, pago_realizado, ID_actividad,
             ID_huesped, ID_forma_reserva))
        self.conexion.commit()

    def MostrarReservaActividad(self):
        self.cursor.execute("SELECT * FROM RESERVA_ACTIVIDAD")
        reserva_actividad = self.cursor.fetchall()
        return reserva_actividad

    def EditarReservaActividad(self, id, fecha, hora_ingreso, hora_salida, confirmada, cancelada, disponible,
                               pago_realizado, ID_actividad, ID_huesped, ID_forma_reserva):
        self.cursor.execute(
            " UPDATE RESERVA_ACTIVIDAD SET fecha=? , hora_ingreso=?, hora_salida=? , confirmada=?, cancelada=? , disponible=?, confirmada=? , pago_realizado=?, ID_actividad=?, ID_huesped=?, ID_forma_reserva=? WHERE id=?",
            (fecha, hora_ingreso, hora_salida, confirmada, cancelada, disponible, pago_realizado, ID_actividad,
             ID_huesped, ID_forma_reserva, id))
        self.conexion.commit()

    def EliminarReservaActividad(self, id):
        self.cursor.execute(" DELETE FROM RESERVA_ACTIVDAD WHERE id=?  ", (id))
        self.conexion.commit()

    ##falta filtro de las reservas de las actividades

    ##CERRAR CONEXION
    def CerrarConexion(self):
        self.cursor.close()
        self.conexion.close()