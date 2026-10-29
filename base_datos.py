import mysql.connector

# ***** GESTOR DE LA BASE DE DATOS *****
# Esta clase solo se encarga de hablar con MySQL.
# Las clases Alumnos y Materias la usan para hacer el CRUD.

class Base_datos:
    # constructor: guarda los datos para conectarse
    def __init__(self, data_host, data, dato_user, data_clave):
        self.host = data_host
        self.data_base = data
        self.user = dato_user
        self.clave = data_clave

    def conexion_data(self):
        conexion = mysql.connector.connect(host=self.host,
                                           database=self.data_base,
                                           user=self.user,
                                           password=self.clave)
        return conexion

    # ----- R: READ (leer todo) -----
    def tomar_info(self, conexion, tabla):
        puntero = conexion.cursor()
        puntero.execute("SELECT * FROM " + tabla)
        resultado = puntero.fetchall()   # arreglo (lista) de duplas (tuplas)
        puntero.close()
        print(resultado)                 # se ve tambien por consola
        return resultado

    # ----- R: buscar un solo registro por su id -----
    def buscar(self, conexion, tabla, columna_id, valor_id):
        puntero = conexion.cursor()
        sql = "SELECT * FROM " + tabla + " WHERE " + columna_id + " = %s"
        puntero.execute(sql, (valor_id,))
        resultado = puntero.fetchone()   # una sola dupla o None
        puntero.close()
        return resultado

    # ----- C: CREATE (guardar) -----
    def guardar(self, conexion, tabla, columnas, valores):
        puntero = conexion.cursor()
        marcas = ", ".join(["%s"] * len(valores))          # %s, %s, %s, %s, %s
        sql = "INSERT INTO " + tabla + " (" + ", ".join(columnas) + ") VALUES (" + marcas + ")"
        puntero.execute(sql, valores)
        conexion.commit()                # sin commit NO se guarda
        filas = puntero.rowcount
        puntero.close()
        return filas

    # ----- U: UPDATE (actualizar) -----
    def actualizar(self, conexion, tabla, columnas, valores, columna_id, valor_id):
        puntero = conexion.cursor()
        cambios = ", ".join([columna + " = %s" for columna in columnas])
        sql = "UPDATE " + tabla + " SET " + cambios + " WHERE " + columna_id + " = %s"
        puntero.execute(sql, valores + (valor_id,))
        conexion.commit()
        filas = puntero.rowcount
        puntero.close()
        return filas

    # ----- D: DELETE (eliminar) -----
    def eliminar(self, conexion, tabla, columna_id, valor_id):
        puntero = conexion.cursor()
        sql = "DELETE FROM " + tabla + " WHERE " + columna_id + " = %s"
        puntero.execute(sql, (valor_id,))
        conexion.commit()
        filas = puntero.rowcount
        puntero.close()
        return filas
