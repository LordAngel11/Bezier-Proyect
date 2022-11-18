import pygame
import time 
import math

#Aqui inicializamos la applicaciones de curvas de bezier
pygame.init()
pygame.display.set_caption("cubic bezier curve")
screenSize = (1280, 720)
screen = pygame.display.set_mode(screenSize)
clock = pygame.time.Clock()

#variables yo nombro
x, y = 500.0, 500.0
width, height = 70, 70
speed = 0.0001 

#Propiedades de los textos
font = pygame.font.Font("Roboto-Black.ttf", 32)
position_text1 = font.render("P0", True, (255, 255, 255), (0,0,0))
position_text2 = font.render("P1", True, (255, 255, 255), (0,0,0))
position_text3 = font.render("P2", True, (255, 255, 255), (0,0,0))
position_text4 = font.render("P3", True, (255, 255, 255), (0,0,0))

#Posiciones de los textos
textRect1 = position_text1.get_rect()
textRect2 = position_text2.get_rect()
textRect3 = position_text3.get_rect()
textRect4 = position_text4.get_rect()

path_positions = [(100.0, 600.0), (200.0, 100.0), (1000.0, 80.0), (1050.0, 610.0)]

running = True
pos_list =[]  #Lista de posiciones donde se almacenan


#Provisional 

    

while running:      #While corra    
    screen.fill((0,0,0))        #Pantalla en negro
    pygame.time.delay(500)    

    P0 = path_positions[0]      #Se le asignan las posiciones 
    P1 = path_positions[1]      
    P2 = path_positions[2]
    P3 = path_positions[3]

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            pos_list.append(event.pos)
    
    screen.fill(0)
    for x,y in pos_list:
        pygame.draw.circle(screen,(0, 255, 0),(x, y,(0,255,0), (0,255,0)), 2.5)
    
    pygame.display.update()
    clock.tick(60)
    
pygame.quit()