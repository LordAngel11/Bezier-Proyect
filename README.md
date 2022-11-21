# Proyecto Curvas de Bezier 
## Luz Ahide Gallardo y Juan Angel López Delgadillo.
## Métodos Numericos



### Curva Lineal

Dados los puntos $P_0$ y $P_1$, una curva lineal de Bézier es una línea recta entre los dos puntos. La curva viene dada por la expresión:

$$
    B(t) = P_0 + (P_1 + P_0) t = (1-t)P_0
 + tP_1,
 $$
 donde $t \in [0,1]$

 ### Curva Cuadratica 

 UNa curva cuadrática de Bezier es el camino trazado por la función $B(t)$, dados los puntos: $P_0$, $P_1$ y $P_2$

$$
B(t) = (1-t)^{2} P_0 + 2t(1-t)P_1 + t_2P_2,
$$
donde $t \in [0,1].$

### Curvas cúbicas de Bézier 

Cuando tenemos cuatro puntos del plano o del espacio tridimensional $P_0$, $P_1$, $P_2$ y $P_3$ se definen una curva cúbica de Bézier. La curva comienza en el punto $P_0$ y se dirige hacia $P_1$ y llega a $P_3$ vinibiendo de la dirección del punto $P_2$. Usualmente, no pasará ni por $P_1$ ni por $P_2$. Estos puntos solo están ahí para proporcionar información direccional. La distancia entre $P_0$ y $P_1$ determina "que longitud" tiene la curva cuando se mueve hacia la dirección de $P_2$ antes de dirigirse hacia $P_3$. La forma de la curva es:
$$
B(t) = (1-t)^{2}P_0 + 2t(1-t)P_1 + t^{2}P_2,
$$
donde $t \in [0,1]$

### Generalización de una curva de Bezier.

La generalización de las curvas se les denomina splines. De este modo la curva spline de grado $n$ esta generalizada de la siguiente forma. Dado los puntos $P_0, P_1, \dots, P_n$, la curva de Bezier es del tipo:

 $$
    B(t) = \sum_{i = 0}^{n} {n\choose{i}} P_i(1 - t)^{n-i}t^{i},
 $$
 donde es obvio que $t \in [0,1]$

Una vez hecho el resumen rapido de lo que es una curva de bezier vamos a pasar a explicar nuestro proyecto:

## Detalles Técnicos.

Nuestra proyecto consiste en una aplicación iteractiva que permite al usuario generar curvas de bezier de cualquier orden utilizando solo el ratón. Para esto  vamos a utilizar la librería de Pygame para llevar a cabo el proyecto. Así pues importamos las siguientes librerías.

```
import pygame, sys
from pygame.locals import *
import math
```
(Es necesario importar math ya que este nos permitira generalizar las curvas de bezier). 
Luego lo que se hace es inicializar nuestra aplicación definiendo el tamaño de la pantalla y creando el display.

```
#tamaño de la ventana
screensize = (800,500) #800 x 500 pixeles.

#crear ventana.
screen = pygame.display.set_mode(screensize) 

#nombre de la ventana
pygame.display.set_caption("Proyecto")
```
Una vez creado el display de la aplicación vamos a generar un arreglo de tuplas donde cada tupla almacena las coordenadas $(x,y)$ del mouse con respecto a la ventana al momento de dar click, también vamos a definir nuestra variable $t = 0$ y una variable auxiliar $speed = 0.0001$ en la cual va a permitir variar $t$ en el tiempo con respecto a la animación de la curva, de este modo tenemos que 
``` 
#Lista de posiciones donde se almacenan
pos_list = []
t = 0
speed = 0.0001
(x,y) = (0,0)
```
Luego al iniciar la aplicación lo que vamos a hacer es lo siguiente. Primero  vamos a habilitar una opción que le permita al usuario ingresar el orden de la curva en una variable $n$ antes de asignar puntos de manera libre. 
```
#Mientras el programa corra
while True:
   
   try:  #Va a intentar para cada evento de la ventana

      for evento in pygame.even.get():
      #Este caso es para cerrar el juego.
         if evento.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
   
         #Aqui es donde en la pantalla aparece la indicación y el usuario guarda el orden de la curva.
         if evento.type == pygame.KEYDOWN:
            n = int(evento.unicode)
            screen.fill((0, 0, 0))
            screen.blit(text3, (260,100))

```

Una vez almacenado el orden de la curva en la variable $n$, entonces la aplicación va a permitir al usuario dibujar los puntos $P$ que definen la curva de Bezier. 

```
         if evento.type == pygame.MOUSEBUTTONDOWN:
            pos_list.append(evento.pos) 

            #Por cada tupla (x,y) en el arreglo de tuplas pos_list se dibuja un punto verde en la posicion x,y

               for x, y in pos_list:  
                  pygame.draw.circle(screen,(255,255,255),(x,y),(4))
```
Estos se almacenan en el arreglo de tuplas "pos_list" y en cada tupla se amacenan la coordenadas $(x,y)$ de donde se hizo el click. Ademas de que la función "pygame.draw.circle" permite dibujar un punto en donde se dio el click.

Una vez que se dibujaron todos los puntos se van a dibujar las lineas que uniran los puntos y se va a proceder con la animación de la curva.

```
         if len(pos_list) == n:
            for j in range(n-1):
               pygame.draw.line(screen, (0, 255, 0), pos_list[j], pos_list[j+1], 1)
```

Para la animación de la curva recordemos que la generalización de la curva de Bezier esta dada por 
$$
B(t) = \sum_{i = 0}^{n}{n \choose{i}}P_i(1-t)^{n-i}t^{i}. 
$$
De este modo para cada $i = 1,\dots,n$ se realiza lo siguiente
```
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

                  pygame.display.update()
```
## Conclusiones

Una vez realizado el proyecto una de las conclusiones a las que llegamos fue de que el control de la curva es global, esto quiere decir que al modificar un punto de control implica modificar completamente la curva, esto lo puede verificar volviendo a correr la aplicación y generar un punto en alguna otra parte. 

Luego también se puede observar que la curva se puede ver como una linea recta si y solo si todos sus segmentos estan completamente alineados. 

FInalmente con este proyecto podemos observar que una de las aplicaciónes de las curvas de Bézier consiste en la descripción de pasos para el movimiento de objetos en animaciónes enfocadas en cualquier tipo de industria (Animación, Videojuegos, Astronomía, etc.)

### Referencias

- https://www.pygame.org/docs/