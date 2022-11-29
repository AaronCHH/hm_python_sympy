#-----------------------------------------------------
#   CH_15_7_EX_1_Integration_Multiple_Integration.py   
#-----------------------------------------------------
import math
from sympy import *
x, y = symbols('x, y')
#----- 不定積分 (Indefinite Integration) 
print(integrate(x**2, x))
print(integrate(cos(x), x))
print(integrate(1/x, x))
print(integrate(exp(x), x))
#----- 定積分(Definite Integration)
print(integrate(x**2, (x, 0, 1)))
print(integrate(cos(x), (x, 0, math.pi/2)))
print(integrate(1/x, (x, 1, 2)))
print(integrate(exp(x), (x, 0, 2)))
#-----  二重積分 (Double Integration)
print(integrate(x*y, x, y))
print(integrate(exp(-x**2-y**2), (x, -oo, oo), (y, -oo, oo)))












































	


