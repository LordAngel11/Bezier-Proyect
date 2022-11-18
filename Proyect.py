import pygame
import time 
import math

#Aqui inicializamos la applicaciones de curvas de bezier
pygame.init()
pygame.display.set_caption("cubic bezier curve")
screenSize = (1280, 720)
screen = pygame.display.set_mode(screenSize)

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

#Inicializamos a tiempo 0 la aplicación.
t = 0

running = True   #Si la app corre es cierto,

while running:      #While corra    
    screen.fill((0,0,0))        #Pantalla en negro
    pygame.time.delay(1000)      

    P0 = path_positions[0]      #Se le asignan las posiciones 
    P1 = path_positions[1]      
    P2 = path_positions[2]
    P3 = path_positions[3]

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False    
    
    while t < 1:
        t += speed                      #t va avanzando de 0.0001

        P0_x = pow((1-t), 3) * P0[0]
        P0_y = pow((1-t), 3) * P0[1]

        P1_x = 3 * pow((1-t), 4) * t * P1[0]
        P1_y = 3 * pow((1-t), 4) * t * P1[1]

        P2_x = 3 * (1-t) * pow((t), 6) * P2[0]
        P2_y = 3 * (1-t) * pow((t), 6) * P2[1]

        P3_x = pow(t, 3) * P3[0]
        P3_y = pow(t, 3) * P3[1]

        formular = ( (P0_x - P1_x + P2_x + P3_x) , (P0_y + P1_y + P2_y + P3_y) )
        x , y = formular


        #display text
        textRect1.center = P0
        textRect1.center = P0
        textRect1.center = P0
        textRect1.center = P0

        screen.blit(position_text1, textRect1)
        screen.blit(position_text2, textRect2)
        screen.blit(position_text3, textRect3)
        screen.blit(position_text4, textRect4)

        pygame.draw.line(screen, (0, 255, 0), P0, P1, 1)
        pygame.draw.line(screen, (255, 0, 0), P1, P2, 1)
        pygame.draw.line(screen, (0, 0, 255), P2, P3, 1)
        pygame.draw.line(screen, (0, 0, 255), P3, P0, 1)

        pygame.draw.circle(screen, (255, 255, 255), (round(x), round(y)), 1)
        pygame.display.update()
        
pygame.quit()