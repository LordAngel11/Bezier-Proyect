import pygame
import time 
import math

#Aqui inicializamos la applicacion
pygame.init()
pygame.display.set_caption("cubic bezier curve")
screenSize = (1280, 720)
screen = pygame.display.set_mode(screenSize)
clock = pygame.time.Clock()
dot_color = "green"
dot_size = 5 

##################################
#variables yo nombro##############
x, y = 500.0, 500.0
width, height = 70, 70
speed = 0.0001 
##################################
#Propiedades de los textos#######################################
font = pygame.font.Font("Roboto-Black.ttf", 32)
position_text1 = font.render("P0", True, (255, 255, 255), (0,0,0))
position_text2 = font.render("P1", True, (255, 255, 255), (0,0,0))
position_text3 = font.render("P2", True, (255, 255, 255), (0,0,0))
position_text4 = font.render("P3", True, (255, 255, 255), (0,0,0))
##################################################################

#Posiciones de los textos############
textRect1 = position_text1.get_rect()
textRect2 = position_text2.get_rect()
textRect3 = position_text3.get_rect()
textRect4 = position_text4.get_rect()
######################################
path_positions = [(100.0, 600.0), (200.0, 100.0), (1000.0, 80.0), (1050.0, 610.0)]
###################################################################################

#Lista de posiciones donde se almacenan
pos_list =[] 

running = True 
press = False

while running:      #While corra    
    screen.fill((0,0,0))        #Pantalla en negro
    pygame.time.delay(100)    
    
    #El juego va a realizar lo siguiente:
    try:
        for event in pygame.event.get():            #cerrar la app
            if event.type == pygame.QUIT:
                running = False
    
        px,py = pygame.mouse.get_pos()              #Se almacena la posicion x,y del mouse en la pantalla
        if event.type == pygame.MOUSEBUTTONDOWN:    #Si se clickea
            pos_list.append(event.pos)              #Se guardan las coordenadas actuales del mouse en el arreglo pos_list
            print(px,py)                            #Imprimimos las coordenadas almacenadas
            print(pos_list)     #Aqui imprime el arreglo de puntos.    
            
        screen.fill(0)
        for x, y in pos_list:                       #Por cada tupla (x,y) en el arreglo de tuplas pos_list se dibuja un punto verde en la posicion x,y
            pygame.draw.circle(screen,(0,255,0),(x,y),(5))
        
        if len(pos_list) >= 2:                      #Si hay mas de dos puntos en el arreglo de puntos, entonces se dibujan las lineas 
            aux = pos_list[0]
            for i in pos_list:
                pygame.draw.line(screen, (255, 255, 255), aux, i, 3)
                aux = i
            
        
        #Se actualiza el display cada vez que reseteamos uno
        if event.type == pygame.MOUSEBUTTONUP:
            press == False
        #Importante que el pygame display update quede hasta el final.
        pygame.display.update()
        
    except Exception as e:
        print(e)
        pygame.quit()
        
pygame.quit()