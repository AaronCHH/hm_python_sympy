#------------------------------------
#   CH_15_3_2_EX_1_Expand_Factor.py   
#------------------------------------
from sympy import *
x, y = symbols('x, y')
#----- 多項式函數展開
print(expand((x-1)**3))
print(expand((x-1)*(x+1)*(x+2)))
#----- 多項式函數因式分解
print(factor(x**3 - 3*x**2 + 3*x - 1))
print(factor(x**3 + 2*x**2 - x - 2))








































	


