# ***** CLASE ALUMNOS *****
# Usa el gestor Base_datos para hacer el CRUD de la tabla alumno

class Alumnos:
    # constructor
    def __init__(self, obj_base, conexion):
        self.obj_base = obj_base          # objeto Base_datos
        self.conexion = conexion          # conexion abierta
        self.tabla = "alumno"
        self.columnas = ["id_alumno", "nombre_alumno", "apellido_alumno",
                         "edad_alumno", "correo_alumno"]
        self.titulos = ["Cedula", "Nombre", "Apellido", "Edad", "Correo"]
        self.lista_alumnos = []           # arreglo de duplas que viene de la BD

    def mostrar(self):
        self.lista_alumnos = self.obj_base.tomar_info(self.conexion, self.tabla)
        return self.lista_alumnos

    def buscar(self, cedula):
        return self.obj_base.buscar(self.conexion, self.tabla, self.columnas[0], cedula)

    def guardar(self, cedula, nombre, apellido, edad, correo):
        dupla = (cedula, nombre, apellido, int(edad), correo)
        return self.obj_base.guardar(self.conexion, self.tabla, self.columnas, dupla)

    def actualizar(self, cedula, nombre, apellido, edad, correo):
        dupla = (nombre, apellido, int(edad), correo)
        return self.obj_base.actualizar(self.conexion, self.tabla, self.columnas[1:],
                                        dupla, self.columnas[0], cedula)

    def eliminar(self, cedula):
        return self.obj_base.eliminar(self.conexion, self.tabla, self.columnas[0], cedula)
