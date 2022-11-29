#-------------------------------------------
#   CH_15_3_4_EX_1_Trigsimp_Expand_Trig.py   
#-------------------------------------------
from sympy import *
x, y = symbols('x, y')
#----- 三角函數簡化 (trigsimp)
print(trigsimp((cos(x)**2-sin(x)**2)))
print(trigsimp(cos(x)*tan(x)))
#----- 三角函數展開 (expand_trig)
print(expand_trig(sin(x+y)))
print(expand_trig(sin(x-y)))
print(expand_trig(cos(x+y)))
print(expand_trig(cos(x-y)))
print(expand_trig(tan(x+y)))
print(expand_trig(tan(x-y)))









































	


