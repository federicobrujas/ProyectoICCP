from tkinter import *
#Características generales del jugador
nombre_jugador = ""

# Inicialización de la ventana usando tkinter
principal = Tk()
principal.title("Perdido en el Laberinto: Un Juego Simple Basado en Texto")
principal.geometry("550x350")

#Introducción y configuración del jugador
etiqueta_intro = Label(principal, text = "Bienvenido a Perdido en el Laberinto, ¿estás dispuesto a comenzar?\n")
etiqueta_intro.pack()


etiqueta_nombre = Label(principal, text = "Ingresa tu nombre")
etiqueta_nombre.pack()

ingreso_nombre = Entry(principal)
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
    #boton_afrontar_la_puerta.destroy()
    etiqueta_texto_inicial.destroy()
    
    etiqueta_texto_buscar_en_la_habitacion.pack()
    
    boton_inspeccionar_simbolos.pack()
    boton_afrontar_la_puerta.place(x=200,y=100)

def afrontarLaPuerta():
    boton_inspeccionar_simbolos.destroy()
    etiqueta_texto_buscar_en_la_habitacion.destroy()
    boton_buscar_en_la_habitacion.destroy()
    boton_afrontar_la_puerta.destroy()
    etiqueta_texto_inicial.destroy()
    
    etiqueta_texto_afrontar_la_puerta.pack()
    
    boton_cruzar_el_puente.pack()
    boton_explorar_otro_camino.pack()
    
def cruzarElPuente():
    boton_cruzar_el_puente.destroy()
    boton_explorar_otro_camino.destroy()
    etiqueta_texto_memorizar_mapa_cruzar_puerta.destroy()
    etiqueta_texto_afrontar_la_puerta.destroy()
    boton_cruzar_el_puente.destroy()
    boton_explorar_otro_camino.destroy()

    etiqueta_texto_cruzar_el_puente.pack()
    boton_explorar_otro_camino_1.pack()
    boton_seguir_cruzando_el_puente.pack()

def seguirCruzandoElPuente():
    etiqueta_texto_cruzar_el_puente.destroy()
    boton_explorar_otro_camino_1.destroy()
    boton_seguir_cruzando_el_puente.destroy()

    etiqueta_texto_continuar_cruzando_el_puente.pack()

def explorarOtroCamino():
    boton_cruzar_el_puente.destroy()
    boton_explorar_otro_camino.destroy()
    etiqueta_texto_memorizar_mapa_cruzar_puerta.destroy()
    boton_cruzar_el_puente.destroy()
    boton_explorar_otro_camino.destroy()
    
def inspeccionarSimbolos():
    boton_inspeccionar_simbolos.destroy()
    etiqueta_texto_buscar_en_la_habitacion.destroy()
    boton_afrontar_la_puerta.destroy()
    
    etiqueta_texto_inspeccionar_simbolos.pack()
    boton_arrancar_simbolos.pack()
    boton_memorizar_mapa.pack()

def arrancarSimbolos():
    etiqueta_texto_inspeccionar_simbolos.destroy()
    boton_arrancar_simbolos.destroy()
    boton_memorizar_mapa.destroy()

    etiqueta_texto_arrancar_simbolos.pack()
    boton_atravezar_puerta_que_se_cierra.pack()
    boton_buscar_otra_salida.pack()


def memorizarMapaCruzarPuerta():
    etiqueta_texto_inspeccionar_simbolos.destroy()
    boton_arrancar_simbolos.destroy()
    boton_memorizar_mapa.destroy()

    etiqueta_texto_memorizar_mapa_cruzar_puerta.pack()
    boton_cruzar_el_puente.pack()
    boton_explorar_otro_camino.pack()


def atravesarPuertaQueSeCierra():
    etiqueta_texto_arrancar_simbolos.destroy()
    boton_atravezar_puerta_que_se_cierra.destroy()
    boton_buscar_otra_salida.destroy()

    etiqueta_texto_atravezar_puerta_que_se_cierra()
    

def buscarOtraSalida50():
    etiqueta_texto_arrancar_simbolos.destroy()
    boton_atravezar_puerta_que_se_cierra.destroy()
    boton_buscar_otra_salida.destroy()



#Función terminar ejecución
def salirJuego():
    principal.destroy()

#Definición de botones para interacción
boton_inicio = Button(principal, text = "Comenzar", command = comienzoHistoria)
boton_inicio.pack()
boton_salir = Button(principal, text = "Salir", command = salirJuego)
boton_buscar_en_la_habitacion = Button(principal, text = "Buscar en la habitación", command = buscarEnLaHabitación)
boton_afrontar_la_puerta = Button(principal, text = "Afrontar la puerta", command = afrontarLaPuerta)
boton_cruzar_el_puente = Button(principal, text = "Cruzar el puente", command = cruzarElPuente)
boton_explorar_otro_camino = Button(principal, text = "Explorar otro camino", command = explorarOtroCamino)
boton_explorar_otro_camino_1 = Button(principal, text = "Explorar otro camino", command = explorarOtroCamino)
boton_inspeccionar_simbolos = Button(principal, text = "Inspeccionar los Símbolos en las Paredes", command = inspeccionarSimbolos)
boton_arrancar_simbolos = Button(principal, text = "Arrancar los símbolos y conservarlos", command = arrancarSimbolos)
boton_memorizar_mapa = Button(principal, text = "Memorizar el mapa y avanzar por la puerta", command = memorizarMapaCruzarPuerta)
boton_atravezar_puerta_que_se_cierra = Button(principal, text = "Atravesar rápidamente la puerta que se cierra", command = atravesarPuertaQueSeCierra)
boton_buscar_otra_salida = Button(principal, text ="Buscar otra salida", command = buscarOtraSalida50)
boton_seguir_cruzando_el_puente = Button(principal, text ="Continuar cruzando el puente", command = seguirCruzandoElPuente)


# Textos
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

texto_inspeccionar_simbolos = (
        f"Los símbolos en las paredes parecen formar un mapa rudimentario del laberinto, y descifras un mensaje:\n" 
        f"'Cuidado con las criaturas, no confíes en nadie'\n"
        f"Armado con esta advertencia, te preparas para el viaje que tienes por delante.\n"
)
texto_memorizar_mapa_cruzar_puerta = (
        f"Entras en el laberinto, entre sus giros y vueltas retumban sonidos escalofriantes.\n"
        f"Criaturas acechan en las sombras, y te enfrentas a tu primer desafío:\n"
        f"Un puente precario sobre un abismo aparentemente interminable.\n "
        f"Cierras los ojos e intentas recordar el mapa que intentaste memorizar,\n"
        f"hay algo en ese puente que te dice que debes cruzarlo\n"
)
texto_arrancar_simbolos = (
        f"Con urgencia, arrancas los símbolos de las paredes, pensando que podrían ser cruciales para tu supervivencia.\n "
        f"Sin embargo, al guardarlos apresuradamente en tus bolsillos, un ruido abominable resuena en la habitación. \n"
        f"Las paredes parecen temblar, y la puerta de salida comienza a cerrarse.\n"
)
texto_atravezar_puerta_que_se_cierra =(
        f"Corres hacia la puerta que se cierra, apenas logrando pasar antes de que se selle.\n"
        f"La habitación se transforma en un laberinto, ves cómo la forma del laberinto se transforma frente a tus ojos \n"
        f"de manera impredecible. Los símbolos rasgados en tus manos son ahora indescifrables.\n"
)
texto_buscar_otra_salida50 =(
        f"pag 50\n"
)
texto_explorar_otro_camino =(
        f"h"
)
texto_cruzar_el_puente =(
        f"Te acercas con cautela al precario puente, el eco de tus pasos se mezcla con el sonido espeluznante del\n"
         f"laberinto. Cuando subes a la primera tabla, ésta cruje siniestramente pero mantiene tu peso.\n"
)
texto_continuar_cruzando_el_puente =(
        f"Con pasos cuidadosos, navegas por el puente traicionero. El abismo de abajo parece interminable,\n"
        f"pero llegas ileso al otro lado. El laberinto se abre y te dirige al interior de una caverna que\n"
        f"es una camara con múltiples caminos.\n"
)


#Etiquetas de texto
etiqueta_texto_inicial = Label(principal, text = texto_inicial)
etiqueta_texto_buscar_en_la_habitacion = Label(principal, text = texto_buscar_en_la_habitacion)
etiqueta_texto_afrontar_la_puerta = Label(principal, text = texto_afrontar_la_puerta)
etiqueta_texto_inspeccionar_simbolos = Label(principal, text = texto_inspeccionar_simbolos)
etiqueta_texto_arrancar_simbolos = Label(principal, text = texto_arrancar_simbolos)
etiqueta_texto_memorizar_mapa_cruzar_puerta = Label(principal, text =texto_memorizar_mapa_cruzar_puerta)
etiqueta_texto_buscar_otra_salida50 = Label(principal, text = texto_buscar_otra_salida50)
etiqueta_texto_atravezar_puerta_que_se_cierra = Label(principal, text = texto_atravezar_puerta_que_se_cierra)
etiqueta_texto_cruzar_el_puente = Label(principal, text =texto_cruzar_el_puente)
etiqueta_texto_continuar_cruzando_el_puente = Label(principal, text = texto_continuar_cruzando_el_puente)

#Loop principal
principal.mainloop()
