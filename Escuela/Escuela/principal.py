from base_datos import Base_datos
from alumnos import Alumnos
from materias import Materias
from interfaz import Interfaz

# ***** codigo principal *****
obj_connex = Base_datos("localhost", "escuela", "root", "")
conex = obj_connex.conexion_data()

obj_alumnos = Alumnos(obj_connex, conex)
obj_materias = Materias(obj_connex, conex)

obj_interfaz = Interfaz(obj_alumnos, obj_materias)
ventana = obj_interfaz.iniciar_ventana()
ventana.mainloop()

conex.close()
