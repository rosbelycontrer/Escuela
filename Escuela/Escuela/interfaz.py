import tkinter as Ventana
from tkinter import ttk
from tkinter import messagebox

# ***** INTERFAZ DE USUARIO (Tkinter) *****
# Una pestaña para Alumnos y otra para Materias, cada una con su CRUD:
# Guardar (Create) - Mostrar/Buscar (Read) - Actualizar (Update) - Eliminar (Delete)

class Interfaz:
    # constructor
    def __init__(self, obj_alumnos, obj_materias):
        self.colorAzul = "#1e3a8a"
        self.colorAmarillo = "yellow"
        self.formulario = None
        self.cuaderno = None
        self.obj_alumnos = obj_alumnos
        self.obj_materias = obj_materias
        # lambda CON parametro: dice si un texto esta vacio
        self.campo_vacio = lambda texto: texto.strip() == ""

    def iniciar_ventana(self):
        self.formulario = Ventana.Tk()
        self.formulario.title("Escuela - Alumnos y Materias")
        self.formulario.geometry("900x620")
        self.formulario.configure(bg=self.colorAzul)

        titulo = Ventana.Label(self.formulario, text="GESTION ESCUELA",
                               bg=self.colorAzul, fg=self.colorAmarillo,
                               font=("Arial", 18, "bold"))
        titulo.pack(pady=8)

        self.cuaderno = ttk.Notebook(self.formulario)
        self.cuaderno.pack(fill="both", expand=True, padx=10, pady=10)

        self.crear_pestana("Alumnos", self.obj_alumnos)
        self.crear_pestana("Materias", self.obj_materias)
        return self.formulario

    # metodo para no repetir el codigo de las dos pestañas
    def crear_pestana(self, nombre, gestor):
        pestana = Ventana.Frame(self.cuaderno, bg=self.colorAzul)
        self.cuaderno.add(pestana, text=nombre)

        # ----- campos -----
        marco_campos = Ventana.Frame(pestana, bg=self.colorAzul)
        marco_campos.pack(pady=10)
        entries = []
        for i in range(len(gestor.titulos)):
            label = Ventana.Label(marco_campos, text=gestor.titulos[i] + ":",
                                  bg=self.colorAmarillo, font=("Arial", 11, "bold"), width=12)
            label.grid(row=i // 2, column=(i % 2) * 2, padx=5, pady=4)
            entry = Ventana.Entry(marco_campos, font=("Arial", 11), width=28)
            entry.grid(row=i // 2, column=(i % 2) * 2 + 1, padx=5, pady=4)
            entries.append(entry)

        # ----- tabla para ver el arreglo de duplas -----
        tabla = ttk.Treeview(pestana, columns=gestor.titulos, show="headings", height=10)
        for t in gestor.titulos:
            tabla.heading(t, text=t)
            tabla.column(t, width=160)

        labelMensaje = Ventana.Label(pestana, text="", bg=self.colorAzul,
                                     fg=self.colorAmarillo, font=("Arial", 11, "bold"))

        # ----- botones del CRUD (lambda sin parametros que llama al metodo) -----
        marco_botones = Ventana.Frame(pestana, bg=self.colorAzul)
        marco_botones.pack(pady=5)
        botones = [
            ("Guardar",    lambda: self.guardar(gestor, entries, tabla, labelMensaje)),
            ("Mostrar",    lambda: self.mostrar(gestor, tabla, labelMensaje)),
            ("Buscar",     lambda: self.buscar(gestor, entries, labelMensaje)),
            ("Actualizar", lambda: self.actualizar(gestor, entries, tabla, labelMensaje)),
            ("Eliminar",   lambda: self.eliminar(gestor, entries, tabla, labelMensaje)),
            ("Limpiar",    lambda: self.limpiar_campos(entries)),
        ]
        for texto, accion in botones:
            boton = Ventana.Button(marco_botones, text=texto, width=11,
                                   font=("Arial", 11, "bold"), command=accion)
            boton.pack(side="left", padx=4)

        labelMensaje.pack(pady=5)
        tabla.pack(fill="both", expand=True, padx=10, pady=5)

        # al hacer clic en una fila se llenan los campos
        tabla.bind("<<TreeviewSelect>>", lambda evento: self.seleccionar_fila(tabla, entries))

        self.mostrar(gestor, tabla, labelMensaje)   # carga los datos al abrir

    # ================= METODOS DEL CRUD =================
    def tomar_datos(self, entries):
        datos = []
        for entry in entries:
            datos.append(entry.get())
        return datos

    def validar_campos(self, datos, labelMensaje):
        for dato in datos:
            if self.campo_vacio(dato):
                labelMensaje.configure(text="Hay campos vacios")
                return False
        return True

    def guardar(self, gestor, entries, tabla, labelMensaje):     # CREATE
        datos = self.tomar_datos(entries)
        if not self.validar_campos(datos, labelMensaje):
            return
        try:
            gestor.guardar(*datos)
            labelMensaje.configure(text="Registro " + datos[0] + " guardado")
            self.limpiar_campos(entries)
            self.mostrar(gestor, tabla, labelMensaje, mensaje=False)
        except ValueError:
            labelMensaje.configure(text="Edad / Creditos debe ser un numero")
        except Exception as error:
            messagebox.showerror("Error al guardar", str(error))

    def mostrar(self, gestor, tabla, labelMensaje, mensaje=True):  # READ
        try:
            arreglo = gestor.mostrar()          # lista de duplas
        except Exception as error:
            messagebox.showerror("Error al leer", str(error))
            return
        for fila in tabla.get_children():
            tabla.delete(fila)
        for dupla in arreglo:
            tabla.insert("", "end", values=dupla)
        if mensaje:
            labelMensaje.configure(text="Total de registros: " + str(len(arreglo)))

    def buscar(self, gestor, entries, labelMensaje):              # READ (uno)
        id_buscar = entries[0].get()
        if self.campo_vacio(id_buscar):
            labelMensaje.configure(text="Escriba el " + gestor.titulos[0] + " a buscar")
            return
        dupla = gestor.buscar(id_buscar)
        if dupla is None:
            labelMensaje.configure(text="No se encontro " + id_buscar)
        else:
            self.llenar_campos(entries, dupla)
            labelMensaje.configure(text="Encontrado: " + str(dupla))

    def actualizar(self, gestor, entries, tabla, labelMensaje):   # UPDATE
        datos = self.tomar_datos(entries)
        if not self.validar_campos(datos, labelMensaje):
            return
        try:
            filas = gestor.actualizar(*datos)
            if filas == 0:
                labelMensaje.configure(text="No hubo cambios o no existe " + datos[0])
            else:
                labelMensaje.configure(text="Registro " + datos[0] + " actualizado")
            self.mostrar(gestor, tabla, labelMensaje, mensaje=False)
        except ValueError:
            labelMensaje.configure(text="Edad / Creditos debe ser un numero")
        except Exception as error:
            messagebox.showerror("Error al actualizar", str(error))

    def eliminar(self, gestor, entries, tabla, labelMensaje):     # DELETE
        id_borrar = entries[0].get()
        if self.campo_vacio(id_borrar):
            labelMensaje.configure(text="Seleccione o escriba el " + gestor.titulos[0])
            return
        if not messagebox.askyesno("Confirmar", "¿Eliminar " + id_borrar + "?"):
            return
        try:
            filas = gestor.eliminar(id_borrar)
            if filas == 0:
                labelMensaje.configure(text="No existe " + id_borrar)
            else:
                labelMensaje.configure(text="Registro " + id_borrar + " eliminado")
            self.limpiar_campos(entries)
            self.mostrar(gestor, tabla, labelMensaje, mensaje=False)
        except Exception as error:
            messagebox.showerror("Error al eliminar", str(error))

    # ================= AYUDANTES =================
    def seleccionar_fila(self, tabla, entries):
        seleccion = tabla.selection()
        if seleccion:
            dupla = tabla.item(seleccion[0], "values")
            self.llenar_campos(entries, dupla)

    def llenar_campos(self, entries, dupla):
        self.limpiar_campos(entries)
        for i in range(len(entries)):
            entries[i].insert(0, str(dupla[i]))

    def limpiar_campos(self, entries):
        for entry in entries:
            entry.delete(0, "end")
