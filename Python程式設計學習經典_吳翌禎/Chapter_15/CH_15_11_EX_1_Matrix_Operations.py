#---------------------------------------
#   CH_15_11_EX_1_Matrix_Operations.py   
#---------------------------------------
from sympy import *
import numpy as np
a11, a12, a21, a22 = symbols('a11, a12, a21, a22')
b11, b12, b21, b22 = symbols('b11, b12, b21, b22')
#-----矩陣定義 (Matrix Definition)
matA = Matrix([[a11, a12], [a21, a22]])
matB = Matrix([[b11, b12], [b21, b22]])
print(matA)
print(matB)
#-----矩陣運算 (Matrix Operations)
print(matA+matB)
print(matA-matB)
print(matA*matB)
print(matA**2)
#-----行列式，轉置，逆矩陣
print(det(matA))
print(transpose(matA))
print(matA.shape)
print(matA**(-1))















































	


