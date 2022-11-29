#-----------------------------------
#   CH_15_3_3_EX_1_Cancel_Apart.py   
#-----------------------------------
from sympy import *
x, y = symbols('x, y')
#----- 因式消解
print(cancel((x**2-1)/(x-1)))
print(cancel((x**3+3*x**2+3*x+1)/(x**2+x)))
#----- 真分式拆解
print(apart((x**3-1)/(x**2+1)))
print(apart((2*x)/(x**2-1)))









































	


