from aPythonPack.__init__ import *
# import aPythonPack.LatexConversions as LC
import io
test_data = """ShaftSpeedIndex,rpm,1200,1200,1200,1600,1600,1600,2300,2300,2300
pump,,A,B,C,A,B,C,A,B,C
TestDate,No Unit,01/01,01/01,01/01,01/01,01/01,01/01,01/02,01/02,01/02
ShaftSpeed,rpm,1200,1200,1200,1600,1600,1600,2300,2300,2300
FlowRate,m^3 h^-1,8.72,9.28,9.31,11.61,12.78,13.51,18.32,17.90,19.23
DifferentialPressure,kPa,162.03,144.16,136.47,286.86,241.41,204.21,533.17,526.74,440.76
ShaftPower,kW,1.32,1.23,1.18,3.09,2.78,2.50,8.59,8.51,7.61
Efficiency,dimensionless,30.60,31.16,30.70,30.72,31.83,31.81,32.52,31.67,32.05"""


df = pd.read_csv(io.StringIO(test_data), header=[0, 1], index_col=[0, 1]).T
df = df.pint.quantify(level=-1)
print(df.dtypes)


df["FlowRate"] = df["FlowRate"].pint.to("L/s")

def dfToTab(Data=pd.DataFrame):
    tabular = ''
    header = ''
    for i in Data:
        header += ' ' + str(i[0])
        print(i)
        if i[1] != 'No Unit':
            header += ' [' + i[1] +']'
        header += ' &'
    tabular += header[:-1] + '\\\ \n'

    return tabular



# print(dfToTab(df.de))

# print()