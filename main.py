import pygame as pg
import random
from Funciones import *
from Auxiliares import *
from Sonidos import *

#Iniciamos pygame
pg.init()

#Le ponemos un nombre a la ventana.
pg.display.set_caption("Juego de pesca")
#Le ponemos un icono a la ventana.
pg.display.set_icon(icono)

#Sonidos y música
sonido_juego = Sonido()
sonido_juego.play_musica (SONIDO_MUSICA)

#Iniciamos el bucle del juego
juego_corriendo = True

#Bucle del juego
while juego_corriendo:
    rectangulo_mouse = pg.draw.rect(pantalla, COLOR_BLANCO, (coord_mouse[0], coord_mouse[1], 2, 2), 1)
    #Lista de eventos de juego
    lista_eventos = pg.event.get()
    tiempo_actual = pg.time.get_ticks()

    for evento in lista_eventos:
        #Botón X (Salir)
        if evento.type == pg.QUIT:
            #print (evento, evento.type)
            juego_corriendo = False
            sonido_juego.stop_musica
        #Temporizador
        #if evento.type == timer_1_seg:
            #if tiempo_limite > 0:
                #tiempo_limite -= 1 
        if evento.type == pg.KEYDOWN:
            if evento.key == pg.K_e:
                if rect_personaje.colliderect(rectangulo_colision_1):
                    sonido_juego.play_sonido(SONIDO_REEL)
                    personaje = pg.image.load("./Imagenes/personaje-espaldas-sentado-33-68.png")
                    personaje = pg.transform.scale(personaje, tamaño_personaje_frente)
                if rect_personaje.colliderect(rectangulo_colision_2):
                    sonido_juego.play_sonido(SONIDO_REEL)
                    personaje = pg.image.load("./Imagenes/personaje-espaldas-sentado-33-68.png")
                    personaje = pg.transform.scale(personaje, tamaño_personaje_frente)
                                
            if pesca == True:
                if evento.key == pg.K_SPACE:
                    if tiempo_actual - ultima_pesca >= cooldown:
                        #sonido_juego.play_sonido(SONIDO_VOLVIENDO_REEL)
                        pez = random.choice(peces)
                        if rect_personaje.colliderect(rectangulo_colision_1):
                            contador_peces[pez][0] += 1
                            contador_total +=1
                        if rect_personaje.colliderect(rectangulo_colision_2):
                            contador_peces[pez][1] += 1
                            contador_total +=1
                        pez = random.choice(peces)  
                        cooldown = random.choice(tiempos_de_pesca)
                        print (contador_total)
                        ultima_pesca = tiempo_actual
                        sonido_juego.play_sonido(SONIDO_REEL)
                    else:
                        print ("Prueba",cooldown)
                if evento.key == pg.K_x:
                    movimiento = True
                    pesca = False
                    fondo = pg.image.load("./Imagenes/Fondo-con-puntos.png")
                    personaje = pg.image.load("./Imagenes/personaje-espaldas-32-84.png")
                    personaje = pg.transform.scale(personaje, tamaño_personaje_frente)

#Eventos de mouse
        if evento.type == pg.MOUSEBUTTONDOWN:
            coord_mouse = evento.pos
            print(evento.pos) 
            print("M",coord_mouse)  
            if rectangulo_mouse.colliderect(rectangulo_boton_iniciar):
                    print("Botón de inicio clickeado")
                    jugando = True
    # if evento.type == pg.MOUSEBUTTONUP:
    #     pass
    # if evento.type == pg.MOUSEWHEEL:
    #     pez = random.choice(peces)  
    #     contador_peces[pez] += 1

#Eventos de teclado (Tecla presionada)
        lista_tecla_presionada = pg.key.get_pressed()
        if lista_tecla_presionada:
            if movimiento == True:
                if lista_tecla_presionada[pg.K_LSHIFT]:
                    velocidad = velocidad_correr
                else:
                    velocidad = velocidad_normal

                if lista_tecla_presionada[pg.K_w]:
                    if lista_tecla_presionada[pg.K_LSHIFT]:
                        personaje = pg.image.load("./Imagenes/personaje-corriendo-espalda-32-81.png")
                        personaje = pg.transform.scale(personaje, tamaño_personaje_frente)
                    else:
                        personaje = pg.image.load("./Imagenes/personaje-espaldas-32-84.png")
                        personaje = pg.transform.scale(personaje, tamaño_personaje_frente)
                    if coord_personaje[1] > 472:
                        sonido_juego.play_sonido(SONIDO_PASOS)
                        coord_personaje[1] -= velocidad
                        rect_personaje.y = coord_personaje[1]
                if lista_tecla_presionada[pg.K_s]:
                    if lista_tecla_presionada[pg.K_LSHIFT]:
                        personaje = pg.image.load("./Imagenes/personaje-corriendo-frente-30-79.png")
                        personaje = pg.transform.scale(personaje, tamaño_personaje_frente)
                    else:
                     personaje = pg.image.load("./Imagenes/personaje-frente-32-86.png")
                     personaje = pg.transform.scale(personaje, tamaño_personaje_frente)
                    if coord_personaje[1] < 515:
                        sonido_juego.play_sonido(SONIDO_PASOS)
                        coord_personaje[1] += velocidad
                        rect_personaje.y = coord_personaje[1]
                if lista_tecla_presionada[pg.K_a]:
                    if lista_tecla_presionada[pg.K_LSHIFT]:
                        personaje = pg.image.load("./Imagenes/personaje-corriendo-izquierda-36-78.png")
                        personaje = pg.transform.scale(personaje, tamaño_personaje_frente)
                    else:
                     personaje = pg.image.load("./Imagenes/personaje-izquierda-33-81.png")
                     personaje = pg.transform.scale(personaje, tamaño_personaje_frente)
                    if coord_personaje[0] > 0:
                        sonido_juego.play_sonido(SONIDO_PASOS)
                        coord_personaje[0] -= velocidad
                        rect_personaje.x = coord_personaje[0]
                if lista_tecla_presionada[pg.K_d]:
                    if lista_tecla_presionada[pg.K_LSHIFT]:
                        personaje = pg.image.load("./Imagenes/personaje-corriendo-derecha-35-78.png")
                        personaje = pg.transform.scale(personaje, tamaño_personaje_frente)
                    else:
                     personaje = pg.image.load("./Imagenes/personaje-derecha-33-80.png")
                     personaje = pg.transform.scale(personaje, tamaño_personaje_frente)
                    if coord_personaje[0] < 765:
                        sonido_juego.play_sonido(SONIDO_PASOS)
                        coord_personaje[0] += velocidad
                        rect_personaje.x = coord_personaje[0]
                if lista_tecla_presionada[pg.K_UP]:
                    if lista_tecla_presionada[pg.K_LSHIFT]:
                        personaje = pg.image.load("./Imagenes/personaje-corriendo-espalda-32-81.png")
                        personaje = pg.transform.scale(personaje, tamaño_personaje_frente)
                    else:
                        personaje = pg.image.load("./Imagenes/personaje-espaldas-32-84.png")
                        personaje = pg.transform.scale(personaje, tamaño_personaje_frente)
                    if coord_personaje[1] > 472:
                        sonido_juego.play_sonido(SONIDO_PASOS)
                        coord_personaje[1] -= velocidad
                        rect_personaje.y = coord_personaje[1]
                if lista_tecla_presionada[pg.K_DOWN]:
                    if lista_tecla_presionada[pg.K_LSHIFT]:
                        personaje = pg.image.load("./Imagenes/personaje-corriendo-frente-30-79.png")
                        personaje = pg.transform.scale(personaje, tamaño_personaje_frente)
                    else:
                        personaje = pg.image.load("./Imagenes/personaje-frente-32-86.png")
                        personaje = pg.transform.scale(personaje, tamaño_personaje_frente)
                    if coord_personaje[1] < 515:
                        sonido_juego.play_sonido(SONIDO_PASOS)
                        coord_personaje[1] += velocidad
                        rect_personaje.y = coord_personaje[1]
                if lista_tecla_presionada[pg.K_LEFT]:
                    if lista_tecla_presionada[pg.K_LSHIFT]:
                        personaje = pg.image.load("./Imagenes/personaje-corriendo-izquierda-36-78.png")
                        personaje = pg.transform.scale(personaje, tamaño_personaje_frente)
                    else:
                        personaje = pg.image.load("./Imagenes/personaje-izquierda-33-81.png")
                        personaje = pg.transform.scale(personaje, tamaño_personaje_frente)
                    if coord_personaje[0] > 0:
                        sonido_juego.play_sonido(SONIDO_PASOS)
                        coord_personaje[0] -= velocidad
                        rect_personaje.x = coord_personaje[0]
                if lista_tecla_presionada[pg.K_RIGHT]:
                    if lista_tecla_presionada[pg.K_LSHIFT]:
                        personaje = pg.image.load("./Imagenes/personaje-corriendo-derecha-35-78.png")
                        personaje = pg.transform.scale(personaje, tamaño_personaje_frente)
                    else:
                        personaje = pg.image.load("./Imagenes/personaje-derecha-33-80.png")
                        personaje = pg.transform.scale(personaje, tamaño_personaje_frente)
                    if coord_personaje[0] < 765:
                        sonido_juego.play_sonido(SONIDO_PASOS)
                        coord_personaje[0] += velocidad
                        rect_personaje.x = coord_personaje[0]
                if lista_tecla_presionada[pg.K_e]:
                    movimiento = False
                    fondo = pg.image.load("./Imagenes/Fondo.png")
                    pesca = True
                if rect_personaje.colliderect(rectangulo_colision_1):
                    pass
                if rect_personaje.colliderect(rectangulo_colision_2):
                    pass
            # if lista_tecla_presionada[pg.K_x]:
            #     movimiento = True
            #     pesca = False
            #     fondo = pg.image.load("./Imagenes/Fondo-con-puntos.png")
#Cargas en la pantalla
    #Fondo
    pantalla.blit(fondo, COORD_FONDO)
    if jugando == False:
        fondo = pg.image.load("./Imagenes/Fondo-libre.png")
        pantalla.blit(boton_iniciar, (coord_contador_x, 200))
        movimiento = False
    else:
        if pesca == False:
            movimiento = True
            fondo = pg.image.load("./Imagenes/Fondo-con-puntos.png")
        pantalla.blit(personaje, coord_personaje)
        contador_totales1 = fuente_lista.render (f"Total pescado: {contador_total}", True, COLOR_NARANJA)
        pantalla.blit(contador_totales1, (coord_contador_x, coord_contador_y))
        contador_totales = fuente_lista.render (f"Total pescado: {contador_total}", False, COLOR_NEGRO)
        pantalla.blit(contador_totales, (coord_contador_x, coord_contador_y))
    if modo_test:
        pg.draw.rect(pantalla, COLOR_BLANCO, rectangulo_colision_1, 1)
        pg.draw.rect(pantalla, COLOR_BLANCO, rectangulo_colision_2, 1)
        pg.draw.rect(pantalla, COLOR_NEGRO, rectangulo_mouse, 2)
        if jugando == False:
            pg.draw.rect(pantalla, COLOR_ROJO, rectangulo_boton_iniciar, 1)
    #Personaje
    pg.draw.rect(pantalla, COLOR_CELESTE, rect_personaje, 1)
    #pantalla.blit(personaje, coord_personaje)
    #Colisiones 
    if pesca == True:
        lista_tecla_presionada = pg.key.get_pressed()
        if lista_tecla_presionada:
            if lista_tecla_presionada[pg.K_l]:
                y_offset = 5  
                for pez, contador in contador_peces.items():
                    lista_de_peces = fuente_lista.render(f"{pez}: {contador}", False, COLOR_ROJO)
                    pantalla.blit(lista_de_peces, (5, y_offset))
                    y_offset += 25
            elif():
                pass
    # contador_totales1 = fuente_lista.render (f"Total pescado: {contador_total}", True, COLOR_NARANJA)
    # pantalla.blit(contador_totales1, (coord_contador_x, coord_contador_y))
    # contador_totales = fuente_lista.render (f"Total pescado: {contador_total}", False, COLOR_NEGRO)
    # pantalla.blit(contador_totales, (coord_contador_x, coord_contador_y))

    pg.display.flip()
#Fin del juego
pg.quit()
exit()
