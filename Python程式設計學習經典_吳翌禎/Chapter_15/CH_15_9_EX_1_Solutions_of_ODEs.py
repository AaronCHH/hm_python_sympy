#--------------------------------------
#   CH_15_9_EX_1_Solutions_of_ODEs.py   
#--------------------------------------
from sympy import *
x, y, a, b, c = symbols('x, y, a, b, c')
f, g = symbols('f, g', cls = Function)
#-----一階齊性微分方程 (1st-order homogeneous ODE)
print(dsolve(Eq(f(x).diff(x) - f(x)), f(x)))
print(dsolve(Eq(f(x).diff(x) + f(x)), f(x)))
#-----一階非齊性微分方程 (1-st order nonhomogeneous ODE)
print(dsolve(Eq(f(x).diff(x) - f(x), exp(-2*x)), f(x)))
#-----一階非線性微分方程 (1-st order nonlinear ODE)
print(dsolve(Eq(f(x).diff(x) - 1 - f(x)/x - f(x)**2/x**2), f(x)))
#------一階 Bounoulli微分方程 (1-st order Bernoulli Eq.)
print(dsolve(Eq(f(x).diff(x) - f(x), f(x)**2), f(x)))
#-----二階常係微分方程 (2nd-order ODE with constant coefficients)
print(dsolve(Eq(f(x).diff(x,2)-2*f(x).diff(x)-3*f(x)),f(x)))
print(dsolve(Eq(f(x).diff(x,2)-2*f(x).diff(x)-3*f(x), exp(x)),f(x)))
#-----二階等維微分方程 (2nd-order Euler-Cauchy ODE)
print(dsolve(Eq(x**2*f(x).diff(x,2) - x*f(x).diff(x) - 3*f(x)),f(x)))
print(dsolve(Eq(x**2*f(x).diff(x,2) - x*f(x).diff(x) - 3*f(x), x),f(x)))














































	


