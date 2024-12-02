import pygame.mixer as mixer


class Sonido:

    def _init_():
        mixer.init()

    def play_sonido(self, ruta_sonido: str):
        Sonido = mixer.Sound(ruta_sonido)
        Sonido.set_volume(0.4)
        Sonido.play()
    
    def play_musica(self, ruta_musica: str):
        mixer.music.load(ruta_musica)
        mixer.music.set_volume(0.3)
        mixer.music.play()
    
    def stop_musica (self):
        mixer.music.fadeout(2500)

    def stop_sonido (self):
        Sonido.stop()
    

