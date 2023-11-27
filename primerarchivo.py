from tkinter import *
#Características generales del jugador
nombre_jugador = ""

# Inicialización de la ventana usando tkinter
principal = Tk()
principal.title("Perdido en el Laberinto: Un Juego Simple Basado en Texto")
principal.geometry("750x350")

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
    
    boton_explorar_camino_izquierda.pack()
    boton_explorar_camino_derecha.pack()
    
    

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
    boton_atravesar_puerta_que_se_cierra.pack()
    boton_encontrar_otra_salida.pack()


def memorizarMapaCruzarPuerta():
    etiqueta_texto_inspeccionar_simbolos.destroy()
    boton_arrancar_simbolos.destroy()
    boton_memorizar_mapa.destroy()

    etiqueta_texto_memorizar_mapa_cruzar_puerta.pack()
    boton_cruzar_el_puente.pack()
    boton_explorar_otro_camino.pack()


def atravesarPuertaQueSeCierra():
    etiqueta_texto_arrancar_simbolos.destroy()
    boton_atravesar_puerta_que_se_cierra.destroy()
    boton_encontrar_otra_salida.destroy()

    etiqueta_texto_atravesar_puerta_que_se_cierra.pack()
    
    boton_continuar_adelante.pack()
    boton_retroceder_replantear_estrategia.pack()
    
def explorarOtroCamino():
    boton_explorar_otro_camino.destroy()
    boton_explorar_otro_camino_1.destroy()
    boton_cruzar_el_puente.destroy()
    boton_seguir_cruzando_el_puente.destroy()
    etiqueta_texto_afrontar_la_puerta.destroy()
    etiqueta_texto_cruzar_el_puente.destroy()
     
    etiqueta_texto_explorar_otro_camino.pack()
    
    boton_investigar_caverna.pack()
    boton_ignorar_caverna.pack()
        

def encontrarOtraSalida():
    etiqueta_texto_arrancar_simbolos.destroy()
    boton_atravesar_puerta_que_se_cierra.destroy()
    boton_encontrar_otra_salida.destroy()
    
    etiqueta_texto_encontrar_otra_salida.pack()
    
    boton_continuar.pack()



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
boton_atravesar_puerta_que_se_cierra = Button(principal, text = "Atravesar rápidamente la puerta que se cierra", command = atravesarPuertaQueSeCierra)
boton_encontrar_otra_salida = Button(principal, text ="Buscar otra salida", command = encontrarOtraSalida)
boton_seguir_cruzando_el_puente = Button(principal, text ="Continuar cruzando el puente", command = seguirCruzandoElPuente)
boton_explorar_camino_izquierda = Button(principal, text = "Explorar el camino de la izquierda")
boton_explorar_camino_derecha = Button(principal, text = "Explorar el camino de la derecha")
boton_continuar_adelante = Button(principal, text = "Continuar adelante")
boton_retroceder_replantear_estrategia = Button(principal, text = "Retroceder y replantear tu estrategia")
boton_investigar_caverna = Button(principal, text = "Investigar la caverna")
boton_ignorar_caverna = Button(principal, text = "Ignorar la caverna y continuar por el camino")
boton_continuar = Button(principal, text = "Continuar")


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
texto_atravesar_puerta_que_se_cierra =(
        f"Corres hacia la puerta que se cierra, apenas logrando pasar antes de que se selle.\n"
        f"La habitación se transforma en un laberinto, ves cómo la forma del laberinto se transforma frente a tus ojos \n"
        f"de manera impredecible. Los símbolos rasgados en tus manos son ahora indescifrables.\n\n"
        f"Mientras avanzas, el laberinto se vuelve más traicionero. Las sombras parpadean y gruñidos distantes aseguran peligros acechando.\n"
        f"Tu decisión de arrancar los símbolos puede haber hecho que el laberinto sea aún más impredecible.\n"
)
texto_encontrar_otra_salida =(
        f"La puerta se cierra y la habitación comienza a temblar.\n"
        f"Desesperado buscas otra salida, pasas tu mirada por todos los rincones.\n"
        f"Eventualmente un punto oscuro llama tu atención, te diriges hacia este y descubres que es una entrada a un pasadizo por el que apenas cabes.\n"
)
texto_explorar_otro_camino =(
        f"Decides evitar el raquítico puente y buscar una ruta alterna, tomas un pasadizo cada vez más angosto,\n"
        f"te volteas pues el camino no te da confianza y descubres que el camino de vuelta está bloqueado, solo puedes seguir adelante.\n"
        f"Después de lo que parecen horas caminando, encuentras una entrada hacia lo que parece una caverna.\n"
)
texto_cruzar_el_puente =(
        f"Te acercas con cautela al precario puente, el eco de tus pasos se mezcla con el sonido espeluznante del\n"
         f"laberinto. Cuando subes a la primera tabla, ésta cruje siniestramente pero mantiene tu peso.\n"
)
texto_continuar_cruzando_el_puente =(
        f"Con pasos cuidadosos, navegas por el puente traicionero. El abismo de abajo parece interminable,\n"
        f"pero llegas ileso al otro lado. El laberinto se abre y te dirige al interior de una caverna que\n"
        f"es una cámara con múltiples caminos.\n\n"
        f"De repente escuchas lamentos y gritos de desesperación que parecen venir del camino de la izquierda.\n"
)

texto_rendir_ante_caida = (
    f"Estás de vuelta en el laberinto, esta vez la forma del laberinto se transforma frente a tus ojos de manera impredecible.\n"
    f"Los símbolos rasgados en tus manos son ahora indescifrables.\n\n"
    f"Mientras avanzas, el laberinto se vuelve más traicionero\n"
    f"Las sombras parpadean y gruñidos distantes aseguran peligros acechando.\n"
    f"Tu decisión de arrancar los símbolos puede haber hecho que el laberinto sea aún más impredecible.\n"
)

texto_continuar_adelante = (
    f"Con determinación, sigues adelante a través de los corredores siempre cambiantes del laberinto.\n"
    f"Los símbolos rasgados ofrecen poca orientación, y pronto te encuentras frente a una enorme puerta cerrada con llave.\n"
)

texto_retroceder_replantear_estrategia = (
    f"Al darte cuenta de que los símbolos rasgados son más un obstáculo que una ayuda,\n"
    f"retrocedes intentando volver sobre tus pasos.\n"
    f"Sin embargo, el laberinto parece tener una mente propia, reorganizándose como si se burlara de tus intentos de escapar.\n"
    
)

texto_explorar_camino_izquierda = (
    f"Te aventuras por el camino de la izquierda y te encuentras con un grupo de personas perdidas.\n"
    f"Algunos ofrecen valiosas ideas y comparten suministros.\n"
    f"Uno de ellos te entrega un mapa del laberinto, que revela atajos y peligros potenciales.\n"
)

texto_intentas_forzar_cerradura = (
    f"Tomas aire profundamente, acercándote a la imponente puerta.\n"
    f"La tenue luz proyecta sombras inquietantes a medida que manipulas el candado, intentando forzarlo desesperadamente.\n"
    f"Sin que te des cuenta, el sonido que haces en tu esfuerzo produce un eco en el laberinto\n"
    f"llamando la atención de los guardianes de este.\n\n"
    f"De repente la puerta se abre revelando un pasadizo angosto.\n"
    f"Sonríes triunfante, pero la sonrisa dura poco.\n"
    f"Los guardianes, unas criaturas grotescas con garras afiladas y ojos hambrientos emergen de las sombras.\n"
)

texto_buscas_refugio_esperas = (
    f"Encuentras una pequeña zanja donde apenas cabes, esta parece ser capaz de protegerte del caos de afuera.\n"
    f"El mundo comienza a temblar, es como un terremoto que jamás has sentido ni imaginado.\n"
    f"Eres incapaz de salir de donde estás y tu única esperanza es que ahí dentro estés seguro.\n"
    f"Después de lo que parece una eternidad el temblor cesa y sales de la zanja.\n"
    f"Ahora el laberinto parece estable y de hecho te parece familiar con lo que alcanzaste a ver del mapa.\n"
)

texto_investigas_mas = (
    f"Tus ojos se fijan en algo que parece producir un destello de luz rojo, y procedes a tomarlo con tus manos.\n"
    f"Entonces, el calor empieza a desaparecer y la habitación comienza a iluminarse.\n"
    f"Notas que tu visión estaba borrosa pero también notas, a medida que el mareo desaparece,\n" 
    f"que te encuentras en una cámara llena de artefactos\n"
)

#Etiquetas de texto
etiqueta_texto_inicial = Label(principal, text = texto_inicial)
etiqueta_texto_buscar_en_la_habitacion = Label(principal, text = texto_buscar_en_la_habitacion)
etiqueta_texto_afrontar_la_puerta = Label(principal, text = texto_afrontar_la_puerta)
etiqueta_texto_inspeccionar_simbolos = Label(principal, text = texto_inspeccionar_simbolos)
etiqueta_texto_arrancar_simbolos = Label(principal, text = texto_arrancar_simbolos)
etiqueta_texto_memorizar_mapa_cruzar_puerta = Label(principal, text =texto_memorizar_mapa_cruzar_puerta)
etiqueta_texto_encontrar_otra_salida = Label(principal, text = texto_encontrar_otra_salida)
etiqueta_texto_atravesar_puerta_que_se_cierra = Label(principal, text = texto_atravesar_puerta_que_se_cierra)
etiqueta_texto_cruzar_el_puente = Label(principal, text =texto_cruzar_el_puente)
etiqueta_texto_continuar_cruzando_el_puente = Label(principal, text = texto_continuar_cruzando_el_puente)
etiqueta_texto_explorar_otro_camino = Label(principal, text = texto_explorar_otro_camino)
etiqueta_texto_rendir_ante_caida = Label(principal, text = texto_rendir_ante_caida)
etiqueta_texto_continuar_adelante = Label(principal, text = texto_continuar_adelante)
etiqueta_texto_retroceder_replantear_estrategia = Label(principal, text = texto_retroceder_replantear_estrategia)
etiqueta_texto_explorar_camino_izquierda = Label(principal, text = texto_explorar_camino_izquierda)
etiqueta_texto_intentas_forzar_cerradura = Label(principal, text = texto_intentas_forzar_cerradura)
etiqueta_texto_buscas_refugio_esperas = Label(principal, text = texto_buscas_refugio_esperas)
etiqueta_texto_investigas_mas = Label (principal, text = texto_investigas_mas)

#Loop principal
principal.mainloop()
