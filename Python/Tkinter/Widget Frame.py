import tkinter as tk
from tkinter import *

root = tk.Tk()

# En el metodo pack creas primero el frame y el label para acontinuacion empaquetarlos

marco_principal = Frame()

marco_principal.pack()

# Tamaño de ancho y largo de la ventana

marco_principal.config(width="500", height="400")

# Color de fondo

marco_principal.config(bg="lightblue")

root.mainloop()