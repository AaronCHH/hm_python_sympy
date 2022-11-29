#----------------------------------------------------
#   CH_15_5_EX_1_Derivatives_Partial_Derivatives.py   
#----------------------------------------------------
from sympy import *
x, y = symbols('x, y')
#----- 推求微分(Derivatives)
print(diff(x**3, x))     
print(diff(x**3, x, 2))
print(diff(x**3, x, 3))
print(diff(sin(2*x), x))
print(diff(tan(x), x))
print(diff(asin(x), x))
print(diff(exp(x), x))
print(diff(log(x), x))
#----- 推求偏微分 (Partial Derivatives)
print(diff(x**2*y**2, x))
print(diff(sin(x)*cos(y), x))
print(diff(sin(x)*cos(y), y))











































	


