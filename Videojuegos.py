import pygame
from pygame.locals import *
import sys
pygame.init()


# Crear display window
altura = 700
ancho = 1200

screen = pygame.display.set_mode((ancho, altura))
pygame.display.set_caption('Videojuegos')
fuente=pygame.font.Font(None,50)
text="Videojuegos para tu entretenimiento :)"
mensaje=fuente.render(text,1,(255,255,255))

mensaje_rect = mensaje.get_rect()
mensaje_rect.centerx = screen.get_rect().centerx

star_img = pygame.image.load('Pacman.png').convert_alpha()
star_img2 = pygame.image.load('serpiente.png').convert_alpha()
star_img3 = pygame.image.load('dinosaurio.png').convert_alpha()

class button():
    def __init__(self,x,y, image):
        self.image= image
        self.rect = self.image.get_rect()
        self.rect.topleft = (x,y)
    def dibujo(self):
        screen.blit(self.image,(self.rect.x, self.rect.y))


star_button = button(100,200, star_img)
star_button2 = button(450,200, star_img2)
star_button3 = button(800,200, star_img3)


#game loop
run = True
while run:
    screen.fill((0,0,0))
    #screen.blit(mensaje,(15,10))
    screen.blit(mensaje, mensaje_rect)
    star_button.dibujo()
    star_button2.dibujo()
    star_button3.dibujo()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    pygame.display.update()
 
    

pygame.quit()
