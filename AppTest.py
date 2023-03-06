import tkinter as tk

# Funciones que se ejecutan al hacer clic en los botones del menú principal
def abrir_ingresos():
    # Crear ventana emergente para ingresos
    ventana_ingresos = tk.Toplevel()
    ventana_ingresos.geometry("300x200")
    # Crear botón de inicio en la ventana emergente
    btn_inicio = tk.Button(ventana_ingresos, text="Inicio", command=ventana_ingresos.destroy)
    btn_inicio.pack(pady=10)
    
def abrir_gastos():
    # Crear ventana emergente para gastos
    ventana_gastos = tk.Toplevel()
    ventana_gastos.geometry("300x200")
    # Crear botón de inicio en la ventana emergente
    btn_inicio = tk.Button(ventana_gastos, text="Inicio", command=ventana_gastos.destroy)
    btn_inicio.pack(pady=10)

def abrir_resumen():
    # Crear ventana emergente para resumen
    ventana_resumen = tk.Toplevel()
    ventana_resumen.geometry("300x200")
    # Crear botón de inicio en la ventana emergente
    btn_inicio = tk.Button(ventana_resumen, text="Inicio", command=ventana_resumen.destroy)
    btn_inicio.pack(pady=10)

# Crear ventana principal
ventana = tk.Tk()

# Establecer tamaño de ventana
ventana.geometry("500x700")

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