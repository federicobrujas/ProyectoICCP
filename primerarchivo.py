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

def buscarEnLaHabitación(): #Página 4
    boton_buscar_en_la_habitacion.destroy()
    #boton_afrontar_la_puerta.destroy()
    etiqueta_texto_inicial.destroy()
    
    etiqueta_texto_buscar_en_la_habitacion.pack()
    
    boton_inspeccionar_simbolos.pack()
    boton_afrontar_la_puerta.place(x=200,y=100)

def afrontarLaPuerta(): #Página 6
    boton_inspeccionar_simbolos.destroy()
    etiqueta_texto_buscar_en_la_habitacion.destroy()
    boton_buscar_en_la_habitacion.destroy()
    boton_afrontar_la_puerta.destroy()
    etiqueta_texto_inicial.destroy()
    
    etiqueta_texto_afrontar_la_puerta.pack()
    
    boton_cruzar_el_puente.pack()
    boton_explorar_otro_camino.pack()
    
def inspeccionarSimbolos(): #Página 8
    boton_inspeccionar_simbolos.destroy()
    etiqueta_texto_buscar_en_la_habitacion.destroy()
    boton_afrontar_la_puerta.destroy()
    
    etiqueta_texto_inspeccionar_simbolos.pack()
    boton_arrancar_simbolos.pack()
    boton_memorizar_mapa.pack()    
    
def memorizarMapaCruzarPuerta(): #Página 12
    etiqueta_texto_inspeccionar_simbolos.destroy()
    boton_arrancar_simbolos.destroy()
    boton_memorizar_mapa.destroy()

    etiqueta_texto_memorizar_mapa_cruzar_puerta.pack()
    boton_cruzar_el_puente.pack()
    boton_explorar_otro_camino.pack()    
    
def arrancarSimbolos(): #Página 14
    etiqueta_texto_inspeccionar_simbolos.destroy()
    boton_arrancar_simbolos.destroy()
    boton_memorizar_mapa.destroy()

    etiqueta_texto_arrancar_simbolos.pack()
    boton_atravesar_puerta_que_se_cierra.pack()
    boton_encontrar_otra_salida.pack()
        
def cruzarElPuente():#Página 18
    boton_cruzar_el_puente.destroy()
    boton_explorar_otro_camino.destroy()
    etiqueta_texto_memorizar_mapa_cruzar_puerta.destroy()
    etiqueta_texto_afrontar_la_puerta.destroy()
    boton_cruzar_el_puente.destroy()
    boton_explorar_otro_camino.destroy()

    etiqueta_texto_cruzar_el_puente.pack()
    boton_explorar_otro_camino_1.pack()
    boton_seguir_cruzando_el_puente.pack()
    
def atravesarPuertaQueSeCierra(): #Página 22
    etiqueta_texto_arrancar_simbolos.destroy()
    boton_atravesar_puerta_que_se_cierra.destroy()
    boton_encontrar_otra_salida.destroy()

    etiqueta_texto_atravesar_puerta_que_se_cierra.pack()
    
    boton_continuar_adelante.pack()
    boton_retroceder_replantear_estrategia.pack()    

def seguirCruzandoElPuente(): #Página 23
    etiqueta_texto_cruzar_el_puente.destroy()
    boton_explorar_otro_camino_1.destroy()
    boton_seguir_cruzando_el_puente.destroy()

    etiqueta_texto_continuar_cruzando_el_puente.pack()
    
    boton_explorar_camino_izquierda.pack()
    boton_explorar_camino_derecha.pack()

def explorarOtroCamino(): #Página 24
    boton_explorar_otro_camino.destroy()
    boton_explorar_otro_camino_1.destroy()
    boton_cruzar_el_puente.destroy()
    boton_seguir_cruzando_el_puente.destroy()
    etiqueta_texto_afrontar_la_puerta.destroy()
    etiqueta_texto_cruzar_el_puente.destroy()
     
    etiqueta_texto_explorar_otro_camino.pack()
    
    boton_investigar_caverna.pack()
    boton_ignorar_caverna.pack()
        

def encontrarOtraSalida(): #Página 25
    etiqueta_texto_arrancar_simbolos.destroy()
    boton_atravesar_puerta_que_se_cierra.destroy()
    boton_encontrar_otra_salida.destroy()
    
    etiqueta_texto_encontrar_otra_salida.pack()
    
    boton_continuar.pack()
    
def rendirAnteCaida(): #Página 26
    boton_rendir_ante_caida.destroy()
    
    etiqueta_texto_rendir_ante_caida.pack()
    
    boton_continuar_1.pack()

def continuarAdelante(): #Página 28
    boton_continuar.destroy()
    boton_continuar_adelante.destroy()
    boton_retroceder_replantear_estrategia.destroy()
    
    etiqueta_texto_continuar_adelante.pack()
    
    boton_forzar_cerradura.pack()
    boton_explorar_otro_camino_2.pack()
    
def retrocederReplantearEstrategia(): #Página 30
    boton_continuar_1.destroy()
    boton_continuar_adelante.destroy()
    boton_retroceder_replantear_estrategia.destroy()
    
    etiqueta_texto_retroceder_replantear_estrategia.pack()
    
    boton_encontrar_refugio.pack()
    boton_continuar_adelante_1.pack()
    
def explorarCaminoIzquierda(): #Página 31
    boton_explorar_camino_izquierda.destroy()
    boton_explorar_camino_derecha.destroy()
    
    etiqueta_texto_explorar_camino_izquierda.pack()
    
    boton_explorar_otro_camino_3.pack()
    boton_seguir_el_mapa.pack()
    
def forzarCerradura(): #Página 34
    boton_forzar_cerradura.destroy()
    boton_explorar_otro_camino_2.destroy()
    
    etiqueta_texto_intentas_forzar_cerradura.pack()
    
    boton_enfrentar_guardianes.pack()
    boton_escapar_adentrandose.pack()
    
def buscasRefugioEsperas(): #Página 38
    boton_encontrar_refugio.destroy()
    boton_continuar_adelante_1.destroy()
    
    etiqueta_texto_buscas_refugio_esperas.pack()
    
    boton_continuar_4.pack()
    
def investigasMas(): #Página 39
    
    etiqueta_texto_investigas_mas.pack()
    
    boton_continuar_2.pack()
    
def procederSeguridad(): #Página 40
    boton_explorar_otro_camino_3.destroy()
    boton_seguir_el_mapa.destroy()
    
    etiqueta_texto_proceder_seguridad.pack()
    
    boton_continuar_3.pack()
    
def camaraCentral(): #Página 41
    boton_continuar_2.destroy()
    boton_continuar_3.destroy()
    
    etiqueta_texto_camara_central.pack()
    
def enfrentarGuardianes(): #Página 42
    boton_enfrentar_guardianes.destroy()
    boton_escapar_adentrandose.destroy()
    
    etiqueta_texto_enfrentar_guardianes.pack()
    
    #Faltan cosas y borrar de la 44
    
def vueltaAlLaberinto(): #Página 43
    boton_continuar_4.destroy()
    
    etiqueta_texto_vuelta_al_laberinto.pack()
    
def escaparAdentrandose(): #Página 44
    boton_enfrentar_guardianes.destroy()
    boton_escapar_adentrandose.destroy()
    
    etiqueta_texto_escapar_adentrandose.pack()
    
    #llama a la 48

def lograsteEscalarNoCaes(): #Página 46
    boton_lograste_escalar_no_caes.destroy()
    
    etiqueta_texto_lograste_escalar_no_caes.pack()
    
    boton_continuar_5.pack()
    
def implorarPiedad(): #Página 48
    #llamada por 44
    
    etiqueta_texto_implorar_piedad.pack()

def investigarCaverna(): #Página 49
    boton_investigar_caverna.destroy()
    boton_ignorar_caverna.destroy()
    boton_continuar_5.destroy()
    
    etiqueta_texto_investigar_caverna.pack()
    
    boton_salir_caverna.pack()
    boton_quedarse_investigar.pack()
    
def buscarOtraSalida50(): #Página 50
    boton_investigar_caverna.destroy()
    boton_ignorar_caverna.destroy()
    boton_continuar.destroy()
    boton_salir_caverna.destroy()
    boton_quedarse_investigar.destroy()
    
    etiqueta_texto_buscar_otra_salida50.pack()
    
    boton_lograste_escalar_no_caes.pack()
    boton_rendir_ante_caida.pack()
    
def permanecesCaverna(): #Página 56
    boton_salir_caverna.destroy()
    boton_quedarse_investigar.destroy()
    
    etiqueta_texto_permaneces_caverna.pack()
    
    boton_investigas_mas.pack()
    boton_precipitas_salida.pack()
    
def precipitasSalida(): #Página 59
    boton_investigas_mas.destroy()
    boton_precipitas_salida.destroy()
    
    etiqueta_texto_precipitas_salida.pack()  
              

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
boton_forzar_cerradura = Button(principal, text = "Intentar forzar cerradura")
boton_explorar_otro_camino_2 = Button(principal, text = "Buscar otra ruta", command = explorarOtroCamino)
boton_enfrentar_laberinto = Button(principal, text = "Enfrentar el laberinto directamente")
boton_encontrar_refugio = Button(principal, text = "Buscar refugio y esperar un cambio")
boton_seguir_el_mapa = Button(principal, text = "Seguir el mapa para navegar con seguridad")
boton_explorar_otro_camino_3 = Button(principal, text = "Continúa tu camino siguiendo únicamente tus instintos", command = explorarOtroCamino)
boton_enfrentar_guardianes = Button(principal, text = "Enfrentar a los guardianes")
boton_escapar_adentrandose = Button(principal, text = "Escapar adentrándose en el laberinto")
boton_dar_ultima_batalla = Button(principal, text = "Dar una última batalla")
boton_implorar_piedad = Button(principal, text = "Implorar piedad")
boton_salir_caverna = Button(principal, text = "Salir de la caverna y continuar explorando")
boton_quedarse_investigar = Button(principal, text = "Quedarse e investigar un poco más")
boton_lograste_escalar_no_caes = Button(principal, text="Intentas escalar", command = lograsteEscalarNoCaes)
boton_rendir_ante_caida = Button(principal, text= "Te rindes y caes esperando lo mejor", command = rendirAnteCaida)
boton_investigas_mas= Button(principal, text= "Investigar un poco más", command = investigasMas)
boton_precipitas_salida = Button(principal, text= "Precipitarte hacia la salida", command = precipitasSalida)
boton_continuar_1 = Button(principal, text = "Continuar", command = continuarAdelante)
boton_continuar_adelante_1 = Button(principal, text = "Continuar adelante")
boton_continuar_2 = Button(principal, text = "Continuar")
boton_continuar_3 = Button(principal, text = "Continuar")
boton_continuar_4 = Button(principal, text = "Continuar", command = vueltaAlLaberinto)
boton_continuar_5 = Button(principal, text= "Continuar")


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

texto_proceder_seguridad = (
    f"Usando el misterioso mapa, navegas el laberinto con una confianza renovada.\n"
    f"El mapa te lleva a una cámara central llena de artefactos.\n"
)

texto_camara_central = (
    f"A medida que investigas los artefactos más a fondo, notas un pequeño compartimento que revela una llave.\n"
    f"Intrigado, notas una cerradura muy peculiar que encaja perfectamente con la forma de la llave.\n"
    f"Insertas la llave en la cerradura y la cámara comienza a transformarse.\n"
    f"Se abre un pasadizo que te conduce de vuelta al mundo real.\n"
    f"A medida que lo recorres notas que estás sosteniendo un objeto muy antiguo: una reliquia del experimento.\n\n"
    f"HAS ESCAPADO DEL LABERINTO Y ESTÁS A SALVO\n\n"
    f"Este artefacto es único, un símbolo de tu triunfo sobre el enigmático laberinto.\n"
    f"Puede que tenga una significancia histórica o que tenga misteriosos poderes que podrás aprovechar en tu vida.\n"
    f"La naturaleza y potencial de esta reliquia están por ser descubiertas…\n"
)

texto_enfrentar_guardianes = (
    f"Te paras firmemente de cara a los guardianes con determinación.\n"
    f"Sin embargo, su cantidad te abruma, y sus garras despedazan cualquier defensa que puedas tener.\n"
    f"Lo último que ves es la retorcida mueca de en la cara de uno de los guardianes mientras la oscuridad te consume.\n\n"
    f"El experimento reclama una nueva víctima y tu aventura en el laberinto llega a un trágico final.\n\n"
    f"FIN\n"
)

texto_escapar_adentrandose = (
    f"Con el miedo apretando tu corazón, te giras y corres hacia la profundidad del laberinto, con la esperanza de perder a los guardianes que te persiguen.\n"
    f"Sin embargo, el laberinto serpentea de manera impredecible y te encuentras en un callejón sin salida.\n"
    f"Los guardianes se acercan con sus ojos hambrientos fijos en ti.\n"
)

texto_lograste_escalar_no_caes = (
    f"Con todas tus fuerzas escalas y tocas suelo firme.\n"
    f"Te encuentras en una caverna, ¿acaso la misma que decidiste ignorar?\n"
    f"No muy lejos ves que la luz del exterior se asoma pero eres consciente de que si ésta es la misma caverna que decidiste ignorar.\n"
    f"Salir podría traerte de vuelta a este mismo punto.\n"
)

texto_implorar_piedad = (
    f"Te arrodillas e imploras piedad.\n"
    f"Los guardianes hacen una pausa, sus caras retorcidas muestran una expresión de duda por un momento.\n"
    f"Pero la piedad no es un lenguaje que ellos entiendan.\n"
    f"Atacan sin remordimiento y tus lamentos quedan sin respuesta.\n\n"
    f"El experimento reclama una nueva víctima y tu aventura en el laberinto llega a un trágico final.\n\n"
    f"FIN\n"
)

texto_investigar_caverna = (
    f"La caverna está muy calurosa, no sabes si es buena idea quedarte.\n"
    f"Sin embargo, también piensas que algo muy importante puedes encontrar si investigas un poco más.\n"
)

texto_buscar_otra_salida50 = (
    f"Te adentras en un camino particularmente escabroso, y cada vez más oscuro.\n"
    f"El piso se siente cada vez más inestable.\n"
    f"En el momento en que te preguntas si deberías retornar, el suelo se derrumba.\n"
    f"Agitas tus brazos y tus manos agarran algo.\n"
)

texto_permaneces_caverna = (
    f"El calor aumenta y comienzas a sentir algo de mareo, aún no encuentras nada.\n"
    f"Una parte de ti cree que debe investigar un poco más.\n"
    f"Miras a la salida, está más lejana de lo que parece.\n"
    f"No sabes si puedas llegar sin desmayarte.\n"
)

texto_precipitas_salida = (
    f"El calor es insoportable, tu visión de la salida se hace doble, caes al suelo, pierdes la consciencia.\n"
    f"Te entregas a una muerte sin dolor.\n"
    f"El experimento ha cobrado una nueva vida.\n\n"
    f"FIN\n"
)

texto_vuelta_al_laberinto = (
    f"Caminas un poco y encuentras un puente\n"
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
etiqueta_texto_proceder_seguridad = Label(principal, text = texto_proceder_seguridad)
etiqueta_texto_camara_central = Label(principal, text = texto_camara_central)
etiqueta_texto_enfrentar_guardianes = Label(principal, text = texto_enfrentar_guardianes)
etiqueta_texto_escapar_adentrandose = Label(principal, text = texto_escapar_adentrandose)
etiqueta_texto_lograste_escalar_no_caes = Label(principal, text = texto_lograste_escalar_no_caes)
etiqueta_texto_implorar_piedad = Label(principal, text = texto_implorar_piedad)
etiqueta_texto_investigar_caverna = Label(principal, text = texto_investigar_caverna)
etiqueta_texto_buscar_otra_salida50 = Label(principal, text = texto_buscar_otra_salida50)
etiqueta_texto_permaneces_caverna = Label(principal,  text = texto_permaneces_caverna)
etiqueta_texto_vuelta_al_laberinto = Label(principal, text = texto_vuelta_al_laberinto)
etiqueta_texto_precipitas_salida = Label(principal, text = texto_precipitas_salida)



#Loop principal
principal.mainloop()
