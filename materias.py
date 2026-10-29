# ***** CLASE MATERIAS *****
# Usa el gestor Base_datos para hacer el CRUD de la tabla materia

class Materias:
    # constructor
    def __init__(self, obj_base, conexion):
        self.obj_base = obj_base
        self.conexion = conexion
        self.tabla = "materia"
        self.columnas = ["id_materia", "nombre_materia", "profesor_materia",
                         "creditos_materia", "horario_materia"]
        self.titulos = ["Codigo", "Materia", "Profesor", "Creditos", "Horario"]
        self.lista_materias = []          # arreglo de duplas que viene de la BD

    def mostrar(self):
        self.lista_materias = self.obj_base.tomar_info(self.conexion, self.tabla)
        return self.lista_materias

    def buscar(self, codigo):
        return self.obj_base.buscar(self.conexion, self.tabla, self.columnas[0], codigo)

    def guardar(self, codigo, nombre, profesor, creditos, horario):
        dupla = (codigo, nombre, profesor, int(creditos), horario)
        return self.obj_base.guardar(self.conexion, self.tabla, self.columnas, dupla)

    def actualizar(self, codigo, nombre, profesor, creditos, horario):
        dupla = (nombre, profesor, int(creditos), horario)
        return self.obj_base.actualizar(self.conexion, self.tabla, self.columnas[1:],
                                        dupla, self.columnas[0], codigo)

    def eliminar(self, codigo):
        return self.obj_base.eliminar(self.conexion, self.tabla, self.columnas[0], codigo)
