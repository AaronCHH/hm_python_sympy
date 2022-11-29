#--------------------------------------------
#   CH_15_3_5_EX_1_Logcombine_Expand_Log.py   
#--------------------------------------------
from sympy import *
x, y = symbols('x, y')
#----- 對數函數組合 (logcombine)
print(logcombine(log(x)+log(y), force = True))
print(logcombine(log(x)-log(y), force = True))
#----- 對數函數展開 (expand_log)
print(expand_log(log(x*y), force = True))
print(expand_log(log(x/y), force = True))
print(expand_log(log(x**3), force = True))










































	


