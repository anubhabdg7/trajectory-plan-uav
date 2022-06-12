import numpy as np 
import matplotlib.pyplot as plt 
from scipy import interpolate
from uav import model as model 

class cost:
    def __init__(self):
        self.m=model()
        self.beta=100
        # self.tt=np.linspace(0,1,100)
        
    def get_cost(self,sol1):
        self.x=sol1['x'] 
        self.y=sol1['y'] 
        self.k=self.x.size + 2
        self.TS=np.linspace(0,1,self.k)
        self.XS=np.insert(self.x,0,self.m.xs)
        self.XS=np.append(self.XS,self.m.xt)
        # self.YS=np.insert(self.y,[0,self.y.size],[self.m.ys,self.m.yt])
        self.YS=np.insert(self.y,0,self.m.ys)
        self.YS=np.append(self.YS,self.m.yt)

        xmax=self.XS[np.argmax(self.XS)]
        xmin=self.XS[np.argmin(self.XS)]
        self.tt=np.linspace(xmin,xmax,100)
        # xpts=interpolate.splrep(self.TS,self.XS)
        # ypts=interpolate.splrep(self.TS,self.YS)
        # self.newXS=np.sort(self.XS)
        self.newXS,self.newYS = zip(*sorted(zip(self.XS,self.YS)))

        newpts=interpolate.splrep(self.newXS,self.newYS)
        self.xx=self.tt 
        self.yy=interpolate.splev(self.tt,newpts)

        self.dx=np.diff(self.xx)
        self.dy=np.diff(self.yy)
        self.L=np.sum(np.sqrt(np.square(self.dx)+np.square(self.dy)))

        nobs=self.m.xobs.size 
        self.violation=0
        self.feasible=1
        for i in range(nobs):
            d=np.sqrt(np.square(self.xx-self.m.xobs[i])+np.square(self.yy-self.m.yobs[i]))
            temp=1-(d/(self.m.robs[i]))

            v=np.maximum(temp,np.zeros(1))
            self.violation+=np.mean(v)
            
            # v=temp[np.argmax(temp)]
            # if v == 1:
            #     self.feasible=0
            #     self.violation+=1
        if self.violation==0:
            self.feasible=1
        else:
            self.feasible=0   
            
        
        
        
        self.z=self.L*(1+self.beta*self.violation)
        return self.z, self.feasible
        

            
                

