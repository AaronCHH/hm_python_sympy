#---------------------------
#   CH_15_4_EX_1_Limits.py   
#---------------------------
from sympy import *
x, y = symbols('x, y')
#----- 推求極限 (limits)
print(limit((2*x+1)/(5*x-1), x, oo))
print(limit(1/x, x, 0))
print(limit(sin(x)/x, x, 0))
print(limit((cos(x)-1)/x, x, 0))











































	


