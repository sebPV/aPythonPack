from aPythonPack.__init__ import *
# import aPythonPack.LatexConversions as LC

df = pd.DataFrame(
    {
        'ShaftSpeedIndex':pd.Series([1200,1200,1200,1600,1600,1600,2300,2300,2300],dtype='pint[rpm]'),
        'FlowRate':pd.Series([8.72,9.28,9.31,11.61,12.78,13.51,18.32,17.90,19.23],dtype='pint[m^3/h]'),
        'FlowRateNU':pd.Series([8.72,9.28,9.31,11.61,12.78,13.51,18.32,17.90,19.23])
    }
)

df.ShaftSpeedIndex = df.ShaftSpeedIndex.pint.to('Hz')


def dfToTab(Data=pd.DataFrame):
    tabular = ''
    header = ''
    for i in Data:
        header += ' ' + str(i)
        if str(type(df[i].dtypes)) == '<class \'pint_pandas.pint_array.PintType\'>':
            header += ' [ {:~L}'.format(df[i].pint.units) +']'
        header += ' &'
    tabular += header[:-1] + '\\\ \n \\hline \n'

    return tabular

# for i in df:
#     print(str(type(df[i].dtypes)))



# print()