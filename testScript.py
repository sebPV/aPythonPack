# from aPythonPack.__init__ import *
# # import aPythonPack.LatexConversions as LC

# df = pd.DataFrame(
#     {
#         'ShaftSpeedIndex':pd.Series([1200,1200,1200,1600,1600,1600,2300,2300,2300],dtype='pint[rpm]'),
#         'FlowRate':pd.Series([8.72,9.28,9.31,11.61,12.78,13.51,18.32,17.90,19.23],dtype='pint[m^3/h]'),
#         'FlowRateNU':pd.Series([8.72,9.28,9.31,11.61,12.78,13.51,18.32,17.90,19.23])
#     },
#     # index = [1200,1200,1200,1600,1600,1600,2300,2300,2300]
# )

# df.ShaftSpeedIndex = df.ShaftSpeedIndex.pint.to('Hz')
# print(df)

# def dfToTab(Data=pd.DataFrame):
#     outData = pd.DataFrame()
#     for i in Data:
#         if str(type(df[i].dtypes)) == '<class \'pint_pandas.pint_array.PintType\'>':
#             outData[i+ ' [ {:~L}'.format(df[i].pint.units) +']'] = df[i].values.quantity.magnitude
#         else:
#             outData[i] = df[i]
#     return outData.to_latex()

# print(dfToTab(df))


from aPythonPack.LatexConversions import *

tt=np.linspace(0,4,10)


plot = tikzPlot()
plot.addPlot([1,2,3,4],[5,6,7,8],legend='pis')
plot.addPlot(tt,tt**2,legend='lort',opt='line',line='--o')
plot.printPlot()
plot.writePLot()

