# importaciones
import tkinter as tk
from tkinter import Button, END, messagebox, ttk
from tkcalendar import Calendar
import pandas as pd

# Listas en vacío
listamonto = []
categoriaG = []
fecha = []

# Constante para evitar repetir la misma cadena
exito = "Exito!"
error = "Error!"

# Funciones que se ejecutan al hacer clic en los botones del menú principal
def abrir_ingresos():
    # Crear ventana emergente para ingresos
    ventana_ingresos = tk.Toplevel()
    ventana_ingresos.geometry("500x500")

    def insertar_ingresos():
        global listamonto
        global fecha

        fecha_i = cal_fecha.get()
        monto_i = ingresa_monto.get()

        if monto_i.isdigit(): # Sólo acepta dígitos
            listamonto.append(monto_i)
            fecha.append(fecha_i)
            messagebox.showinfo(exito, "Datos guardados correctamente")
            ingresa_monto.delete(0, END)
            cal_fecha.delete(0, END)


        else:
            messagebox.showerror(error, "Debes introducir únicamente números en los campos")

    def guardar_ingresos():
        global listamonto

        datos = {'Montos': listamonto, 'Fecha': fecha}
        nom_excel = str("ingresos.csv")
        df = pd.DataFrame(datos, columns=['Montos', 'Fecha'])
        df.to_csv(nom_excel)
        messagebox.showinfo(exito, "Archivo guardado correctamente")

    # Agregar campo para rellenar únicamente con números
    lbl_monto = tk.Label(ventana_ingresos, text="Monto de ingresos:")
    lbl_monto.pack(pady=5)
    ingresa_monto = tk.Entry(ventana_ingresos, width = 8)
    ingresa_monto.pack(pady = 5)

    # Entradas de montos con botones para agregar y guardar
    agregar = Button(ventana_ingresos, width=20, font=('Courier', 16, 'bold'), text='Agregar', bg='#fadf9b', bd=5,
                     command=insertar_ingresos)
    agregar.pack(pady = 5)

    guardar = Button(ventana_ingresos, width=10, font=('Courier', 16, 'bold'), text='Guardar', bg='red', bd=5,
                     command=guardar_ingresos)
    guardar.pack(pady = 5)

    # Agregar calendario para seleccionar una fecha
    lbl_fecha = tk.Label(ventana_ingresos, text="Fecha:")
    lbl_fecha.pack(pady=5)
    cal_fecha = Calendar(ventana_ingresos, selectmode="day", date_pattern="yyyy-mm-dd")
    cal_fecha.pack(pady=5)

    # Crear botón de inicio en la ventana emergente
    btn_inicio = tk.Button(ventana_ingresos, text="Inicio", command=ventana_ingresos.destroy)
    btn_inicio.pack(pady=10)


def validar_numero(valor):
    # Función para validar que el campo solo contenga números
    if valor.isnumeric() or valor == "":
        return True
    else:
        return False

def abrir_gastos():
    # Crear ventana emergente para gastos
    ventana_gastos = tk.Toplevel()
    ventana_gastos.geometry("500x500")

    def insertar_gastos():
        global listamonto
        global fecha
        global categoriaG

        gastos = ingresa_montoG.get()
        fecha_G = cal_fecha.get()
        categoria_G = cmb_categoria.get()

        if gastos.isdigit():
            listamonto.append(gastos)
            fecha.append(fecha_G)
            categoriaG.append(categoria_G)

            messagebox.showinfo(exito, "Datos guardados correctamente")
            ingresa_montoG.delete(0, END)
            cal_fecha.delete(0, END)


        else:
            messagebox.showerror("Error", "Debes introducir únicamente números en los campos")

    def guardar_gastos():
        global listamonto

        datos = {'Montos': listamonto, 'Fecha': fecha, 'Categoría': categoriaG}
        nom_excel = str("Gastos.csv")
        df = pd.DataFrame(datos, columns=['Montos'])
        df.to_csv(nom_excel)
        messagebox.showinfo("Exito", "Archivo guardado correctamente")


    # Agregar campo para rellenar únicamente con números
    lbl_monto = tk.Label(ventana_gastos, text="Monto de gastos:")
    lbl_monto.pack(pady=5)
    ingresa_montoG = tk.Entry(ventana_gastos, width=8)
    ingresa_montoG.pack(pady=5)

    # Entradas de montos con botones para agregar y guardar
    agregar = Button(ventana_gastos, width=20, font=('Courier', 16, 'bold'), text='Agregar', bg='#fadf9b', bd=5,
                         command=insertar_gastos)
    agregar.pack(pady=5)

    guardar = Button(ventana_gastos, width=10, font=('Courier', 16, 'bold'), text='Guardar', bg='red', bd=5,
                         command=guardar_gastos)
    guardar.pack(pady=5)

    # Crear botón de inicio en la ventana emergente
    btn_inicio = tk.Button(ventana_gastos, text="Inicio", command=ventana_gastos.destroy)
    btn_inicio.pack(pady=10)
    # Agregar lista desplegable con diferentes categorías
    lbl_categoria = tk.Label(ventana_gastos, text="Categoría:")
    lbl_categoria.pack(pady=5)
    opciones_categoria = ["Alimentación", "Servicios", "Hogar", "Salud", "Transporte", "Otros"]
    cmb_categoria = ttk.Combobox(ventana_gastos, values=opciones_categoria)
    cmb_categoria.pack(pady=5)

    # Agregar calendario para seleccionar una fecha
    lbl_fecha = tk.Label(ventana_gastos, text="Fecha:")
    lbl_fecha.pack(pady=5)
    cal_fecha = Calendar(ventana_gastos, selectmode="day", date_pattern="yyyy-mm-dd")
    cal_fecha.pack(pady=5)


def abrir_resumen():
    # Crear ventana emergente para resumen
    ventana_resumen = tk.Toplevel()
    ventana_resumen.geometry("500x500")
    # Crear botón de inicio en la ventana emergente
    btn_inicio = tk.Button(ventana_resumen, text="Inicio", command=ventana_resumen.destroy)
    btn_inicio.pack(pady=10)


print(listamonto)

# Crear ventana principal
ventana = tk.Tk()

# Establecer tamaño de ventana
ventana.geometry("500x500")

# Crear botones del menú principal
btn_ingresos = tk.Button(ventana, text="Ingresos", command=abrir_ingresos)
btn_gastos = tk.Button(ventana, text="Gastos", command=abrir_gastos)
btn_resumen = tk.Button(ventana, text="Resumen", command=abrir_resumen)

# Posicionar botones en la ventana
btn_ingresos.pack(pady=10)
btn_gastos.pack(pady=10)
btn_resumen.pack(pady=10)

ventana.mainloop()