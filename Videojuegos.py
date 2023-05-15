import pygame
from pygame.locals import *
import sys
pygame.init()
import os
import subprocess

# Crear ventana principal
altura = 700
ancho = 1200

screen = pygame.display.set_mode((ancho, altura))
pygame.display.set_caption('Videojuegos')
fuente=pygame.font.Font(None,50)#fuente(fuente tipo, fuente tamaño)
text="Videojuegos para tu entretenimiento :)"
mensaje=fuente.render(text,1,(255,255,255))

mensaje_rect = mensaje.get_rect() 
mensaje_rect.centerx = screen.get_rect().centerx

# Se agregan las imagenes  
star_img = pygame.image.load('Pacman.png').convert_alpha()
star_img2 = pygame.image.load('dinosaurio.png').convert_alpha()
star_img3 = pygame.image.load('serpiente.png').convert_alpha()

class button():
    # funcionalidad imagenes
    def __init__(self,x,y, image):
        self.image= image
        self.rect = self.image.get_rect()
        self.rect.topleft = (x,y)
        self.clicked = False
    def dibujo(self):
        action= False
        # optener posición del mouse
        pos = pygame.mouse.get_pos()
        

        # verificar si el mouse esta sobre la imagen y si se presiona
        if self.rect.collidepoint(pos):
            if pygame.mouse.get_pressed()[0] == 1 and self.clicked == False:
                self.clicked = True
                action= True
                
            if pygame.mouse.get_pressed()[0] == 0:
                self.clicked = False


        screen.blit(self.image,(self.rect.x, self.rect.y))
        return action

# Se le asigna posición a cada uno de las imagenes en la pantalla

star_button = button(100,200, star_img)
star_button2 = button(450,200, star_img2)
star_button3 = button(800,200, star_img3)


# loop principal de la interfaz principal 
run = True
while run:
    screen.fill((0,0,0))
    screen.blit(mensaje, mensaje_rect)
# se importo subprocess para ejecutar los juegos
    if star_button.dibujo():
        subprocess.run(['python','pacman.py'])
    if star_button2.dibujo():
        subprocess.run(['python','dinosaurio.py'])
    if star_button3.dibujo():
        subprocess.run(['python','snake.py'])

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        

    pygame.display.update()
 
    

pygame.quit()
