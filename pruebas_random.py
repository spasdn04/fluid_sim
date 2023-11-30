from Heat1 import *
import math

menu = MenuSystem()
menu.init('Python Interface', 'cool huh')

heat = Heat1()
heat.define(menu)

L2_errors = []
dt = 0.1
n = 8
for i in range(5):
    n *= 2
    grid_str = 'P=PreproBox | d=2 [0,1]x[0,1] \
        | d=2 e=ElmB4n2D div=[%d,%d] grading=[1,1]' % (n, n)
    menu.set('gridfile', grid_str)
    dt = dt/4.0; dx =1.0/n
    tip_str = 'dt=%g [0,3]' % dt
    menu.set('time parameters', tip_str)
    heat.scan()
    heat.solveProblem()
    heat.resultReport()
    L2_errors.append((dx, dt), heat.L2_error)