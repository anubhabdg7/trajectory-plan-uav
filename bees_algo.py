import numpy as np 
import matplotlib.pyplot as plt 
from uav import model as model 
from cost import cost as cost 

class bees_algo:
    def __init__(self):
        self.nodes=10
        self.m=model()
        self.cost=cost()
        self.max_eval=500000
        self.n=7
        self.nep=10
        self.shrink=0.8
        self.stlim=5
        self.accuracy=0.001

        ### Intitialization and site selection ###

        self.recruitment=np.round(np.linspace(self.nep,1,self.n))
        self.assignment=np.linspace(0,1,self.n)
        self.colony_size=np.sum(self.recruitment)
        self.max_it=50 

        self.empty_patch={'position':{'x':np.zeros(self.nodes),'y':np.zeros(self.nodes)},
                          'cost':float(0.00),
                          'sol': 0,
                          'size': 0,
                          'stagnated': 0,
                          'counter': 0}
        counter=0
        self.patch=[self.empty_patch for i in range(self.n)]

        for i in range(self.n):
            if i>0:
                self.patch[i]['position']['x']=np.random.uniform(self.m.xmin,self.m.xmax,self.nodes)
                self.patch[i]['position']['y']=np.random.uniform(self.m.ymin,self.m.ymax,self.nodes)
            else :
                xx=np.linspace(self.m.xs,self.m.xt,self.nodes)
                yy=np.linspace(self.m.ys,self.m.yt,self.nodes)
                self.patch[i]['position']['x']=xx[1:self.nodes-1]
                self.patch[i]['position']['y']=yy[1:self.nodes-1]
            
            self.patch[i]['cost']=self.cost.get_cost(self.patch[i]['position'])
            self.patch[i]['size']=


        

