import csv
import numpy as np
def getdatasource(data_path):
    size=[]
    time=[]
    with open(data_path) as f:
        reader=csv.DictReader(f)
        for row in reader:
            size.append(float(row["Size of TV"]))
            time.append(float(row["\tAverage time spent watching TV in a week (hours)"]))
    return {"x":size, "y":time}

def findcorrelation(datasource):
    correlation=np.corrcoef(datasource["x"],datasource["y"])
    print("correlation coefficient: \n", correlation[0,1])

def setup():
    data_path='TV.csv'
    datasource=getdatasource(data_path)
    findcorrelation(datasource)

setup()