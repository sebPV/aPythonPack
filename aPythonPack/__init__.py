import matplotlib.pyplot as plt  # importerer matplotlib
import sympy as sp# importerer sympy
from sympy import exp, I , pi, sqrt, E, log, ln
from sympy import E as e
import numpy as np
from collections.abc import Iterable
sp.init_printing()  # gør at matematiske udtryk skrives pænt
# import LatexConversions
def simpArr(arr):
    res = []
    for n in arr:
        res.append(sp.simplify(n))
    return res
def sympArr(arr):
    res = []
    for n in arr:
        res.append(sp.sympify(n))
    return res


def arrOp(func, values, *args):
    argNames = func.__code__.co_varnames
    res = []
    for n in values:
        parsel ={}       
        if not isinstance(values[0], Iterable):
            parsel[argNames[0]]=n
            for m in range(len(args)):
                if isinstance(args[m], dict):
                    parsel.update(args[m])
                else:
                    parsel[argNames[m+1]] = args[m]
        else:
            for m in range(len(values)):
                parsel[argNames[m]] = n[m]
            for m in range(len(args)):
                if isinstance(args[m],dict):
                    parsel.update(args[m])
                else:
                    parsel[argNames[m+len(n)]]=args[m]
        
        res.append(func(**parsel))
    return res


def forceRekt(arr):
    if isinstance(arr, Iterable):
        res = []
        for n in range(len(arr)):
            res.append(sp.re(n)+I*sp.im(n))
        return res
    else:
        return sp.re(arr)+I*sp.im(arr)
def forcePol(arr):
    if isinstance(arr,Iterable):
        res = []
        for n in arr:
            res.append(sp.Abs(n)*sp.exp(I*sp.arg(n)))
        return res
    else:
        return sp.Abs(arr)*sp.exp(I*sp.arg(arr))

def divArr(arr):
    res =[]
    for n in arr:
        res.append(sp.div(n[0],n[1]))
    return res

def plotComplex(arr):
    plt.axvline(0, color="gray")  # akser
    plt.axhline(0, color="gray")  # akser
    Rea = []
    Ima = []
    for z in arr:
        Rea.append(sp.re(z))
        Ima.append(sp.im(z))
        plt.annotate(r'$s$'.replace('s',sp.latex(z)),(sp.re(z),sp.im(z)))
        
    plt.scatter(Rea, Ima)
    plt.xlabel(r"$Re(z)$")  # akse-etiketter
    plt.ylabel(r"$Im(z)$")  # akse-etiketter
    plt.grid(True)  # gitter


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
