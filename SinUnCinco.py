from tkcalendar import Calendar
from tkinter import messagebox, ttk
import tkinter as tk
import tkinter.font as tkFont
import sqlite3
import pandas as pd
import datetime
import babel.numbers
import sys
from PIL import ImageTk, Image

# Conectar a la base de datos
conexion = sqlite3.connect('database/finanzas.db')

# Funciones que se ejecutan al hacer clic en los botones del menú principal

# Formato de fecha
date = '%Y-%m-%d'

# Imagen que se usa como icono
icono = "images/icono.ico"

# Tamaño de las ventanas en general
ventana_size = "500x500"

def validate_entry(text):
    if text.isdigit() or text == "":
        return True
    else:
        messagebox.showerror("Error", "Ingrese solo números")
        return False

def validate_on_focusout(event):
    text = entry_monto.get()
    if not text.isdigit() and text != "":
        messagebox.showerror("Error", "Ingrese solo números")

def abrir_ingresos():
    # Minizar la ventana principal
    ventana.iconify()
    # Crear ventana emergente para ingresos
    global ventana_ingresos
    ventana_ingresos = tk.Toplevel()
    screen_width = ventana_ingresos.winfo_screenwidth()
    screen_height = ventana_ingresos.winfo_screenheight()
    window_width = 500
    window_height = 500
    x = (screen_width // 2) - (window_width // 2)
    y = (screen_height // 2) - (window_height // 2)
    ventana_ingresos.geometry('{}x{}+{}+{}'.format(window_width, window_height, x, y))
    ventana_ingresos.config(bg='#9bfab0')
    ventana_ingresos.iconbitmap(icono)
    ventana_ingresos.grab_set()

    # Crear campo para ingresar el monto
    lbl_monto = tk.Label(ventana_ingresos, font=('Normographe', 11, 'bold'), text="Monto:", bg = "yellow")
    lbl_monto.pack(pady=5)
    global entry_monto
    entry_monto = tk.Entry(ventana_ingresos, validate="key")
    entry_monto['validatecommand'] = (entry_monto.register(validate_entry), '%S')
    entry_monto.pack(pady=5)
    entry_monto.bind("<FocusOut>", validate_on_focusout)

    # Crear calendario para seleccionar la fecha
    lbl_fecha = tk.Label(ventana_ingresos, font=('Normographe', 11, 'bold'), text="Fecha:", bg = "yellow")
    lbl_fecha.pack(pady=5)
    global cal_fecha
    cal_fecha = Calendar(ventana_ingresos)
    cal_fecha.pack(pady=5)

    # Crear botón de inicio en la ventana emergente
    btn_inicio = tk.Button(ventana_ingresos, text="Inicio", height=2, width=10, font=('Normographe', 11, 'bold'),
                           background="lightblue", command=cerrar_ingreso)
    btn_inicio.pack(pady=10)

    # Crear botón de guardar en la ventana emergente
    btn_guardar = tk.Button(ventana_ingresos, text="Guardar", height=2, width=10, font=('Normographe', 11, 'bold'),
                            background="lightblue", command=guardar_ingreso)
    btn_guardar.pack(pady=10)

def guardar_ingreso():    
    # Obtener los valores de los campos de entrada
    monto = entry_monto.get()
    # Comprobar si el campo de monto está vacío
    if not monto:
        messagebox.showerror("Error", "El campo de monto está vacío.")
        return
    fecha = cal_fecha.selection_get().strftime(date)
    c = conexion.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS movimientos
                 (monto REAL, fecha TEXT, categoria TEXT NULL, tipo TEXT)''')
    c.execute("INSERT INTO movimientos VALUES (?, ?, ' ', 'ingreso')", (monto, fecha))    
    conexion.commit()
    entry_monto.delete(0,tk.END)

def cerrar_ingreso():
    ventana_ingresos.destroy()
    ventana.deiconify()
    
def abrir_gastos():
    # Minizar la ventana principal
    ventana.iconify()
    # Crear ventana emergente para gastos
    global ventana_gastos
    ventana_gastos = tk.Toplevel()
    screen_width = ventana_gastos.winfo_screenwidth()
    screen_height = ventana_gastos.winfo_screenheight()
    window_width = 500
    window_height = 500
    x = (screen_width // 2) - (window_width // 2)
    y = (screen_height // 2) - (window_height // 2)
    ventana_gastos.geometry('{}x{}+{}+{}'.format(window_width, window_height, x, y))
    ventana_gastos.config(bg='#9bfab0')
    ventana_gastos.iconbitmap(icono)
    ventana_gastos.grab_set()
    
    # Crear campo para ingresar el monto
    lbl_monto = tk.Label(ventana_gastos, font=('Normographe', 11, 'bold'), text="Monto:", bg = "yellow")
    lbl_monto.pack(pady=5)
    global entry_monto
    entry_monto = tk.Entry(ventana_gastos, validate="key")
    entry_monto['validatecommand'] = (entry_monto.register(validate_entry), '%S')
    entry_monto.pack(pady=5)
    entry_monto.bind("<FocusOut>", validate_on_focusout)

    # Crear lista desplegable para seleccionar la categoría
    lbl_categoria = tk.Label(ventana_gastos, font=('Normographe', 11, 'bold'), text="Categoría:", bg = "yellow")
    lbl_categoria.pack(pady=5)
    categorias = ["Alimentación", "Transporte",
                  "Entretenimiento", "Salud", "Educación", "Otros"]
    global var_categoria
    var_categoria = tk.StringVar(value=categorias[0])
    combo_categoria = tk.OptionMenu(ventana_gastos, var_categoria, *categorias)
    combo_categoria.pack(pady=5)

    # Crear calendario para seleccionar la fecha
    lbl_fecha = tk.Label(ventana_gastos, font=('Normographe', 11, 'bold'), text="Fecha:", bg = "yellow")
    lbl_fecha.pack(pady=5)
    global cal_fecha
    cal_fecha = Calendar(ventana_gastos)
    cal_fecha.pack(pady=5)

    # Crear botón de inicio en la ventana emergente
    btn_inicio = tk.Button(ventana_gastos, text="Inicio", height=2, width=10, font=('Normographe', 11, 'bold'),
                           background="lightblue", command=cerrar_gasto)
    btn_inicio.pack(pady=10)

    # Crear botón de guardar en la ventana emergente
    btn_guardar = tk.Button(ventana_gastos, text="Guardar", height=2, width=10, font=('Normographe', 11, 'bold'),
                            background="lightblue", command=guardar_gasto)
    btn_guardar.pack(pady=10)

def guardar_gasto():
    # Obtener los valores de los campos de entrada
    monto = entry_monto.get()
    # Comprobar si el campo de monto está vacío
    if not monto:
        messagebox.showerror("Error", "El campo de monto está vacío.")
        return
    categoria = var_categoria.get()
    fecha = cal_fecha.selection_get().strftime(date)
    c = conexion.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS movimientos
                 (monto REAL, fecha TEXT, categoria TEXT NULL, tipo TEXT)''')
    c.execute("INSERT INTO movimientos VALUES (?, ?, ?, 'gasto')", (monto, fecha, categoria))
    conexion.commit()
    entry_monto.delete(0,tk.END)

def calcular_gastos():
    meses = {
    "Enero": 1,
    "Febrero": 2,
    "Marzo": 3,
    "Abril": 4,
    "Mayo": 5,
    "Junio": 6,
    "Julio": 7,
    "Agosto": 8,
    "Septiembre": 9,
    "Octubre": 10,
    "Noviembre": 11,
    "Diciembre": 12
    }
    # Obtener el mes y año seleccionados
    mes = meses[cbx_mes.get()]
    year = int(cbx_year.get())
    fecha_inicio = datetime.datetime(year, mes, 1).strftime(date)
    fecha_fin = datetime.datetime(year, mes +1, 1) - datetime.timedelta(days=1)
    fecha_fin = fecha_fin.strftime(date)
    
    # Consultar la tabla y filtrar por el período seleccionado
    df = pd.read_sql_query(f"SELECT * from movimientos WHERE fecha BETWEEN '{fecha_inicio}' AND '{fecha_fin}'", conexion)

    if df.empty:
        messagebox.showwarning("Datos inexistentes", "No existen datos para el período seleccionado")
    else:    
        # Calcular el total de gastos
        total_gastos = df[df["tipo"] == "gasto"]["monto"].sum()

        # Mostrar el total de gastos en un mensaje
        messagebox.showinfo("Total de gastos", f"El total de gastos en {cbx_mes.get()} - {cbx_year.get()} es de ${total_gastos}")

def cerrar_gasto():
    ventana_gastos.destroy()
    ventana.deiconify()
    
def abrir_resumen():
    # Minizar la ventana principal
    ventana.iconify()
    # Crear ventana emergente para resumen
    global ventana_resumen
    ventana_resumen = tk.Toplevel()
    screen_width = ventana_resumen.winfo_screenwidth()
    screen_height = ventana_resumen.winfo_screenheight()
    window_width = 500
    window_height = 500
    x = (screen_width // 2) - (window_width // 2)
    y = (screen_height // 2) - (window_height // 2)
    ventana_resumen.geometry('{}x{}+{}+{}'.format(window_width, window_height, x, y))
    ventana_resumen.config(bg='#9bfab0')
    ventana_resumen.iconbitmap(icono)
    ventana_resumen.grab_set()

    # Crear botón de inicio en la ventana emergente
    btn_inicio = tk.Button(ventana_resumen, text="Inicio", height=2, width=10, font=('Normographe', 11, 'bold'),
                            background="lightblue",command=cerrar_resumen)
    btn_inicio.pack(pady=10)

    # Crear sección para seleccionar mes y año
    frm_fecha = tk.Frame(ventana_resumen)
    frm_fecha.pack(pady=10)

    lbl_mes = tk.Label(frm_fecha, text="Mes:")
    lbl_mes.pack(side="left")

    global cbx_mes
    cbx_mes = ttk.Combobox(frm_fecha, values=["Enero", "Febrero", "Marzo", "Abril", "Mayo", "Junio", "Julio", "Agosto", "Septiembre", "Octubre", "Noviembre", "Diciembre"])
    cbx_mes.current(datetime.datetime.today().month - 1)
    cbx_mes.pack(side="left", padx=5)

    lbl_year = tk.Label(frm_fecha, text="Año:")
    lbl_year.pack(side="left")

    global cbx_year
    cbx_year = ttk.Combobox(frm_fecha, values=[str(year) for year in range(datetime.datetime.today().year, datetime.datetime.today().year - 10, -1)])
    cbx_year.current(0)
    cbx_year.pack(side="left", padx=5)

    btn_calcular = tk.Button(frm_fecha, text="Calcular", height=2, width=10, font=('Normographe', 11, 'bold'),
                            background="yellow",command=calcular_gastos)
    btn_calcular.pack(side="left")

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

def cerrar_resumen():
    ventana_resumen.destroy()
    ventana.deiconify()

# Función para cerrar la conexion a la base de datos y las ventanas
def cerrar():
    conexion.close()
    sys.exit(0)

# Crear ventana principal
ventana = tk.Tk()

# Establecer tamaño de ventana
screen_width = ventana.winfo_screenwidth()
screen_height = ventana.winfo_screenheight()
window_width = 500
window_height = 500
x = (screen_width // 2) - (window_width // 2)
y = (screen_height // 2) - (window_height // 2)
ventana.geometry('{}x{}+{}+{}'.format(window_width, window_height, x, y))

# Establecer el color de la ventana
ventana.config(bg = "lightblue")

# Establecer el titulo de la ventana
ventana.title("Ni un $inco")

# Imagen de fondo principal
imagen_fondo = Image.open("images/finanzas.jpg")
imagen_fondo = ImageTk.PhotoImage(imagen_fondo)

label_fondo = tk.Label(ventana, image=imagen_fondo)
label_fondo.place(x=0, y=0, relwidth=1, relheight=1)

# Crear botones del menú principal
btn_ingresos = tk.Button(ventana, text="Ingresos", height= 2, width = 10, font=('Normographe',11,'bold'),background= "palegreen",command=abrir_ingresos)
btn_gastos = tk.Button(ventana, text="Gastos", height= 2, width = 10, font=('Normographe',11,'bold'),background= "palegreen",command=abrir_gastos)
btn_resumen = tk.Button(ventana, text="Resumen", height= 2, width = 10,font=('Normographe',11,'bold'),background= "palegreen",command=abrir_resumen)
btn_salir = tk.Button(ventana, text="Salir", height= 2, width = 10, font=('Normographe',11,'bold'),background= "palegreen",command=cerrar)

# Posicionar botones en la ventana
btn_ingresos.place(x = 202, y = 200)
btn_gastos.place(x = 202, y = 270)
btn_resumen.place(x = 202, y = 340)
btn_salir.place(x = 202, y = 410)

# Imagen menú principal
image = Image.open('images/diner.png')
image = image.resize((220,150),Image.LANCZOS)

img = ImageTk.PhotoImage(image)
lbl_img = tk.Label(ventana,image=img)
lbl_img.place(x=140,y=25)

# Icono de la ventana
ventana.iconbitmap(icono)

# Ejecutar ventana
ventana.mainloop()
