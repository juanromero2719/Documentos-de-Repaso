import tkinter as tk
from tkinter import *

# Llamado a la clase Tk

root = tk.Tk()

# Titulo de la ventana
root.title("Mi primera ventana")

# Crea un label

etiqueta = Label(root, text="Hola Mundo")

# Empaqueta (Muestra el widget)

etiqueta.pack()

# Refresca la ventana hasta el infinito
root.mainloop()