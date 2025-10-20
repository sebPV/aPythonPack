import matplotlib.pyplot as plt  # importerer matplotlib
import sympy as sp# importerer sympy
from sympy import exp, I , pi, sqrt
import numpy as np
from collections.abc import Iterable
sp.init_printing()  # gør at matematiske udtryk skrives pænt

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


def arrOp(func, values, args=[]):
    argNames = func.__code__.co_varnames
    res = []
    for n in values:
        parsel ={}       
        if not isinstance(values[0], Iterable):
            parsel[argNames[0]]=n
            for m in range(len(args)):
                parsel[argNames[m+1]] = args[m]
        else:
            for m in range(len(values)):
                parsel[argNames[m]] = n[m]
            for m in range(len(args)):
                parsel[argNames[m+len(n)]]=args[m]
        print(parsel)
        
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

