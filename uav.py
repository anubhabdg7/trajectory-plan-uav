import numpy as np 
import matplotlib.pyplot as plt 

class model:

    def __init__(self):
        self.xs=10
        self.ys=10
        self.xt=55
        self.yt=100
        self.xobs=np.array([45,12,32,36,55])
        self.yobs=np.array([52,40,68,26,80])
        self.robs=np.array([10,10,8,12,9])
        self.xmin=0
        self.xmax=100
        self.ymin=0
        self.ymax=100
        
        
