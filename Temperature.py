import csv
import numpy as np
def getdatasource(data_path):
    IceCream=[]
    ColdDrink=[]
    with open(data_path) as f:
        reader=csv.DictReader(f)
        for row in reader:
            IceCream.append(float(row["Ice-cream Sales"]))
            ColdDrink.append(float(row["Cold drink sales"]))
    return {"x":IceCream, "y":ColdDrink}

def findcorrelation(datasource):
    correlation=np.corrcoef(datasource["x"],datasource["y"])
    print("correlation coefficient: \n", correlation[0,1])

def setup():
    data_path='Temperature.csv'
    datasource=getdatasource(data_path)
    findcorrelation(datasource)

setup()