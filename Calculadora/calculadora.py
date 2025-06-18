from tkinter import *
from tkinter import PhotoImage
from tkinter import ttk

# Crear ventana principal
calc_window = Tk()
calc_window.title("Calculadora")
calc_window.config(bg="#f7d4f4")

calc_window.geometry("250x500")
# calc_window.minsize(100, 250)
# calc_window.maxsize(800, 1200)

# Crear icono para la app
icono = PhotoImage(file="4757105.png")
# iconphoto = multiplataforma, iconbitmap = windows
calc_window.iconphoto(True, icono)


# Crear grid de filas y columnas
for i in range(5):
    calc_window.grid_rowconfigure(i, weight=1)
for i in range(4):
    calc_window.grid_columnconfigure(i, weight=1)

# Crear visor
textoVisor = StringVar()
style = ttk.Style()
style.configure("Modern",
                borderwidth=1,
                insertwidth=4,
                fieldbackground="#957397",
                relief="flat")

visor = ttk.Entry(calc_window,
                  style="Modern",
                  textvariable=textoVisor,
                  font=("Helvetica", 20),
                  width=14, # Cuántos caracteres puede mostrar
                  justify="right")

visor.pack(pady=20, padx=20)

visor.grid(row=0,
           column=0,
           columnspan=4)

# Crear botones


# Ejecutar aplicación
calc_window.mainloop()

