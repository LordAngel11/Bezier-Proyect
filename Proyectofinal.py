import pygame, sys
from pygame.locals import *
import math

press = False


pygame.init()

#tamño de la ventana 
screensize =(800, 500)

#crear ventana 
screen = pygame.display.set_mode(screensize)


#nombre de la ventana 
pygame.display.set_caption("Proyecto")

#Lista de posiciones donde se almacenan
pos_list =[] 
t=0
speed = 0.0001 
x,y =(0,0)
font = pygame.font.Font("BungeeShade-Regular.ttf", 22) 

text1 = font.render("¡Bienvenido!", 0, (255,255,255), (0,0,0))
text2 = font.render("Ingrese el orden de la curva ", 0, (255,255,255), (0,0,0))
text3 = font.render("Ingrese los puntos", 0, (255,255,255), (0,0,0))
texttime = font.render("t = ", 0, (255,255,255), (0,0,0))

#texto de bienvenida
screen.blit(text1, (260,100))
screen.blit(text2, (160,130)) 

# el ciclo es miestras no precionen salir
while True:
    #cambia el color a mi ventana 
    #screen.fill(color)

    try:
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                #Cerrar la ventana
                pygame.quit()
                sys.exit()

            #entra el orden de la curva
            if evento.type == pygame.KEYDOWN:
                #print(evento.unicode)
                n = int(evento.unicode)
                screen.fill((0, 0, 0))
                screen.blit(text3, (260,100))
                   

            #entran los puntos
            if evento.type == pygame.MOUSEBUTTONDOWN:
                pos_list.append(evento.pos)  
                #print(pos_list)  #no es necesario ver las impresiones de animación 
                
                for x, y in pos_list:                                   #Por cada tupla (x,y) en el arreglo de tuplas pos_list se dibuja un punto verde en la posicion x,y
                    pygame.draw.circle(screen,(255,255,255),(x,y),(4))
                
                if len(pos_list) == n:
                    for j in range(n-1):
                        pygame.draw.line(screen, (0, 255, 0), pos_list[j], pos_list[j+1], 1)
                    while t < 1:
                        t += speed
                        m = n-1
                        for i in range(n): #generalización de las curvas de bezier
                            x += math.comb(m,i) * pos_list[i][0] * pow((1-t), (m-i)) * pow(t, i)
                            y += math.comb(m,i) * pos_list[i][1] * pow((1-t), (m-i)) * pow(t, i)
                        x=x/10
                        y=y/10
                       #animacion
                        pygame.draw.circle(screen, (255, 0, 0), ((x*10)-30, (y*10)-30), 1)
                        #seconds = pygame.time.get_ticks()/10000
                        #seconds = str(seconds)
                        #counter = font.render(seconds,0,(255,255,255))
                        #screen.blit(counter,(700,100))
                        pygame.display.update()
                        
            

    except Exception as e:
        print(e)
        pygame.quit()
        sys.exit()




    pygame.display.update()

