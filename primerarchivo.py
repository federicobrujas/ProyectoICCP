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


#Funciones inicio de juego
def comenzarJuego():
    global nombre_jugador
    nombre_jugador = ingreso_nombre.get()
    etiqueta_intro.config(text = f"Bienvenido, {nombre_jugador}! La aventura comienza...")
    boton_inicio.destroy()
    boton_salir.pack()

def comienzoHistoria():
    boton_inicio.destroy()
    etiqueta_intro.destroy()
    etiqueta_nombre.destroy()
    ingreso_nombre.destroy()
    boton_salir.destroy()
    
    etiqueta_texto_inicial.pack()
    boton_buscar_en_la_habitacion.pack()
    boton_afrontar_la_puerta.pack()
    
    boton_salir.pack()
    
#Funciones de transcurso de la historia

def buscarEnLaHabitación():
    boton_buscar_en_la_habitacion.destroy()
    boton_afrontar_la_puerta.destroy()
    etiqueta_texto_inicial.destroy()
    
    etiqueta_texto_buscar_en_la_habitacion.pack()
    
    boton_inspeccionar_simbolos.pack()

def afrontarLaPuerta():
    boton_buscar_en_la_habitacion.destroy()
    boton_afrontar_la_puerta.destroy()
    etiqueta_texto_inicial.destroy()
    
    etiqueta_texto_afrontar_la_puerta.pack()
    
    boton_cruzar_el_puente.pack()
    boton_explorar_otro_camino.pack()
    
def cruzarElPuente():
    blabla
    
def explorarOtroCamino():
    blabla
    
def inspeccionarSimbolos():
    boton_inspeccionar_simbolos.destroy()
    
    
    
    
#Función terminar ejecución
def salirJuego():
    principal.destroy()

#Definición de botones para interacción
boton_inicio = tk.Button(principal, text = "Comenzar", command = comienzoHistoria)
boton_inicio.pack()
boton_salir = tk.Button(principal, text = "Salir", command = salirJuego)
boton_buscar_en_la_habitacion = tk.Button(principal, text = "Buscar en la habitación", command = buscarEnLaHabitación)
boton_afrontar_la_puerta = tk.Button(principal, text = "Afrontar la puerta", command = afrontarLaPuerta)
boton_cruzar_el_puente = tk.Button(principal, text = "Cruzar el puente", command = cruzarElPuente)
boton_explorar_otro_camino = tk.Button(principal, text = "Explorar otro camino", command = explorarOtroCamino)
boton_inspeccionar_simbolos = tk.Button(principal, text = "Inspeccionar los Símbolos en las Paredes", command = inspeccionarSimbolos)

#Textos
texto_inicial = (
        f"Tus ojos se abren de golpe, te encuentras en una habitación tenue con el sabor metálico del miedo en el aire.\n"
        f"El sudor frío recorre tu frente mientras te pones de pie, dándote cuenta de que estás solo.\n" 
        f"Las paredes están decoradas con símbolos extraños que parecen palpitar con una energía inquietante.\n" 
        f"Una puerta misteriosa te llama hacia la oscuridad que hay más allá.\n"
    )

texto_buscar_en_la_habitacion = (
        f"Mientras buscas, tu mano roza una nota arrugada en tu bolsillo.\n" 
        f"Dice: ""Navega el laberinto para encontrar la verdad"".\n" 
        f"Determinado, contemplas tu próximo movimiento.\n"
    )

texto_afrontar_la_puerta = (
    f"Decides proceder por la misteriosa puerta.\n" 
    f"El angosto corredor te lleva hacia un laberinto con pasajes enredados.\n" 
    f"Te enfrentas a tu primer desafío: un puente precario sobre un abismo aparentemente interminable.\n"
)

#Etiquetas de texto
etiqueta_texto_inicial = tk.Label(principal, text = texto_inicial)
etiqueta_texto_buscar_en_la_habitacion = tk.Label(principal, text = texto_buscar_en_la_habitacion)
etiqueta_texto_afrontar_la_puerta = tk.Label(principal, text = texto_afrontar_la_puerta)



#Loop principal
principal.mainloop()
