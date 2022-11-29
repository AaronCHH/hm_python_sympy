#-------------------------------
#   CH_15_3_1_EX_1_Simplify.py   
#-------------------------------
from sympy import *
x, y = symbols('x, y')
#----- 多項式函數
print(simplify((1+x)**2-(1-x)**2))
print(simplify(1+1/(x+2)))
print(simplify((x**2-1)/(x+1)))
print(simplify(sqrt(x)*sqrt(x)+1))
#----- 三角函數
print(simplify(sin(x)*cos(y)+sin(y)*cos(x)))
print(simplify(2*sin(x)*cos(x)))
print(simplify(4*cos(x)**3 - 3*cos(x)))
#----- 雙曲三角函數
print(simplify((exp(x)-exp(-x))/2))
print(simplify((exp(x)+exp(-x))/2))
print(simplify((exp(x)-exp(-x))/(exp(x)+exp(-x))))
#----- 指數與對數函數
print(simplify(exp(x)/exp(y)))
print(simplify(1/(1+exp(-x))))
print(simplify(exp(log(x+2))))
#----- 特殊函數
print(simplify(gamma(x)/gamma(x-3)))
print(simplify(besselj(0, 0)-besselj(1, 0)))
print(simplify(besseli(0, 0)-besseli(1, 0)))
print(simplify(legendre(2, x)))
print(simplify(hermite(2, x)))








































	


