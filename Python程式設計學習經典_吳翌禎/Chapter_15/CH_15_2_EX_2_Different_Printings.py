#----------------------------------------
#   CH_15_2_EX_2_Different_Printings.py   
#----------------------------------------
from sympy import *
x, y = symbols('x, y')
#-----列印
print(expand((x+y)**2))
#----- 列印 LaTeX 表達式
print(latex(expand((x+y)**2)))
#-----列印 ASCII 格式
pprint(expand((x+y)**2), use_unicode=False)
#-----列印 Unicode 格式
pprint(expand((x+y)**2), use_unicode=True)

from sympy.printing.dot import dotprint
print(dotprint(expand((x+y)**2)))








































	


