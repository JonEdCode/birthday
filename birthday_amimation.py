import pygame
pygame.init()
WIDTH = 600
HEIGHT = 600
TITLE = "birthday"

screen = pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption("birthday")
bd = pygame.image.load("birthday.jpg")
bd2 = pygame.image.load("cake.jpg")
bd3 = pygame.image.load("presant.jpg")
run = True
while run  == True:
    screen.blit(bd,(0,0))
    font = pygame.font.SysFont("sherif",50)
    words = font.render("happy birthday!",True,"black")
    screen.blit(words,(180,300))
    pygame.display.update()
    
    pygame.time.delay(3000)
    screen.blit(bd2,(0,0))
    pygame.display.update()

    pygame.time.delay(3000)
    screen.blit(bd3,(0,0))
    pygame.display.update()
    pygame.time.delay(3000)



    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False 


    pygame.display.update()
