import pygame, sys, time, random

# pantalla de juego 

pygame.init()

play_surface = pygame.display.set_mode((500, 500))

font = pygame.font.Font(None, 30)

fps = pygame.time.Clock()

# funcion para que las manzanas aparezcan de manera aleatoria en la pantalla
def comida():
    random_pos = random.randint(0,49)*10
    manzana = [random_pos, random_pos]
    return manzana


def juego():
# caracteristicas inciales de el personaje y el juego
    cabeza = [100, 50]
    cuerpo = [[100,50],[90,50],[80,50]]
    change = "RIGHT"
    run = True
    manzana = comida()
    score = 0

    while run:
# loop para los movimientos del personaje
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RIGHT:
                    change = "RIGHT"
                if event.key == pygame.K_LEFT:
                    change = "LEFT"
                if event.key == pygame.K_UP:
                    change = "UP"
                if event.key == pygame.K_DOWN:
                    change = "DOWN"
        # Defnición de movimientos            
        if change == "RIGHT":
            cabeza[0] += 10
        if change == "LEFT":
            cabeza[0] -= 10
        if change == "UP":
            cabeza[1] -= 10
        if change == "DOWN":
            cabeza[1] += 10

        cuerpo.insert(0, list(cabeza))
        # Aumento score - aumento cuerpo
        if cabeza == manzana:
            manzana= comida()
            score += 1
            print(score)
        else:
            cuerpo.pop()
        # Si choca consimismo pierde
        head = cuerpo[-1]
        for i in range(len(cuerpo) - 1): 
            part = cuerpo[i]
            if head[0] == part[0] and head[1] == part[1]:
                run = False
                print("YOU LOSE")


        play_surface.fill((0,0,0))

        for pos in cuerpo:
            pygame.draw.rect(play_surface,(200,200,200), pygame.Rect(pos[0], pos[1], 10, 10))
        
        pygame.draw.rect(play_surface,(169,6,6), pygame.Rect(manzana[0], manzana[1], 10, 10))
        
        text = font.render(str(score),0,(200,60,80))
        play_surface.blit(text, (480,20))

        # Aumento de velocidad
        if score < 10:
            fps.tick(10)
        if score >= 10:
            fps.tick(20)
        # si choca contra las paredes de la pantalla pierde
        if cabeza[0] <= 0 or cabeza[0] >= 500:
            run = False
            print("YOU LOSE")
        if cabeza[1] <= 0 or cabeza[1] >= 500:
            run = False
            print("YOU LOSE")

        pygame.display.flip()

juego()

pygame.quit()