import matplotlib.pyplot as plt  # importerer matplotlib
import sympy as sp# importerer sympy
from sympy import exp, I , pi, sqrt
import numpy as np
sp.init_printing()  # gør at matematiske udtryk skrives pænt

def simpArr(arr):
    for n in range(len(arr)):
        arr[n] = sp.simplify(arr[n])
    return arr
def sympArr(arr):
    for n in range(len(arr)):
        arr[n] = sp.sympify(arr[n])
    return arr
def forceRekt(arr):
    for n in range(len(arr)):
        arr[n] = sp.re(arr[n])+i*sp.im(arr[n])
    return arr
def forcePol(arr):
    for n in range(len(arr)):
        arr[n] = sp.Abs(arr[n])*sp.exp(i*sp.arg(arr[n]))
    return arr