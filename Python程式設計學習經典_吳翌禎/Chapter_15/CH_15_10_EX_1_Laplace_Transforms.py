#----------------------------------------
#   CH_15_10_EX_1_Laplace_Transforms.py   
#----------------------------------------
from sympy import *
x, s, a = symbols('x, s, a')
#-----列示Laplace 轉換結果
print(integrate(1*exp(-s*x), (x, 0, oo)))
print(integrate(x*exp(-s*x), (x, 0, oo)))
print(integrate(x**2*exp(-s*x), (x, 0, oo)))
print(integrate(sin(x)*exp(-s*x), (x, 0, oo)))
print(integrate(cos(x)*exp(-s*x), (x, 0, oo)))
print(integrate(sinh(x)*exp(-s*x), (x, 0, oo)))
print(integrate(cosh(x)*exp(-s*x), (x, 0, oo)))
print(integrate(exp(a*x)*exp(-s*x),(x, 0, oo) ))















































	


