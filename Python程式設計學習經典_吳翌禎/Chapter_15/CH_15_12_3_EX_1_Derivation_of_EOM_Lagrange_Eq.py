#-----------------------------------------------------
#   CH_15_12_3_EX_1_Derivation_of_EOM_Lagrange_Eq.py   
#-----------------------------------------------------
from sympy import *
import numpy as np
#----- 定義符號變數
t, L, m, g = symbols('t, L, m, g')
theta, T, U, Lag, L1 = symbols('theta, T, U, Lag, L1', cls=Function)
#----- 定義位置向量
rt = Matrix([L*sin(theta(t)), -L*cos(theta(t))])
#----- 以微分推求速度向量
vt = diff(rt, t)
print('v(t) =', vt)
#----- 推求動能
T = simplify(0.5*m*transpose(vt)*vt)
print('T =', T)
#----- 推求位能
U = Matrix([[m*g*L*(1-cos(theta(t)))]])
#----- 推求 Lagrangian
Lagrangian = T- U

print('Lagrangian = ', Lagrangian)
#----- 推求運動方程式
L1 = diff(Lagrangian, Derivative(theta(t), t))
print('L1=', L1) 
Eq = diff(L1, t) - diff(Lagrangian, theta(t))
Eq1 = simplify(Eq)
print('Eq =', Eq)
print('Eq1 =', Eq1)
















































	


