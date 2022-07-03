import numpy as np 
import matplotlib.pyplot as plt 
from scipy import interpolate
from uav import model as model 

class cost:
    def __init__(self):
        self.m=model()
        self.beta=100
        self.tt=np.linspace(0,1,102)
        self.alpha=1
        self.ld=0.5
        
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
        # self.tt=np.linspace(xmin,xmax,100)
        xpts=interpolate.splrep(self.TS,self.XS)
        ypts=interpolate.splrep(self.TS,self.YS)
        # self.newXS=np.sort(self.XS)
        # self.newXS,self.newYS = zip(*sorted(zip(self.XS,self.YS)))

        # newpts=interpolate.splrep(self.newXS,self.newYS)
        self.xx=interpolate.splev(self.tt,xpts) 
        self.yy=interpolate.splev(self.tt,ypts)

        xx1=np.array([self.m.xs,self.xx[16],self.xx[33],self.xx[50],self.xx[67],self.xx[84],self.m.xt])
        yy1=np.array([self.m.ys,self.yy[16],self.yy[33],self.yy[50],self.yy[67],self.yy[84],self.m.yt])
        self.dx=np.diff(self.xx)
        self.dy=np.diff(self.yy)
        dx1=np.diff(self.xx[0:17])
        dx2=np.diff(self.xx[17:34])
        dx3=np.diff(self.xx[34:51])
        dx4=np.diff(self.xx[51:68])
        dx5=np.diff(self.xx[68:85])
        dx6=np.diff(self.xx[85:102])

        dy1=np.diff(self.yy[0:17])
        dy2=np.diff(self.yy[17:34])
        dy3=np.diff(self.yy[34:51])
        dy4=np.diff(self.yy[51:68])
        dy5=np.diff(self.yy[68:85])
        dy6=np.diff(self.yy[85:102])

        self.L=np.sum(np.sqrt(np.square(self.dx)+np.square(self.dy)))
        l1=np.sum(np.sqrt(np.square(dx1)+np.square(dy1)))
        l2=np.sum(np.sqrt(np.square(dx2)+np.square(dy2)))
        l3=np.sum(np.sqrt(np.square(dx3)+np.square(dy3)))
        l4=np.sum(np.sqrt(np.square(dx4)+np.square(dy4)))
        l5=np.sum(np.sqrt(np.square(dx5)+np.square(dy5)))
        l6=np.sum(np.sqrt(np.square(dx6)+np.square(dy6)))
        length=np.array([l1,l2,l3,l4,l5,l6])
        cost=(1-self.ld)*self.L 

        nobs=self.m.xobs.size 
        self.violation=0
        self.feasible=1
        
        for j in range(2,8,1):

            newx=np.linspace(xx1[j-2],xx1[j-1],7)
            newy=np.linspace(yy1[j-2],yy1[j-1],7)
            sum1=0
            flag=0

            for i in range(nobs):
                d1=np.square(np.square(newx[1]-self.m.xobs[i])+np.square(newy[1]-self.m.yobs[i]))
                d2=np.square(np.square(newx[2]-self.m.xobs[i])+np.square(newy[2]-self.m.yobs[i]))
                d3=np.square(np.square(newx[3]-self.m.xobs[i])+np.square(newy[3]-self.m.yobs[i]))
                d4=np.square(np.square(newx[4]-self.m.xobs[i])+np.square(newy[4]-self.m.yobs[i]))
                d5=np.square(np.square(newx[5]-self.m.xobs[i])+np.square(newy[5]-self.m.yobs[i]))

                temp=((1/d1)+(1/d2)+(1/d3)+(1/d4)+(1/d5))*self.m.tobs[i]
                sum1+=temp

                if d1<pow(self.m.robs[i],4):
                    flag+=1
                if d2<pow(self.m.robs[i],4):
                    flag+=1
                if d3<pow(self.m.robs[i],4):
                    flag+=1
                if d4<pow(self.m.robs[i],4):
                    flag+=1
                if d5<pow(self.m.robs[i],4):
                    flag+=1
            if flag>0:
                cost+=(self.ld)*(pow(length[j-2],2))*(sum1/5.00)


                # temp=1-(d/(self.m.robs[i]))

                # v=np.maximum(temp,np.zeros(1))
                # self.violation+=np.mean(v)
            
            # v=temp[np.argmax(temp)]
            # if v == 1:
            #     self.feasible=0
            #     self.violation+=1
        # if self.violation==0:
        #     self.feasible=1
        # else:
        #     self.feasible=0   
            
        
        # print(self.violation)
        
        # self.z=self.alpha*self.L+self.beta*self.violation*self.L
        # self.z=self.L*self.violation 
        # print(self.z)
        # self.z=np.random.randint(0,100)
        self.feasible=1
        self.z=cost 
        return self.z, self.feasible
        

            
                

