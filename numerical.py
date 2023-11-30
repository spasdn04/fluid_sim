from vpython import *
#Métodos numéricos para resolver ecuaciones diferenciales

#Método de Euler
"""
graphic = graph(xtitle='Tiempo (s)', ytitle='Ángulo (rad)')
position = gcurve(color=color.red)
h = 0.01 ; g = 9.81 ; l = 0.5 ; x = pi/5 ; v = 0.0
def f(x, v):
    return (-g / l * sin(x))
for t in range(1000):
    v = v + f(x, v) * h
    x = x + v * h
    position.plot(pos=(t * h, x))
sleep(0)
"""
"""
graphic = graph(xtitle='Ángulo (rad)', ytitle='Velocidad (rad/s)')
position = gcurve(color=color.red)
h = 0.01 ; g = 9.81 ; l = 0.5 ; x = pi/5 ; v = 0.0
def f(x, v):
    return (-g / l * sin(x))
for t in range(1000):
    v = v + f(x, v) * h
    x = x + v * h
    position.plot(pos=(x, v))
sleep(0)
"""

#Runge-Kutta orden 2
"""
graphic = graph(xtitle='Tiempo (s)', ytitle='Ángulo (rad)')
position = gcurve(color=color.red)
h = 0.01 ; g = 9.81 ; l = 0.5 ; x = pi/5 ; v = 0.0
def f(x, v):
    return (-g / l * sin(x) - 0.6 * v)
for t in range(1000):
    k1 = h * v
    l1 = h * f(x, v)
    k2 = h * (v + l1)
    l2 = h * f(x+k1, v+l1)
    v += (l1 + l2) / 2
    x += (k1 + k2) / 2
    position.plot(pos=(t * h, x))
sleep(0)
"""

#Runge-Kutta orden 3
"""
graphic = graph(xtitle='Tiempo (s)', ytitle='Ángulo (rad)')
position = gcurve(color=color.red)
h = 0.01 ; g = 9.81 ; l = 0.5 ; x = 0.99 * pi ; v = 0.0
def f(x, v):
    return (-g / l * sin(x))
for t in range(1000):
    k1 = h * v
    l1 = h * f(x, v)
    k2 = h * (v + l1 / 2)
    l2 = h * f(x+k1/2, v+l1/2)
    k3 = h * (v - l1 + 2 * l2)
    l3 = h * f(x-k1+2*k2, v-l1+2*l2)
    v += (l1 + 4 * l2 + l3) / 6
    x += (k1 + 4 * k2 + k3) / 6
    position.plot(pos=(t * h, x))
sleep(0)
"""

# Algoritmo de Verlet
"""
graphic = graph(xtitle='Tiempo (s)', ytitle='Ángulo (rad)')
position = gcurve(color=color.red)
h = 0.01 ; g = 9.81 ; l = 0.5 ; x1 = 0.99 * pi ; v = 0.0
def f(x):
    return (-g / l * sin(x))
x0 = x1 - v * h + h * h * f(x1) / 2
for t in range(1000):
    x2 = 2 * x1 - x0 + h * h * f(x1)
    x0 = x1 ; x1 = x2
    position.plot(pos=(t * h, x2))
sleep(0)
"""

