#----------------------------------------------
#   CH_15_8_EX_1_Roots_Algebraic_Equations.py   
#----------------------------------------------
import math
from sympy import *
x, y, a, b, c = symbols('x, y, a, b, c')
#----- 列印求根結果 (用 solve)
print(solve(a*x**2 + b*x + c, x))
print(solve(x**2 - x - 2, x))
print(solve(x**2 - 2*x + 1, x))
print(solve(x**2 + x + 4, x))
#----- 列印求根結果 (用 roots)
print(roots(x**2-1))
print(roots(x**2+1))













































	


