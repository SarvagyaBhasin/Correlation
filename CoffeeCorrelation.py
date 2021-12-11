import plotly.express as px
import csv 
import numpy as np 

def plotfigure(datapath, X, Y):
    with open(datapath) as f:
        df=csv.DictReader(f)
        fig=px.scatter(df, x=X, y=Y)
        fig.show()
def findcorrelation(datapath, X, Y):
    datax=[]
    datay=[]
    with open(datapath) as f:
        df=csv.DictReader(f)
        for row in df:
            datax.append(float(row[X]))
            datay.append(float(row[Y]))
    correlation=np.corrcoef(datax, datay)
    print("Correlation: ", correlation[0, 1])
def main():
    datapath="coffee.csv"
    x="Coffee in ml"
    y="sleep in hours"
    plotfigure(datapath, x, y)
    findcorrelation(datapath, x, y)
main()    