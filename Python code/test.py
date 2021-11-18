import numpy as np
import pickle

cpath = '/opt/shared/PyCharmProjects/CrimePrediction-master/Python code/'
file = cpath + 'matrices311'
with open(file, 'rb') as toOpen:
    data = pickle.load(toOpen)
    print(data)