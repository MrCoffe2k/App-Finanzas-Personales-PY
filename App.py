import tkinter as tk

# Funciones que se ejecutan al hacer clic en los botones
def ingresos():
    print("Ingresos")

def gastos():
    print("Gastos")

def resumen():
    print("Resumen")

# Crear ventana
ventana = tk.Tk()

# Crear botones
btn_ingresos = tk.Button(ventana, text="Ingresos", command=ingresos)
btn_gastos = tk.Button(ventana, text="Gastos", command=gastos)
btn_resumen = tk.Button(ventana, text="Resumen", command=resumen)

# Posicionar botones en la ventana
btn_ingresos.pack()
btn_gastos.pack()
btn_resumen.pack()

# Ejecutar ventana
ventana.mainloop()