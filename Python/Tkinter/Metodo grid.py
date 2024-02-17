import tkinter as tk
from tkinter import *

root = tk.Tk()

# Etiqueta (Muestra un texto)

etiqueta = Label(root, text="Hola Mundo")
etiqueta2 = Label(root, text="Hola Mundo 2")
etiqueta.grid(row=2, column=0)
etiqueta2.grid(row=0, column=0)

# Tamaño de ancho y largo de la ventana

marco_principal = Frame()

# Empaquetar el marco

marco_principal.grid(row=1, column=0)

marco_principal.config(width="500", height="400")

# Color de fondo

marco_principal.config(bg="lightblue")

root.mainloop()