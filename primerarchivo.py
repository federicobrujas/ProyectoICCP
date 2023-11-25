import tkinter as tk

#Características generales del jugador
nombre_jugador = ""


# Inicialización de la ventana usando tkinter
principal = tk.Tk()
principal.title("Perdido en el Laberinto: Un Juego Simple Basado en Texto")

etiqueta = tk.Label(principal, text = "Hola Mundo")
etiqueta.pack(side = tk.BOTTOM)

#Introducción y configuración del jugador
etiqueta_intro = tk.Label(principal, text = "Bienvenido a Perdido en el Laberinto, ¿estás dispuesto a comenzar?")
etiqueta_intro.pack()

etiqueta_nombre = tk.Label(principal, text = "Ingresa tu nombre")
etiqueta_nombre.pack()

ingreso_nombre = tk.Entry(principal)
ingreso_nombre.pack()


#Función inicio de juego
def comenzarJuego ():
    global nombre_jugador
    nombre_jugador = ingreso_nombre.get()
    etiqueta_intro.config(text = f"Bienvenido, {nombre_jugador}! La aventura comienza...")
    boton_inicio.destroy()
    boton_salir.pack()

boton_inicio = tk.Button(principal, text = "Comenzar")
    


#Loop principal
principal.mainloop()
