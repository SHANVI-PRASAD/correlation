import csv
import numpy as np
def getdatasource(data_path):
    Marks=[]
    Days=[]
    with open(data_path) as f:
        reader=csv.DictReader(f)
        for row in reader:
            Marks.append(float(row["Marks In Percentage"]))
            Days.append(float(row["Days Present"]))
    return {"x":Marks, "y":Days}

def findcorrelation(datasource):
    correlation=np.corrcoef(datasource["x"],datasource["y"])
    print("correlation coefficient: \n", correlation[0,1])

def setup():
    data_path='Marks.csv'
    datasource=getdatasource(data_path)
    findcorrelation(datasource)

setup()