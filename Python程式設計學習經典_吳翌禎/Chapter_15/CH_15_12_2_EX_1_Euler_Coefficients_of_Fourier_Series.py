#------------------------------------------------------------
#   CH_15_12_2_EX_1_Euler_Coefficients_of_Fourier_Series.py   
#------------------------------------------------------------
from sympy import *
import numpy as np
x = symbols('x')
n = symbols('n', integer = True)
#----- 線性函數 (Linear function)
T = 1-0
a10 = simplify(integrate(x, (x, 0, 1))/(T/2))
a1n = simplify(integrate(x*cos(2*n*pi*x/T), (x, 0, 1))/(T/2))
b1n = simplify(integrate(x*sin(2*n*pi*x/T), (x, 0, 1))/(T/2))
a10 = trigsimp(a10)
a1n = trigsimp(a1n)
b1n = trigsimp(b1n)
print('a10 = ', a10)
print('a1n = ', a1n)
print('b1n = ', b1n)
#----- 二次式函數 (Quadratic function)
T = 1-0
a20 = simplify(integrate((-4*x**2 + 4*x), (x, 0, 1))/(T/2))
a2n = simplify(integrate((-4*x**2 + 4*x)*cos(2*n*pi*x/T), (x, 0, 1))/(T/2))
b2n = simplify(integrate((-4*x**2 + 4*x)*sin(2*n*pi*x/T), (x, 0, 1))/(T/2))
a20 = trigsimp(a20)
a2n = trigsimp(a2n)
b2n = trigsimp(b2n)
print('a20 = ', a20)
print('a2n = ', a2n)
print('b2n = ', b2n)















































	


