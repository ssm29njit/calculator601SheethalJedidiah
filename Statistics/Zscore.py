#mport numpy as np
#from scipy import stats
from Statistics.randomNum import getRandomNum
from Statistics.Mean import mean
from Statistics.stdeviation import stdev

def zscore(data):
    meann = mean(data)
    stdv = stdev(data)
    outlier =[]
    threshold = meann
    for i in data:
        z = (i-mean)/stdv
        try:
            if z > threshold:
                outlier.append(z)
        except:
            print('No Outlier cannot be added')

