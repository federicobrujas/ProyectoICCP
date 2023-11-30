from tkinter import *
from tkinter import font
import random as rn
from customtkinter import *
import pygame

#Características generales del jugador
nombre_jugador = ""
stamina_jugador = 50
meta = 0

# Inicialización de la ventana usando tkinter
principal = CTk()
principal.title("Perdido en el Laberinto: Un Juego Simple Basado en Texto")
principal.geometry("750x500")

#Variables de diseño

set_appearance_mode("system")
set_default_color_theme("blue")


#principal.overrideredirect(True)

fuente_general = font.Font(family="Garamond", size = 16)
principal.option_add("*Font", fuente_general)

color_letra = "#ffffff"
color_letra_boton= "#ffffff"
color_barra_titulo= "#6b7368"
color_fondo = "#000000"

#title_bar = Frame(principal, bg=color_barra_titulo, relief="raised", bd=0)
#title_bar.pack(expand=1, fill="x")
#title_bar.bind("<B1-Motion>", move_window)

principal.option_add("*Label.Background",color_fondo)
principal.option_add("*Label.Foreground", color_letra)
principal.option_add("*Button.Foreground", color_letra_boton)

#Documentos generales 

pygame.mixer.init()
#pygame.mixer.music.load("C:\\Users\\jleon\\OneDrive\\Documentos\\Through the Sinister Gate.mp3")
#pygame.mixer.music.play(loops=-1)


#Introducción y configuración del jugador
etiqueta_intro = CTkLabel(principal, text = "Bienvenido a Perdido en el Laberinto, ¿estás dispuesto a comenzar?\n")
etiqueta_intro.pack()


etiqueta_nombre = CTkLabel(principal, text = "Ingresa tu nombre")
etiqueta_nombre.pack()

ingreso_nombre = Entry(principal)
ingreso_nombre.pack()


#Funciones inicio de juego
def comenzarJuego():
    global nombre_jugador
    nombre_jugador = ingreso_nombre.get()
    etiqueta_intro.configure(text = f"Bienvenido, {nombre_jugador}! La aventura comienza...")
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
    boton_afrontar_la_puerta.place(x=290, y=218)


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
    boton_explorar_camino_derecha.destroy()
    boton_explorar_camino_izquierda.destroy()
    boton_explorar_otro_camino_3.destroy()
    boton_seguir_el_mapa.destroy()
    etiqueta_texto_afrontar_la_puerta.destroy()
    etiqueta_texto_cruzar_el_puente.destroy()
    etiqueta_texto_continuar_cruzando_el_puente.destroy()
    etiqueta_texto_explorar_camino_izquierda.destroy()
    etiqueta_texto_memorizar_mapa_cruzar_puerta.destroy()
     
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
    boton_lograste_escalar_no_caes.destroy()
    boton_dale.destroy()
    boton_resultado_2.destroy()
    etiqueta_texto_buscar_otra_salida50.destroy()
    etiqueta_resultado.destroy()
    
    etiqueta_texto_rendir_ante_caida.pack()
    
    boton_continuar_1.pack()
    boton_a_la_30.pack()

def continuarAdelante(): #Página 28
    boton_continuar.destroy()
    boton_continuar_adelante.destroy()
    boton_retroceder_replantear_estrategia.destroy()
    boton_encontrar_refugio.destroy()
    boton_continuar_adelante_1.destroy()
    boton_continuar_1.destroy()
    boton_a_la_30.destroy()
    etiqueta_texto_rendir_ante_caida.destroy()
    etiqueta_texto_retroceder_replantear_estrategia.destroy()
    etiqueta_texto_atravesar_puerta_que_se_cierra.destroy()
    
    etiqueta_texto_continuar_adelante.pack()
    
    boton_forzar_cerradura.pack()
    boton_explorar_otro_camino_2.pack()
    
def retrocederReplantearEstrategia(): #Página 30
    boton_continuar_1.destroy()
    boton_continuar_adelante.destroy()
    boton_retroceder_replantear_estrategia.destroy()
    boton_a_la_30.destroy()
    etiqueta_texto_rendir_ante_caida.destroy()
    etiqueta_texto_atravesar_puerta_que_se_cierra.destroy()
    
    etiqueta_texto_retroceder_replantear_estrategia.pack()
    
    boton_encontrar_refugio.pack()
    boton_continuar_adelante_1.pack()
    
def explorarCaminoIzquierda(): #Página 31
    boton_explorar_camino_izquierda.destroy()
    boton_explorar_camino_derecha.destroy()
    etiqueta_texto_continuar_cruzando_el_puente.destroy()
    
    etiqueta_texto_explorar_camino_izquierda.pack()
    
    boton_explorar_otro_camino_3.pack()
    boton_seguir_el_mapa.pack()
    
def forzarCerradura(): #Página 34
    boton_forzar_cerradura.destroy()
    boton_explorar_otro_camino_2.destroy()
    etiqueta_texto_continuar_adelante.destroy()
    
    etiqueta_texto_intentas_forzar_cerradura.pack()
    
    boton_enfrentar_guardianes.pack()
    boton_escapar_adentrandose.pack()
    
def buscasRefugioEsperas(): #Página 38
    boton_encontrar_refugio.destroy()
    boton_continuar_adelante_1.destroy()
    etiqueta_texto_retroceder_replantear_estrategia.destroy()
    
    etiqueta_texto_buscas_refugio_esperas.pack()
    
    boton_continuar_4.pack()
    
def investigasMas(): #Página 39
    boton_investigas_mas.destroy()
    boton_precipitas_salida.destroy()
    etiqueta_texto_permaneces_caverna.destroy()
    
    etiqueta_texto_investigas_mas.pack()
    
    boton_continuar_2.pack()
    
def procederSeguridad(): #Página 40
    boton_explorar_otro_camino_3.destroy()
    boton_seguir_el_mapa.destroy()
    boton_explorar_camino_derecha.destroy()
    boton_explorar_camino_izquierda.destroy()
    etiqueta_texto_continuar_cruzando_el_puente.destroy()
    etiqueta_texto_explorar_camino_izquierda.destroy()
    
    
    etiqueta_texto_proceder_seguridad.pack()
    
    boton_continuar_3.pack()
    
def camaraCentral(): #Página 41
    boton_continuar_2.destroy()
    boton_continuar_3.destroy()
    etiqueta_texto_proceder_seguridad.destroy()
    etiqueta_texto_investigas_mas.destroy()
    
    etiqueta_texto_camara_central.pack()
    
def enfrentarGuardianes(): #Página 42
    boton_enfrentar_guardianes.destroy()
    boton_escapar_adentrandose.destroy()
    boton_dar_ultima_batalla.destroy()
    boton_implorar_piedad.destroy()
    etiqueta_texto_intentas_forzar_cerradura.destroy()
    etiqueta_texto_escapar_adentrandose.destroy()
    
    etiqueta_texto_enfrentar_guardianes.pack()
    
    #Faltan cosas
    
def vueltaAlLaberinto(): #Página 43
    boton_continuar_4.destroy()
    
    etiqueta_texto_vuelta_al_laberinto.pack()
    
def escaparAdentrandose(): #Página 44
    boton_enfrentar_guardianes.destroy()
    boton_escapar_adentrandose.destroy()
    etiqueta_texto_intentas_forzar_cerradura.destroy()
    
    etiqueta_texto_escapar_adentrandose.pack()
    
    boton_implorar_piedad.pack()
    boton_dar_ultima_batalla.pack()

def lograsteEscalarNoCaes(): #Página 46
    boton_lograste_escalar_no_caes.destroy()
    #boton_rendir_ante_caida.destroy()
    etiqueta_texto_buscar_otra_salida50.destroy()
    
    etiqueta_texto_lograste_escalar_no_caes.pack()
    
    boton_continuar_5.pack()
    
def implorarPiedad(): #Página 48
    boton_implorar_piedad.destroy()
    etiqueta_texto_escapar_adentrandose.destroy()
    
    etiqueta_texto_implorar_piedad.pack()

def investigarCaverna(): #Página 49
    boton_investigar_caverna.destroy()
    boton_ignorar_caverna.destroy()
    boton_continuar_5.destroy()
    etiqueta_texto_lograste_escalar_no_caes.destroy()
    etiqueta_texto_explorar_otro_camino.destroy()
    
    etiqueta_texto_investigar_caverna.pack()
    
    boton_salir_caverna.pack()
    boton_quedarse_investigar.pack()
    
def buscarOtraSalida50(): #Página 50
    boton_investigar_caverna.destroy()
    boton_ignorar_caverna.destroy()
    boton_continuar.destroy()
    boton_salir_caverna.destroy()
    boton_quedarse_investigar.destroy()
    etiqueta_texto_explorar_otro_camino.destroy()
    etiqueta_texto_investigar_caverna.destroy()
    etiqueta_texto_encontrar_otra_salida.destroy()
    
    etiqueta_texto_buscar_otra_salida50.pack()
    
    boton_lograste_escalar_no_caes.pack()
    
def permanecesCaverna(): #Página 56
    boton_salir_caverna.destroy()
    boton_quedarse_investigar.destroy()
    etiqueta_texto_investigar_caverna.destroy()
    
    etiqueta_texto_permaneces_caverna.pack()
    
    boton_investigas_mas.pack()
    boton_precipitas_salida.pack()
    
def precipitasSalida(): #Página 57
    boton_investigas_mas.destroy()
    boton_precipitas_salida.destroy()
    etiqueta_texto_permaneces_caverna.destroy()
    
    etiqueta_texto_precipitas_salida.pack()
    
def goldenChoice(): #Página 69
    boton_lograste_escalar_no_caes.destroy()
    boton_continuar_4.destroy()
    boton_forzar_cerradura.destroy()
    boton_explorar_otro_camino_2.destroy()
    boton_dale.destroy()
    boton_resultado_1.destroy()
    etiqueta_resultado.destroy()
    etiqueta_texto_buscar_otra_salida50.destroy()
    etiqueta_texto_buscas_refugio_esperas.destroy()
    etiqueta_texto_continuar_adelante.destroy()
    
    etiqueta_texto_golden_choice.pack() 
    
#Funciones de interacción
def minijuego50():
    etiqueta_texto_buscar_otra_salida50.destroy()
    boton_lograste_escalar_no_caes.destroy()
    
    boton_dale.pack()
    
    global stamina_jugador, meta
    stamina_jugador -= rn.randint(1,10)
    meta += rn.randint(1,10)

    print("Stamina ", stamina_jugador)
    print("Meta ", meta)

    if meta >= 50:
        etiqueta_resultado.configure(text="Lograste escalar")
        boton_resultado_1.pack()
        boton_dale.destroy()
    elif stamina_jugador <= 0:
        etiqueta_resultado.configure(text="Tu energía se ha agotado, te caerás")
        boton_resultado_2.pack()
        boton_dale.destroy()
        
    etiqueta_resultado.pack()    

def llamarBoton():
    minijuego50()
    if meta < 50 and stamina_jugador > 0:
        principal.after(100000000000000, llamarBoton)                       


#Función terminar ejecución
def salirJuego():
    principal.destroy()

#Definición de botones para interacción
boton_inicio = CTkButton(master = principal, text = "Comenzar", command = comienzoHistoria)
boton_inicio.pack()
boton_salir = CTkButton(master = principal, text = "Salir", command = salirJuego)
boton_buscar_en_la_habitacion = CTkButton(master = principal, text = "Explorar la habitación", command = buscarEnLaHabitación)
boton_afrontar_la_puerta = CTkButton(master=principal, text = "Afrontar la puerta", command = afrontarLaPuerta)
boton_cruzar_el_puente = CTkButton(master=principal, text = "Cruzar el puente", command = cruzarElPuente)
boton_explorar_otro_camino = CTkButton(master=principal, text = "Explorar otro camino", command = explorarOtroCamino)
boton_explorar_otro_camino_1 = CTkButton(master=principal, text = "Explorar otro camino", command = explorarOtroCamino)
boton_inspeccionar_simbolos = CTkButton(master=principal, text = "Inspeccionar los Símbolos en las Paredes", command = inspeccionarSimbolos)
boton_arrancar_simbolos = CTkButton(master=principal, text = "Arrancar los símbolos y conservarlos", command = arrancarSimbolos)
boton_memorizar_mapa = CTkButton(master=principal, text = "Memorizar el mapa y avanzar por la puerta", command = memorizarMapaCruzarPuerta)
boton_atravesar_puerta_que_se_cierra = CTkButton(master=principal, text = "Atravesar rápidamente la puerta que se cierra", command = atravesarPuertaQueSeCierra)
boton_encontrar_otra_salida = CTkButton(master=principal, text ="Buscar otra salida", command = encontrarOtraSalida)
boton_seguir_cruzando_el_puente = CTkButton(master=principal, text ="Continuar cruzando el puente", command = seguirCruzandoElPuente)
boton_explorar_camino_izquierda = CTkButton(master=principal, text = "Explorar el camino de la izquierda", command = explorarCaminoIzquierda)
boton_explorar_camino_derecha = CTkButton(master=principal, text = "Explorar el camino de la derecha", command = explorarOtroCamino)
boton_continuar_adelante = CTkButton(master=principal, text = "Continuar adelante", command = continuarAdelante)
boton_retroceder_replantear_estrategia = CTkButton(master=principal, text = "Retroceder y replantear tu estrategia", command = retrocederReplantearEstrategia)
boton_investigar_caverna = CTkButton(master=principal, text = "Investigar la caverna", command = investigarCaverna)
boton_ignorar_caverna = CTkButton(master=principal, text = "Ignorar la caverna y continuar por el camino", command = buscarOtraSalida50)
boton_continuar = CTkButton(master=principal, text = "Continuar", command = buscarOtraSalida50)
boton_forzar_cerradura = CTkButton(master=principal, text = "Intentar forzar cerradura", command = forzarCerradura)
boton_explorar_otro_camino_2 = CTkButton(master=principal, text = "Explorar otro camino", command = goldenChoice)
boton_enfrentar_laberinto = CTkButton(master=principal, text = "Enfrentar el laberinto directamente")
boton_encontrar_refugio = CTkButton(master=principal, text = "Buscar refugio y esperar un cambio", command = buscasRefugioEsperas)
boton_seguir_el_mapa = CTkButton(master=principal, text = "Seguir el mapa para navegar con seguridad", command = procederSeguridad)
boton_explorar_otro_camino_3 = CTkButton(master=principal, text = "Continúa tu camino siguiendo únicamente tus instintos", command = explorarOtroCamino)
boton_enfrentar_guardianes = CTkButton(master=principal, text = "Enfrentar a los guardianes", command = enfrentarGuardianes)
boton_escapar_adentrandose = CTkButton(master=principal, text = "Escapar adentrándose en el laberinto", command = escaparAdentrandose)
boton_dar_ultima_batalla = CTkButton(master=principal, text = "Dar una última batalla", command = enfrentarGuardianes)
boton_implorar_piedad = CTkButton(master=principal, text = "Implorar piedad", command = implorarPiedad)
boton_salir_caverna = CTkButton(master=principal, text = "Salir de la caverna y continuar explorando", command = buscarOtraSalida50)
boton_quedarse_investigar = CTkButton(master=principal, text = "Quedarse e investigar un poco más", command = permanecesCaverna)
boton_lograste_escalar_no_caes = CTkButton(master=principal, text="¿Crees que tienes suficiente energía para escalar?", command = minijuego50)
boton_investigas_mas= CTkButton(master=principal, text= "Investigar un poco más", command = investigasMas)
boton_precipitas_salida = CTkButton(master=principal, text= "Precipitarte hacia la salida", command = precipitasSalida)
boton_continuar_1 = CTkButton(master=principal, text = "Seguir adelante", command = continuarAdelante)
boton_continuar_adelante_1 = CTkButton(master=principal, text = "Continuar adelante", command = continuarAdelante)
boton_continuar_2 = CTkButton(master=principal, text = "Continuar", command = camaraCentral)
boton_continuar_3 = CTkButton(master=principal, text = "Continuar", command = camaraCentral)
boton_continuar_4 = CTkButton(master=principal, text = "Continuar", command = goldenChoice)
boton_continuar_5 = CTkButton(master=principal, text= "Continuar", command = investigarCaverna)
boton_a_la_30 = CTkButton(master=principal, text = "Retroceder y replantear estrategia", command = retrocederReplantearEstrategia)
boton_dale = CTkButton(master=principal, text = "Dale!", command = llamarBoton)
boton_resultado_1 = CTkButton(master=principal, text = "Continuar", command = goldenChoice)
boton_resultado_2 = CTkButton(master=principal, text ="Continuar", command = rendirAnteCaida)

# Textos
texto_inicial = (
        f"Tus ojos se abren de golpe, te encuentras en una habitación \n" 
        f"tenuemente iluminadacon el sabor metálico del miedo en el aire.\n"
        f"El sudor frío recorre tu frente mientras te pones de pie, \n" 
        f"dándote cuenta de que estás solo.\n" 
        f"Las paredes están decoradas con símbolos extraños que \n" 
        f"parecen palpitar con una energía inquietante.\n" 
        f"Una puerta misteriosa te llama hacia la oscuridad \n" 
        f"que hay más allá.\n"
    )

texto_buscar_en_la_habitacion = (
        f"Mientras buscas, tu mano roza una\n" 
        f"nota arrugada en tu bolsillo.\n" 
        f"Dice: ""Navega el laberinto \n" 
        f"para encontrar la verdad"".\n" 
        f"Determinado, contemplas\n"
        f"tu próximo movimiento.\n"
    )

texto_afrontar_la_puerta = (
        f"Decides proceder por la misteriosa puerta.\n" 
        f"El angosto corredor te lleva hacia\n" 
        f"un laberinto con pasajes enredados.\n" 
        f"Te enfrentas a tu primer desafío: \n" 
        f"un puente precario sobre un abismo \n "
        f"aparentemente interminable.\n"
    )

texto_inspeccionar_simbolos = (
        f"Los símbolos en las paredes parecen formar un \n" 
        f"mapa rudimentario del laberinto, y descifras un mensaje:\n" 
        f"'Cuidado con las criaturas, no confíes en nadie'\n"
        f"Armado con esta advertencia, te preparas para el \n" 
        f"viaje que tienes por delante.\n"
)
texto_memorizar_mapa_cruzar_puerta = (
        f"Entras en el laberinto, entre sus giros y \n"
        f"vueltas retumban sonidos escalofriantes.\n"
        f"Criaturas acechan en las sombras, y te \n"
        f"enfrentas a tu primer desafío:\n"
        f"Un puente precario sobre un \n" 
        f"abismo aparentemente interminable.\n "
        f"Cierras los ojos e intentas recordar \n" 
        f"el mapa que intentaste memorizar,\n"
        f"hay algo en ese puente que te dice \n"
        f"que debes cruzarlo\n"
)
texto_arrancar_simbolos = (
        f"Con urgencia, arrancas los símbolos \n"
        f"de las paredes, pensando que podrían \n"
        f"ser cruciales para tu supervivencia.\n "
        f"Sin embargo, al guardarlos apresuradamente \n"
        f"en tus bolsillos, un ruido abominable \n"
        f"resuena en la habitación. Las paredes \n"
        f"parecen temblar, y la puerta de \n"
        f"salida comienza a cerrarse.\n"
)
texto_atravesar_puerta_que_se_cierra =(
        f"Corres hacia la puerta que se cierra, \n"
        f"apenas logrando pasar antes de que se selle.\n"
        f"La habitación se transforma en un laberinto, \n"
        f"ves cómo la forma del laberinto se transforma \n"
        f"frente a tus ojos de manera impredecible. \n"
        f"Los símbolos rasgados en tus manos son \n"
        f"ahora indescifrables.\n\n"
        f"Mientras avanzas, el laberinto se vuelve más \n"
        f"traicionero. Las sombras parpadean y gruñidos \n"
        f"distantes aseguran peligros acechando.\n"
        f"Tu decisión de arrancar los símbolos puede \n"
        f"haber hecho que el laberinto sea aún más impredecible.\n"
)
texto_encontrar_otra_salida =(
        f"La puerta se cierra y la habitación comienza\n" 
        f"a temblar. Desesperado buscas otra salida, pasas \n"
        f"tu mirada por todos los rincones.Eventualmente \n"
        f"un punto oscuro llama tu atención, te diriges \n"
        f"hacia este y descubres que es una entrada a un \n"
        f"pasadizo por el que apenas cabes.\n"
)
texto_explorar_otro_camino =(
        f"Decides buscar una ruta alterna, tomas un \n"
        f"pasadizo cada vez más angosto, te volteas pues \n"
        f"el camino no te da confianza y descubres que \n"
        f"el camino de vuelta está bloqueado, solo puedes \n"
        f"seguir adelante.Después de lo que parecen horas \n"
        f"caminando, encuentras una entrada hacia lo que \n"
        f"parece una caverna.\n"
)
texto_cruzar_el_puente =(
        f"Te acercas con cautela al precario puente, el \n"
        f"eco de tus pasos se mezcla con el sonido \n"
        f"espeluznante del laberinto. Cuando subes a la \n"
        f"primera tabla, ésta cruje siniestramente pero \n"
        f"mantiene tu peso.\n"
)
texto_continuar_cruzando_el_puente =(
        f"Con pasos cuidadosos, navegas por el puente \n"
        f"traicionero. El abismo de abajo parece interminable,\n"
        f"pero llegas ileso al otro lado. El laberinto se \n"
        f"abre y te dirige al interior de una caverna que\n"
        f"es una cámara con múltiples caminos.\n\n"
        f"De repente escuchas lamentos y gritos de \n"
        f"desesperación que parecen venir del camino de la izquierda.\n"
)

texto_rendir_ante_caida = (
    f"Estás de vuelta en el laberinto, esta vez la \n"
    f"forma del laberinto se transforma frente a tus \n"
    f"ojos de manera impredecible. Los símbolos \n"
    f"rasgados en tus manos son ahora indescifrables.\n\n"
    f"Mientras avanzas, el laberinto se vuelve más \n"
    f"traicionero. Las sombras parpadean y gruñidos \n"
    f"distantes aseguran peligros acechando.\n"
    f"Tu decisión de arrancar los símbolos puede haber \n"
    f"hecho que el laberinto sea aún más impredecible.\n"
)

texto_continuar_adelante = (
    f"Con determinación, sigues adelante a través de \n"
    f"los corredores siempre cambiantes del laberinto.\n"
    f"Los símbolos rasgados ofrecen poca orientación, \n"
    f"y pronto te encuentras frente a una enorme puerta \n"
    f"cerrada con llave.\n"
)

texto_retroceder_replantear_estrategia = (
    f"Al darte cuenta de que los símbolos rasgados son \n"
    f"más un obstáculo que una ayuda, retrocedes \n"
    f" intentando volver sobre tus pasos. Sin embargo, \n"
    f"el laberinto parece tener una mente propia, \n"
    f"reorganizándose como si se burlara de tus \n"
    f"intentos de escapar.\n"
    
)

texto_explorar_camino_izquierda = (
    f"Te aventuras por el camino de la izquierda y \n"
    f"te encuentras con un grupo de personas perdidas.\n"
    f"Algunos ofrecen valiosas ideas y comparten \n"
    f"suministros. Uno de ellos te entrega un mapa \n"
    f"del laberinto, que revela atajos y peligros potenciales.\n"
)

texto_intentas_forzar_cerradura = (
    f"Tomas aire profundamente, acercándote a la \n"
    f"imponente puerta. La tenue luz proyecta sombras \n"
    f"inquietantes a medida que manipulas el candado, \n"
    f"intentando forzarlo desesperadamente.\n"
    f"Sin que te des cuenta, el sonido que haces en \n"
    f"tu esfuerzo produce un eco en el laberinto\n"
    f"llamando la atención de los guardianes de este.\n\n"
    f"De repente la puerta se abre revelando un \n"
    f"pasadizo angosto. Sonríes triunfante, pero \n"
    f"la sonrisa dura poco. Los guardianes, unas \n"
    f"criaturas grotescas con garras afiladas y \n"
    f"ojos hambrientos emergen de las sombras.\n"
)

texto_buscas_refugio_esperas = (
    f"Encuentras una pequeña zanja donde apenas \n"
    f"cabes, esta parece ser capaz de protegerte \n"
    f"del caos de afuera. El mundo comienza a temblar, \n"
    f"es como un terremoto que jamás has sentido \n"
    f"ni imaginado. Eres incapaz de salir de donde \n"
    f"estás y tu única esperanza es que ahí dentro \n"
    f"estés seguro. Después de lo que parece una \n"
    f"eternidad el temblor cesa y sales de la zanja.\n"
    f"Ahora el laberinto parece estable y de hecho \n"
    f"te parece familiar con lo que alcanzaste a ver \n"
    f"del mapa.\n"
)

texto_investigas_mas = (
    f"Tus ojos se fijan en algo que parece producir \n"
    f"un destello de luz rojo, y procedes a tomarlo \n"
    f"con tus manos. Entonces, el calor empieza a \n"
    f"desaparecer y la habitación comienza a iluminarse.\n"
    f"Notas que tu visión estaba borrosa pero también \n"
    f"notas, a medida que el mareo desaparece,\n" 
    f"que te encuentras en una cámara llena de artefactos\n"
)

texto_proceder_seguridad = (
    f"Usando el misterioso mapa, navegas el laberinto \n"
    f"con una confianza renovada. El mapa te lleva a \n"
    f"una cámara central llena de artefactos.\n"
)

texto_camara_central = (
    f"A medida que investigas los artefactos más a \n"
    f"fondo, notas un pequeño compartimento que \n"
    f"revela una llave. Intrigado, notas una cerradura \n"
    f"muy peculiar que encaja perfectamente con la \n"
    f"forma de la llave. Insertas la llave en la \n"
    f"cerradura y la cámara comienza a transformarse.\n"
    f"Se abre un pasadizo que te conduce de vuelta al \n"
    f"mundo real. A medida que lo recorres notas que \n"
    f"estás sosteniendo un objeto muy antiguo: una \n"
    f"reliquia del experimento.\n\n"
    f"HAS ESCAPADO DEL LABERINTO Y ESTÁS A SALVO\n\n"
    f"Este artefacto es único, un símbolo de tu \n"
    f"triunfo sobre el enigmático laberinto.\n"
    f"Puede que tenga una significancia histórica \n"
    f"o que tenga misteriosos poderes que podrás \n"
    f"aprovechar en tu vida. La naturaleza y potencial \n"
    f"de esta reliquia están por ser descubiertas…\n"
)

texto_enfrentar_guardianes = (
    f"Te paras firmemente de cara a los guardianes \n"
    f"con determinación. Sin embargo, su cantidad te \n"
    f"abruma, y sus garras despedazan cualquier defensa \n"
    f"que puedas tener. Lo último que ves es la retorcida \n"
    f"mueca de en la cara de uno de los guardianes \n"
    f"mientras la oscuridad te consume.\n\n"
    f"El experimento reclama una nueva víctima y tu \n"
    f"aventura en el laberinto llega a un trágico final.\n\n"
    f"FIN\n"
)

texto_escapar_adentrandose = (
    f"Con el miedo apretando tu corazón, te giras y corres \n"
    f"hacia la profundidad del laberinto, con la esperanza \n"
    f"de perder a los guardianes que te persiguen.\n"
    f"Sin embargo, el laberinto serpentea de manera \n"
    f"impredecible y te encuentras en un callejón sin salida.\n"
    f"Los guardianes se acercan con sus ojos hambrientos \n"
    f"fijos en ti.\n"
)

texto_lograste_escalar_no_caes = (
    f"Con todas tus fuerzas escalas y tocas suelo firme.\n"
    f"Te encuentras en una caverna, ¿acaso la misma que \n"
    f"decidiste ignorar? No muy lejos ves que la luz del \n"
    f"exterior se asoma pero eres consciente de que si \n"
    f"ésta es la misma caverna que decidiste ignorar.\n"
    f"Salir podría traerte de vuelta a este mismo punto.\n"
)

texto_implorar_piedad = (
    f"Te arrodillas e imploras piedad.Los guardianes hacen \n"
    f"una pausa, sus caras retorcidas muestran una expresión \n"
    f"de duda por un momento. Pero la piedad no es un \n"
    f"lenguaje que ellos entiendan. Atacan sin remordimiento\n"
    f"y tus lamentos quedan sin respuesta.\n\n"
    f"El experimento reclama una nueva víctima y tu aventura \n"
    f"en el laberinto llega a un trágico final.\n\n"
    f"FIN\n"
)

texto_investigar_caverna = (
    f"La caverna está muy calurosa, no sabes si es buena \n"
    f"idea quedarte. Sin embargo, también piensas que algo \n"
    f"muy importante puedes encontrar si investigas un poco más.\n"
)

texto_buscar_otra_salida50 = (
    f"Te adentras en un camino particularmente escabroso, \n"
    f"y cada vez más oscuro. El piso se siente cada vez \n"
    f"más inestable. En el momento en que te preguntas si \n"
    f"deberías retornar, el suelo se derrumba. Agitas tus \n"
    f"brazos y tus manos agarran algo.\n"
)

texto_permaneces_caverna = (
    f"El calor aumenta y comienzas a sentir algo de mareo, \n"
    f"aún no encuentras nada. Una parte de ti cree que debe \n"
    f"investigar un poco más. Miras a la salida, está más \n"
    f"lejana de lo que parece. No sabes si puedas llegar \n"
    f"sin desmayarte.\n"
)

texto_precipitas_salida = (
    f"El calor es insoportable, tu visión de la salida se \n"
    f"hace doble, caes al suelo, pierdes la consciencia.\n"
    f"Te entregas a una muerte sin dolor. El experimento \n"
    f"ha cobrado una nueva vida.\n\n"
    f"FIN\n"
)

texto_vuelta_al_laberinto = (
    f"Caminas un poco y encuentras un puente\n"
)

texto_golden_choice = (
    f"Das un paso.\n"
    f"Sientes algo macizo bajo tu pie derecho.\n"
    f"Una explosión te deja sordo, una milésima antes de matarte\n\n"
    f"Por un mal paso te has convertido en la nueva víctima del experimento\n\n"
    f"FIN\n"    
)

#Etiquetas de texto
etiqueta_texto_inicial = CTkLabel(principal, text = texto_inicial)
etiqueta_texto_buscar_en_la_habitacion = CTkLabel(principal, text = texto_buscar_en_la_habitacion)
etiqueta_texto_afrontar_la_puerta = CTkLabel(principal, text = texto_afrontar_la_puerta)
etiqueta_texto_inspeccionar_simbolos = CTkLabel(principal, text = texto_inspeccionar_simbolos)
etiqueta_texto_arrancar_simbolos = CTkLabel(principal, text = texto_arrancar_simbolos)
etiqueta_texto_memorizar_mapa_cruzar_puerta = CTkLabel(principal, text =texto_memorizar_mapa_cruzar_puerta)
etiqueta_texto_encontrar_otra_salida = CTkLabel(principal, text = texto_encontrar_otra_salida)
etiqueta_texto_atravesar_puerta_que_se_cierra = CTkLabel(principal, text = texto_atravesar_puerta_que_se_cierra)
etiqueta_texto_cruzar_el_puente = CTkLabel(principal, text =texto_cruzar_el_puente)
etiqueta_texto_continuar_cruzando_el_puente = CTkLabel(principal, text = texto_continuar_cruzando_el_puente)
etiqueta_texto_explorar_otro_camino = CTkLabel(principal, text = texto_explorar_otro_camino)
etiqueta_texto_rendir_ante_caida = CTkLabel(principal, text = texto_rendir_ante_caida)
etiqueta_texto_continuar_adelante = CTkLabel(principal, text = texto_continuar_adelante)
etiqueta_texto_retroceder_replantear_estrategia = CTkLabel(principal, text = texto_retroceder_replantear_estrategia)
etiqueta_texto_explorar_camino_izquierda = CTkLabel(principal, text = texto_explorar_camino_izquierda)
etiqueta_texto_intentas_forzar_cerradura = CTkLabel(principal, text = texto_intentas_forzar_cerradura)
etiqueta_texto_buscas_refugio_esperas = CTkLabel(principal, text = texto_buscas_refugio_esperas)
etiqueta_texto_investigas_mas = CTkLabel (principal, text = texto_investigas_mas)
etiqueta_texto_proceder_seguridad = CTkLabel(principal, text = texto_proceder_seguridad)
etiqueta_texto_camara_central = CTkLabel(principal, text = texto_camara_central)
etiqueta_texto_enfrentar_guardianes = CTkLabel(principal, text = texto_enfrentar_guardianes)
etiqueta_texto_escapar_adentrandose = CTkLabel(principal, text = texto_escapar_adentrandose)
etiqueta_texto_lograste_escalar_no_caes = CTkLabel(principal, text = texto_lograste_escalar_no_caes)
etiqueta_texto_implorar_piedad = CTkLabel(principal, text = texto_implorar_piedad)
etiqueta_texto_investigar_caverna = CTkLabel(principal, text = texto_investigar_caverna)
etiqueta_texto_buscar_otra_salida50 = CTkLabel(principal, text = texto_buscar_otra_salida50)
etiqueta_texto_permaneces_caverna = CTkLabel(principal,  text = texto_permaneces_caverna)
etiqueta_texto_vuelta_al_laberinto = CTkLabel(principal, text = texto_vuelta_al_laberinto)
etiqueta_texto_precipitas_salida = CTkLabel(principal, text = texto_precipitas_salida)
etiqueta_texto_golden_choice = CTkLabel(principal, text = texto_golden_choice)
etiqueta_resultado = CTkLabel(principal, text = "")


#Loop principal
principal.mainloop()
