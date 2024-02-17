import tkinter as tk
from tkinter import *

root = tk.Tk()

# Marco 1
marco_principal = Frame()
marco_principal.grid(row=0, column=0)
marco_principal.config(width="100", height="100")
marco_principal.config(bg="red")

# Marco 2
marco_principal2 = Frame()
marco_principal2.grid(row=1, column=0)
marco_principal2.config(width="100", height="100")
marco_principal2.config(bg="blue")

# Marco 3
marco_principal3 = Frame()
marco_principal3.grid(row=2, column=0)
marco_principal3.config(width="100", height="100")
marco_principal3.config(bg="yellow")

# Marco 4
marco_principal4 = Frame()
marco_principal4.grid(row=0, column=1)
marco_principal4.config(width="100", height="100")
marco_principal4.config(bg="yellow")

# Marco 5
marco_principal5 = Frame()
marco_principal5.grid(row=1, column=1)
marco_principal5.config(width="100", height="100")
marco_principal5.config(bg="red")

# Marco 6
marco_principal6 = Frame()
marco_principal6.grid(row=2, column=1)
marco_principal6.config(width="100", height="100")
marco_principal6.config(bg="blue")

root.mainloop()