import tkinter as tk
from tkinter import ttk
from tkcalendar import Calendar
import json
from datetime import datetime
import os

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

    # Crear lista desplegable para seleccionar la categoría
    lbl_categoria = tk.Label(ventana_ingresos, text="Categoria:")
    lbl_categoria.pack(pady=5)
    categorias = ["Alimentacion", "Transporte",
                  "Entretenimiento", "Salud", "Educacion", "Otros"]
    global var_categoria
    var_categoria = tk.StringVar(value=categorias[0])
    combo_categoria = tk.OptionMenu(
        ventana_ingresos, var_categoria, *categorias)
    combo_categoria.pack(pady=5)

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


def validar_numero(valor):
    # Función para validar que el campo solo contenga números
    if valor.isnumeric() or valor == "":
        return True
    else:
        return False


def guardar_ingreso():
    # Obtener los valores de los campos de entrada
    monto = entry_monto.get()
    categoria = var_categoria.get()
    fecha = cal_fecha.selection_get().strftime('%d-%m-%Y')

    # Crear un diccionario con los valores
    ingreso = {
        "monto": monto,
        "categoria": categoria,
        "fecha": fecha
    }

    # Colocar una condición en caso de que ya exista el archivo
    archivoJ = "ingresos.json"
    if os.path.exists(archivoJ):
        # Cargar el archivo JSON existente
        with open("ingresos.json", "r") as f:
            data = json.load(f)

            # Agregar el nuevo ingreso al archivo
            data.append(ingreso)

        # Guardar los datos actualizados en el archivo
        with open("ingresos.json", "w") as f:
            json.dump(data, f)

    else:
        # Escribir el diccionario en un archivo JSON
        with open("ingresos.json", "w") as file:
            json.dump(ingreso, file)
    '''
    # Cerrar la ventana de ingresos
    ventana_ingresos.destroy()
    '''
    


def abrir_gastos():
    # Crear ventana emergente para gastos
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
    btn_inicio = tk.Button(ventana_gastos, text="Inicio",
                           command=ventana_gastos.destroy)
    btn_inicio.pack(pady=10)


def abrir_resumen():
    # Crear ventana emergente para resumen
    ventana_resumen = tk.Toplevel()
    ventana_resumen.geometry("500x500")
    # Crear botón de inicio en la ventana emergente
    btn_inicio = tk.Button(ventana_resumen, text="Inicio",
                           command=ventana_resumen.destroy)
    btn_inicio.pack(pady=10)


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

# Ejecutar ventana
ventana.mainloop()
