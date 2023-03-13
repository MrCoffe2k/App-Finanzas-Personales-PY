from tkcalendar import Calendar
from tkinter import ttk
import tkinter as tk
import tkinter.font as tkFont
import sqlite3
import pandas as pd

# Conectar a la base de datos
conexion = sqlite3.connect('finanzas.db')

# Funciones que se ejecutan al hacer clic en los botones del menú principal

def abrir_ingresos():
    # Crear ventana emergente para ingresos
    global ventana_ingresos
    ventana_ingresos = tk.Toplevel()
    ventana_ingresos.geometry("500x500")

    # Crear campo para ingresar el monto
    lbl_monto = tk.Label(ventana_ingresos, text="Monto:")
    lbl_monto.pack(pady=5)
    global entry_monto
    entry_monto = tk.Entry(ventana_ingresos)
    entry_monto.pack(pady=5)

    # Crear calendario para seleccionar la fecha
    lbl_fecha = tk.Label(ventana_ingresos, text="Fecha:")
    lbl_fecha.pack(pady=5)
    global cal_fecha
    cal_fecha = Calendar(ventana_ingresos)
    cal_fecha.pack(pady=5)

    # Crear botón de inicio en la ventana emergente
    btn_inicio = tk.Button(ventana_ingresos, text="Inicio",command=ventana_ingresos.destroy)
    btn_inicio.pack(pady=10)

    # Crear botón de guardar en la ventana emergente
    btn_guardar = tk.Button(ventana_ingresos, text="Guardar", command=guardar_ingreso)
    btn_guardar.pack(pady=10)

def guardar_ingreso():
    # Obtener los valores de los campos de entrada
    monto = entry_monto.get()
    fecha = cal_fecha.selection_get().strftime('%d-%m-%Y')
    c = conexion.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS movimientos
                 (monto REAL, fecha TEXT, categoria TEXT NULL, tipo TEXT)''')
    c.execute("INSERT INTO movimientos VALUES (?, ?, ' ', 'ingreso')", (monto, fecha))
    conexion.commit()

def abrir_gastos():
    # Crear ventana emergente para gastos
    global ventana_gastos
    ventana_gastos = tk.Toplevel()
    ventana_gastos.geometry("500x500")
    
    # Crear campo para ingresar el monto
    lbl_monto = tk.Label(ventana_gastos, text="Monto:")
    lbl_monto.pack(pady=5)
    global entry_monto
    entry_monto = tk.Entry(ventana_gastos)
    entry_monto.pack(pady=5)

    # Crear lista desplegable para seleccionar la categoría
    lbl_categoria = tk.Label(ventana_gastos, text="Categoría:")
    lbl_categoria.pack(pady=5)
    categorias = ["Alimentación", "Transporte",
                  "Entretenimiento", "Salud", "Educación", "Otros"]
    global var_categoria
    var_categoria = tk.StringVar(value=categorias[0])
    combo_categoria = tk.OptionMenu(ventana_gastos, var_categoria, *categorias)
    combo_categoria.pack(pady=5)

    # Crear calendario para seleccionar la fecha
    lbl_fecha = tk.Label(ventana_gastos, text="Fecha:")
    lbl_fecha.pack(pady=5)
    global cal_fecha
    cal_fecha = Calendar(ventana_gastos)
    cal_fecha.pack(pady=5)

    # Crear botón de inicio en la ventana emergente
    btn_inicio = tk.Button(ventana_gastos, text="Inicio", command=ventana_gastos.destroy)
    btn_inicio.pack(pady=10)

    # Crear botón de guardar en la ventana emergente
    btn_guardar = tk.Button(ventana_gastos, text="Guardar", command=guardar_gasto)
    btn_guardar.pack(pady=10)

def guardar_gasto():
    # Obtener los valores de los campos de entrada
    monto = entry_monto.get()
    categoria = var_categoria.get()
    fecha = cal_fecha.selection_get().strftime('%d-%m-%Y')
    c = conexion.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS movimientos
                 (monto REAL, fecha TEXT, categoria TEXT NULL, tipo TEXT)''')
    c.execute("INSERT INTO movimientos VALUES (?, ?, ?, 'gasto')", (monto, fecha, categoria))
    conexion.commit()

def abrir_resumen():
    # Crear ventana emergente para resumen
    global ventana_resumen
    ventana_resumen = tk.Toplevel()
    ventana_resumen.geometry("500x500")
    
    # Crear botón de inicio en la ventana emergente
    btn_inicio = tk.Button(ventana_resumen, text="Inicio", command=ventana_resumen.destroy)
    btn_inicio.pack(pady=10)

    # Consultar la tabla y cargar los datos en un DataFrame de Pandas
    df = pd.read_sql_query("SELECT * from movimientos", conexion)
      
    # Crear una tabla tkinter usando el widget Table
    class Table(tk.Frame):
        def __init__(self, parent=None, headings=tuple(), rows=list()):
            super().__init__(parent)

            self.headings = headings
            self.rows = rows
            self.sort_column = None
            self.sort_descending = False

            self.table = ttk.Treeview(self, show="headings", selectmode="browse")
            self.table["columns"] = headings
            self.table["displaycolumns"] = headings

            for head in headings:
                self.table.heading(head, text=head, anchor="center")
                self.table.column(head, anchor="center", width=tkFont.Font().measure(head))
                self.table.heading(head, command=lambda col=head: self.sort_table(col))

            for row in rows:
                self.table.insert("", "end", values=row)
                # Establecer el ancho de cada columna al ancho mínimo requerido
                for i, item in enumerate(row):
                    col_width = tkFont.Font().measure(item)
                    if self.table.column(self.headings[i], width=None) < col_width:
                        self.table.column(self.headings[i], width=col_width)

            scrolltable = ttk.Scrollbar(self, orient="vertical", command=self.table.yview)
            self.table.configure(yscrollcommand=scrolltable.set)
            scrolltable.pack(side="right", fill="y")
            self.table.pack(expand=True, fill="both")

        def sort_table(self, col):
            # Si se hace clic en la misma columna, invertir el orden de clasificación
            if col == self.sort_column:
                self.sort_descending = not self.sort_descending
            else:
                self.sort_column = col
                self.sort_descending = False

            # Ordenar las filas según la columna correspondiente
            col_index = self.headings.index(col)
            self.rows.sort(key=lambda row: row[col_index], reverse=self.sort_descending)

            # Eliminar todas las filas actuales de la tabla
            for row in self.table.get_children():
                self.table.delete(row)

            # Agregar las filas ordenadas a la tabla
            for row in self.rows:
                self.table.insert("", "end", values=row)

    # Obtener los encabezados y las filas de la tabla
    headings = df.columns.tolist()
    rows = df.values.tolist()

    # Crear y mostrar la tabla en la ventana emergente
    table = Table(ventana_resumen, headings=headings, rows=rows)
    table.pack(expand=True, fill="both")

# Función para cerrar la conexion a la base de datos y las ventanas
def cerrar():
    conexion.close()
    ventana.destroy()

# Crear ventana principal
ventana = tk.Tk()

# Establecer tamaño de ventana
ventana.geometry("500x500")

# Crear botones del menú principal
btn_ingresos = tk.Button(ventana, text="Ingresos", command=abrir_ingresos)
btn_gastos = tk.Button(ventana, text="Gastos", command=abrir_gastos)
btn_resumen = tk.Button(ventana, text="Resumen", command=abrir_resumen)
btn_salir = tk.Button(ventana, text="Salir", command=cerrar)

# Posicionar botones en la ventana
btn_ingresos.pack(pady=10)
btn_gastos.pack(pady=10)
btn_resumen.pack(pady=10)
btn_salir.pack(pady=10)

# Ejecutar ventana
ventana.mainloop()
