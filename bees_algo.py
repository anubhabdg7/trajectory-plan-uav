import numpy as np 
import matplotlib.pyplot as plt 
from uav import model as model 
from cost import cost as cost 
import math as math 


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
        self.P=1
        self.max_it=50
        self.optcost=np.zeros(self.max_it)
        self.counter_sup=np.zeros(self.max_it)
    
    def init(self):

        ### Intitialization and site selection ###

        self.recruitment=np.round(np.linspace(self.nep,1,self.n))
        self.assignment=np.linspace(0,1,self.n)
        self.colony_size=np.sum(self.recruitment)
         

        self.empty_patch={'position':{'x':np.zeros(self.nodes),'y':np.zeros(self.nodes)},
                          'cost':float(0.00),
                          #'sol': 0,
                          'size': np.zeros(2),
                          'stagnated': 0,
                          'counter': 0}
        self.counter=0
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
            
            self.patch[i]['cost'],~=self.cost.get_cost(self.patch[i]['position'])
            self.patch[i]['size']=np.array([((self.m.xmax-self.m.xmin)/4.00),((self.m.ymax-self.m.ymin)/4.00)])
            self.patch[i]['stagnated']=0.00
            counter+=1
            self.patch[i]['counter']=counter
        self.size=np.linspace(0,1,self.n)
        self.patch=self.site_selection(self.patch)

    def site_selection(self,patch):

        patch=sorted(patch, key=lambda d: d['cost'])
        return patch 
        


    def search(self):
        for it in range(self.max_it):

            if self.counter>=self.max_eval:
                break
            self.bestnewbee={'position':{'x':np.zeros(self.nodes),'y':np.zeros(self.nodes)},
                            'cost':float(0.00),
                            #'sol': 0,
                            'size': np.zeros(2),
                            'stagnated': 0,
                            'counter': 0}
            self.foragerbees={'position':{'x':np.zeros(self.nodes),'y':np.zeros(self.nodes)},
                            'cost':float(0.00),
                            #'sol': 0,
                            'size': np.zeros(2),
                            'stagnated': 0,
                            'counter': 0}
            
            for i in range(self.n):
                self.bestnewbee['cost']=np.inf
                self.assignment=self.d_tri_real_array(0,(i+1),1,1,self.recruitment[i])

                for j in range(self.recruitment[i]):
                    if self.P==1:
                        self.foragerbees['position']['x']=self.integrated_foraging_stlim_all(self.patch[i]['position']['x'],self.assignment[j],self.m.xmax,self.m.xmin,self.patch[i]['size'][0])
                        self.foragerbees['position']['y']=self.integrated_foraging_stlim_all(self.patch[i]['position']['y'],self.assignment[j],self.m.ymax,self.m.ymin,self.patch[i]['size'][1])                    
                    else:
                        self.foragerbees['position']['x']=self.integrated_foraging_stlim(self.patch[i]['position']['x'],self.assignment[j],self.m.xmax,self.m.xmin,self.patch[i]['size'][0])
                        self.foragerbees['position']['y']=self.integrated_foraging_stlim(self.patch[i]['position']['y'],self.assignment[j],self.m.ymax,self.m.ymin,self.patch[i]['size'][1])

                    self.foragerbees['cost'],~=self.cost.get_cost(self.foragerbees['position']) 
                    self.foragerbees['size']=self.patch[i]['size']
                    self.foragerbees['stagnated']=self.patch[i]['stagnated']
                    self.counter+=1
                    self.foragerbees['counter']=self.counter
                    if self.foragerbees['cost']<self.bestnewbee['cost']:
                        self.bestnewbee=self.foragerbees
                    
                if self.bestnewbee['cost']<self.patch[i]['cost']:
                    self.patch[i]=self.bestnewbee
                    self.patch[i]['stagnated']=0
                else:
                    self.patch[i]['stagnated']+=1
                    self.patch[i]['size']=self.patch[i]['size']*self.shrink

                if self.patch[i]['stagnated']>self.stlim:
                    self.patch[i]['size']=np.array([((self.m.xmax-self.m.xmin)/4.00),((self.m.ymax-self.m.ymin)/4.00)])
                    self.patch[i]['stagnated']=0
                    self.P*=-1

            self.patch=self.site_selection(self.patch)
            self.optsol=self.patch[0]
            self.optcost[it]=self.optsol['cost']
            opt_cost=np.zeros(self.max_it+1)
            opt_cost[0]=np.inf 
            opt_cost[it+1]=self.optcost[it]
            self.counter_sup[it]=self.counter
        return self.optsol 
            
            
            




        
        

    def d_tri_real_array(self,k,t,b,baris,kolom):
        M=np.zeros(baris,kolom)
        for i in range(baris):
            for j in range(kolom):
                M[i][j]=self.d_tri_real(k,t,b)
        return M 

    def d_tri_real(self,k,t,b):
        m=np.random.randint(1,10)
        a=(t-k)/10
        b=(b-t)/10

        if m==1:
            angka=np.random.uniform((t-a),(t+b),1)
        elif m==2:
            angka=np.random.uniform((t-2*a),(t+2*b),1)
        elif m==3:
            angka=np.random.uniform((t-3*a),(t+3*b),1)
        elif m==4:
            angka=np.random.uniform((t-4*a),(t+4*b),1)
        elif m==5:
            angka=np.random.uniform((t-5*a),(t+5*b),1)
        elif m==6:
            angka=np.random.uniform((t-6*a),(t+6*b),1)
        elif m==7:
            angka=np.random.uniform((t-7*a),(t+7*b),1)
        elif m==8:
            angka=np.random.uniform((t-8*a),(t+8*b),1)
        elif m==9:
            angka=np.random.uniform((t-9*a),(t+9*b),1)
        elif m==10:
            angka=np.random.uniform((t-10*a),(t+10*b),1)
        
        return angka 


    def integrated_foraging_stlim_all(self,x,ass,vmx,vmn,size):
        r=ass*size 
        nvar=x.size 
        pert=np.random.randint(0,1,(1,nvar))
        y=x
        y+=np.random.uniform(-r,r,1)*pert 
        if y>vmx:
            y=vmx 
        if y<vmn:
            y=vmn 
    
    def integrated_foraging_stlim(self,x,ass,vmx,vmn,size):
        r=ass*size 
        nvar=x.size 
        k=np.random.randint(1,nvar)
        y=x 
        y[k]+=r*(math.pow(-1,np.random.randint(1,2)))
        if y>vmx:
            y=vmx 
        if y<vmn:
            y=vmn 
    




        

