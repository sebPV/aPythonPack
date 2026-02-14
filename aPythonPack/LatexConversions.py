# import matplotlib.pyplot as plt  # importerer matplotlib
import sympy as sp # importerer sympy
# from sympy import exp, I , pi, sqrt
# import numpy as np
from collections.abc import Iterable

import numpy as np
import pandas as pd
import pint_pandas

import pint
ureg = pint.get_application_registry()
Q_ = ureg.Quantity




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

class tikzPlot:
    
    def __init__(self,width =0.75, height = 0.5,xlabel = '$x$', ylabel='$y$'):
        self.width = width
        self.height = height
        self.xlabel = xlabel
        self.ylabel = ylabel
        self.colors =['blue','red','green','yellow']
        self.colCount = 0
        self.plots = []
        self.legends =[]
        self.lineTyp={'--': 'dashed,',
                      '-o': 'mark=*,',
                      '--o': 'dashed, mark=*,',
                      'o': 'mark=*, only marks,'}




    def addPlot(self,xx,yy,color='',line='',opt = '',legend = ''):
        if color == '':
            color = self.colors[self.colCount]
            self.colCount = (self.colCount+ 1)%len(self.colors)

        if line in self.lineTyp:
            line = self.lineTyp[line]
        else: line =''

        out = '\\addplot[' +color+','+ line + opt +']     \n table{% \n'
        for i in range(min(len(xx),len(yy))):
            out += str(xx[i]) + ' ' + str(yy[i]) + '\n'
        out += '}; \n'
        self.plots.append(out)
        if legend != '':
            self.legends.append(legend)


    def createString(self):
        out = """
\\begin{tikzpicture}
    \\begin{axis}[\n"""
        out += 'xlabel = {' + self.xlabel +'},\nylabel = {' + self.ylabel + '}, \nheight =' + str(self.height) + '\\linewidth, \nwidth = ' + str(self.width) +'\\linewidth, \n'
        out += 'legend style = {at={(0.05,0.95)},anchor = {north west}} \n ]'
        for i in self.plots:
            out += i
        if self.legends != []:
            leg = '\\legend{'
            for i in self.legends:
                leg += i + ','
            out += leg[:-1] + '}\n'
        out += """
    \\end{axis}
\\end{tikzpicture}"""
        return out


    def printPlot(self):
        print(self.createString())


    def writePLot(self,filename ='plot'):
        with open(filename+'.tex', 'w') as f:
            f.write(self.createString())






# def dfToTab(Data=pd.DataFrame):
#     tabular = ''
#     header = ''
#     for i in Data:
#         header += str(i[0])


#     return tabular





