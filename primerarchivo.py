import tkinter as tk

#Características generales del jugador
nombre_jugador = ""


# Inicialización de la ventana usando tkinter
principal = tk.Tk()
principal.title("Perdido en el Laberinto: Un Juego Simple Basado en Texto")

#Introducción y configuración del jugador
etiqueta_intro = tk.Label(principal, text = "Bienvenido a Perdido en el Laberinto, ¿estás dispuesto a comenzar?\n")
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
boton_inicio.pack()

#Botón salir
def salirJuego():
    principal.destroy()
    
boton_salir = tk.Button(principal, text = "Salir", command = salir_juego)
boton_salir.pack()
    


#Loop principal
principal.mainloop()
