#Creado desde terminal
import tkinter as tk

def pruebas(nombre, apellidos, pais):
    return f"Hola {nombre} {apellidos} veo que eres de {pais}"

window = tk.Tk()

window.geometry("700x500")

text = tk.Label(window, text = "Bienvenido a mi programa")

text.config(
    fg="white",
    bg="#000",
    padx=120,
    pady=20,
    font=("Consolas", 30)
)

text.pack()


text = tk.Label(window, text = "Soy Mike")


text.config(
    height=3,
    justify=tk.RIGHT,
    fg="white",
    bg="#567",
    padx=20,
    pady=20,
    font=("Consolas", 15),
    cursor="circle"
)

text.pack(
    anchor=tk.W,
)

text = tk.Label(window, text = pruebas(pais="México",apellidos="Castañeda",nombre ="MIke"))


text.config(
    height=3,
    justify=tk.LEFT,
    fg="white",
    bg="#900",
    padx=20,
    pady=20,
    font=("Consolas", 15),
    cursor="spider"
)

text.pack(
    anchor=tk.E,
)

window.mainloop()