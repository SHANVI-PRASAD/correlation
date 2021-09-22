import csv
import numpy as np
import plotly.express as px
def plotfigure(data_path):
    with open(data_path) as f:
        df=csv.DictReader(f)
        graph=px.scatter(df,x="Coffee in ml", y="sleep in hours")
        graph.show()
def getdatasource(data_path):
    Coffee=[]
    Hours=[]
    with open(data_path) as f:
        reader=csv.DictReader(f)
        for row in reader:
            Coffee.append(float(row["Coffee in ml"]))
            Hours.append(float(row["sleep in hours"]))
    return {"x":Coffee, "y":Hours}

def findcorrelation(datasource):
    correlation=np.corrcoef(datasource["x"],datasource["y"])
    print("correlation coefficient: \n", correlation[0,1])

def setup():
    data_path='Coffee.csv'
    datasource=getdatasource(data_path)
    findcorrelation(datasource)
    plotfigure(data_path)
setup()