import pygame as pg
import random 
from Funciones import * 

#Constantes y variables
RESOLUCION_PANTALLA = (800, 600)
coord_mouse = [0, 0]
COLOR_NEGRO = (0, 0, 0)
COLOR_CELESTE = (0, 180, 220)
COLOR_AMARILLO = (255, 255, 0)
COLOR_BLANCO = (255, 255, 255)
COLOR_ROJO = (255, 0, 0)
COLOR_NARANJA = (255, 85, 0)
COORD_FONDO = (0, 0)
coord_personaje = [0, 500]
coord_circulo = [100, 100]
velocidad = 0 
velocidad_normal = 2
tamaño_personaje_espalda = [32, 84]
tamaño_personaje_derecha = [33, 80]
tamaño_personaje_izquierda = [33, 81]
tamaño_personaje_frente = [32, 86]
tamaño_personaje_corriendo_derecha = [60, 60]
tamaño_personaje_corriendo_izquierda = [60, 60]
tamaño_personaje_corriendo_espalda = [60, 60]
tamaño_personaje_corriendo_frente = [60, 60]
SONIDO_MUSICA = "./Sonidos/sonido-fondo-mar.mp3"
SONIDO_PASOS = "./Sonidos/caminando madera.mp3"
SONIDO_REEL = "./Sonidos/reel.mp3"
jugando = False

modo_test = False
velocidad_correr = velocidad_normal * 2
movimiento = True
pesca = False
contador_total = 0
tiempos_de_pesca = [4000, 8000, 12000, 16000, 2000]
cooldown = random.choice(tiempos_de_pesca)
ultima_pesca = 0  

#Diccionario
contador_peces = {
    "Arenque": [0,0],
    "Boqueron": [0,0],
    "Anguila": [0,0],
    "Salmon": [0,0],
    "Trucha": [0,0],
    "Anchoa": [0,0],
    "Salmonete": [0,0],
    "Pez Espada": [0,0],
    "Rodaballo": [0,0],
    "Bonito": [0,0],
    "Congrio": [0,0],
    "Cazon": [0,0],
    "Sardina": [0,0],
    "Caballa": [0,0],
    "Jurel": [0,0],
    "Lamprea": [0,0],
}

peces = ["Arenque", "Boqueron", "Anguila", "Salmon", "Trucha", "Anchoa", "Salmonete", "Pez Espada", "Rodaballo", "Bonito", "Congrio", "Cazon", "Sardina", "Caballa", "Jurel", "Lamprea"]

pg.init()
pantalla = pg.display.set_mode(RESOLUCION_PANTALLA)

#Definicion de timers
timer_1_seg = pg.USEREVENT + 1
pg.time.set_timer(timer_1_seg, 1000)
timer_40_fps = pg.USEREVENT + 2
pg.time.set_timer(timer_40_fps, 40)

#Carga de imagenes
personaje = pg.image.load("./Imagenes/personaje-frente-32-86.png")
personaje = pg.transform.scale(personaje, tamaño_personaje_frente)
fondo = pg.image.load("./Imagenes/Fondo-con-puntos.png")
fondo = pg.transform.scale(fondo, RESOLUCION_PANTALLA)
icono = pg.image.load("./Imagenes/icono.png")
boton_iniciar = pg.image.load("./Imagenes/iniciar-juego.png")
boton_iniciar = pg.transform.scale(boton_iniciar, (160, 40))


#Fuentes y textos
fuente = pg.font.SysFont("Arial", 40, True)
fuente_timer = pg.font.Font("./Fuentes/Chatsile.otf", 50)
fuente_lista = pg.font.Font("./Fuentes/HFComic.ttf", 30)
texto = fuente.render("Prueba", True, COLOR_BLANCO)
coord_texto_x = centro_pantalla(RESOLUCION_PANTALLA, texto.get_size())
coord_texto_y = 50

rect_personaje = pg.Rect(coord_personaje[0], coord_personaje[1], personaje.get_width(), personaje.get_height())
rectangulo_colision_1 = pg.draw.rect(pantalla, COLOR_BLANCO, (250, 469, 70, 90), 1)
rectangulo_colision_2 = pg.draw.rect(pantalla, COLOR_BLANCO, (390, 469, 70, 90), 1)
contador_totales_texto = fuente_lista.render (f"Total pescado: xxx", False, COLOR_NEGRO)
coord_contador_x = centro_pantalla(RESOLUCION_PANTALLA, contador_totales_texto.get_size())
coord_contador_y = 15
rectangulo_boton_iniciar = pg.draw.rect(pantalla, COLOR_BLANCO, (288, 200, 160, 40), 1)
