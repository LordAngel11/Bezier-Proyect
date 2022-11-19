# Proyecto Curvas de Bezier 
## Luz Ahide Gallardo y Juan Angel López Delgadillo.
### Métodos Numericos



### Curva Lineal

Dados los puntos $P_0$ y $P_1$, una curva lineal de Bézier es una línea recta entre los dos puntos. La curva viene dada por la expresión:

$$
    B(t) = P_0 + (P_1 + P_0) t = (1-t)P_0
 + tP_1,
 $$
 donde $t \in [0,1]$

 La generalización de las curvas se les denomina splines. De este modo la curva spline de grado $n$ esta generalizada de la siguiente forma. Dado los puntos $P_0, P_1, \dots, P_n$, la curva de Bezier es del tipo:

 $$
    B(t) = \sum_{i = 0}^{n} {n\choose{i}} P_i(1 - t)^{n-i}t^{i},
 $$
 donde es obvio que $t \in [0,1]$

Una vez hecho el resumen rapido de lo que es una curva de bezier vamos a pasar a explicar nuestro proyecto:

## Detalles Técnicos.

Nuestra proyecto consiste en una aplicación iteractiva que permite al usuario generar curvas de bezier de cualquier orden utilizando solo el ratón. Para esto tenemos vamos a utilizar las librería de Pygame para llevar a cabo el proyecto.

