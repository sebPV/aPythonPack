# import matplotlib.pyplot as plt  # importerer matplotlib
import sympy as sp # importerer sympy
# from sympy import exp, I , pi, sqrt
# import numpy as np
from collections.abc import Iterable

def arrTabular(*Data,hline=False):
    res=''
    subArr = []
    subArrLen = []
    for n in Data:
        if isinstance(n[0], Iterable):
            for m in n:
                subArr.append(m)
                subArrLen.append(len(m))
        else:
            subArr.append(n)
            subArrLen.append(len(n))
    
    for n in range(max(subArrLen)):
        line = ''
        for m in subArr:
            if not n < len(m):
                line = line + '  & '
            elif isinstance(m[n],sp.Expr):
                line = line +'$ r $ & '.replace('r',sp.latex(m[n]))
            elif isinstance(m[n],(int, float)):
                line = line + '$ r $ & '.replace('r',str(m[n]))
            else:
                line = line + str(m[n]) + ' & '
        line = line[:-2] + ' \\\\ \n'
        if hline:
            line = line + ' \\hline \n'
        res = res + line
    return res

print(arrTabular([3,4,5,6],sp.Matrix([[1,2],[3,4]]),hline = True))
print(sp.Matrix([[1,2],[3,4]]))
