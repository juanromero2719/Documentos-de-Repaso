import tkinter as tk
from tkinter import *

root = tk.Tk()

def click_boton():
    texto = Label(root, text="Has hecho click en el boton").grid(row=1, column=0)

# Creamos un boton con un texto dentro

button = Button(root, text="Click me!", padx=100, pady=20, command=click_boton).grid(row=0, column=0)

# el atributo comand llama y ejecuta la funcion

print(button)

root.mainloop()