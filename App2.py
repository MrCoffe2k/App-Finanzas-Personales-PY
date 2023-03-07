import tkinter as tk
from tkinter import ttk
from tkcalendar import Calendar

# Funciones que se ejecutan al hacer clic en los botones del menú principal
def abrir_ingresos():
    # Crear ventana emergente para ingresos
    ventana_ingresos = tk.Toplevel()
    ventana_ingresos.geometry("500x500")

    # Agregar campo para rellenar únicamente con números
    lbl_monto = tk.Label(ventana_ingresos, text="Monto:")
    lbl_monto.pack(pady=5)
    var_monto = tk.StringVar()
    ent_monto = tk.Entry(ventana_ingresos, textvariable=var_monto)
    ent_monto.pack(pady=5)
    ent_monto.config(validate="key", validatecommand=(ventana_ingresos.register(validar_numero), "%P"))

    # Agregar lista desplegable con diferentes categorías
    lbl_categoria = tk.Label(ventana_ingresos, text="Categoría:")
    lbl_categoria.pack(pady=5)
    opciones_categoria = ["Comida", "Electronica", "Hogar"]
    cmb_categoria = ttk.Combobox(ventana_ingresos, values=opciones_categoria)
    cmb_categoria.pack(pady=5)

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
    # Crear botón de inicio en la ventana emergente
    btn_inicio = tk.Button(ventana_gastos, text="Inicio", command=ventana_gastos.destroy)
    btn_inicio.pack(pady=10)

def abrir_resumen():
    # Crear ventana emergente para resumen
    ventana_resumen = tk.Toplevel()
    ventana_resumen.geometry("500x500")
    # Crear botón de inicio en la ventana emergente
    btn_inicio = tk.Button(ventana_resumen, text="Inicio", command=ventana_resumen.destroy)
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
