#-------------------------------------
#   CH_15_6_EX_1_Series_Expansion.py   
#-------------------------------------
from sympy import *
x, y = symbols('x, y')
#----- 列印展開之級數
print(sin(x).series(x, 0, 6))
print(sin(x).series(x, 0, 6).removeO())
print(cos(x).series(x, 0, 6))
print(tan(x).series(x, 0, 6))
print(log(1-x).series(x, 0, 6))
print(besselj(0, x).series(x, 0, 6))











































	


