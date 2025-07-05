import pygame, sys
#from button import Button

pygame.init()

WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Aim Trainer")

start = pygame.image.load('STARTBUTTON.png')

for event in pygame.event.get():
        if event.type == pygame.MOUSEBUTTONDOWN:
            print("Start")  
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                run = False
        if event.type == pygame.QUIT:
            run = False

        pygame.display.update()

pygame.quit()