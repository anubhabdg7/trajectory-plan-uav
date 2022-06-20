import numpy as np 
import matplotlib.pyplot as plt 
from uav import model as model 
from cost import cost as cost 
import math as math 
import streamlit as st 



class bees_algo:
    def __init__(self):
        self.nodes=10
        self.m=model()
        self.cost=cost()
        self.max_eval=500000
        self.n=10
        self.nep=10
        self.shrink=0.8
        self.stlim=5
        self.accuracy=0.001
        self.P=1
        self.max_it=1000
        self.optcost=np.zeros(self.max_it)
        self.counter_sup=np.zeros(self.max_it)
        # np.random.seed(200000)
    
    def init(self):

        ### Intitialization and site selection ###

        self.recruitment=np.round(np.linspace(self.nep,1,self.n))
        # self.recruitment=np.round(np.linspace(1,self.nep,self.n))
        # print(self.recruitment)

        self.assignment=np.linspace(0,1,self.n)
        self.colony_size=np.sum(self.recruitment)
         

        self.empty_patch={'position':{'x':np.zeros(self.nodes),'y':np.zeros(self.nodes)},
                          'cost':np.inf,
                          #'sol': 0,
                          'size': np.zeros(2),
                          'stagnated': 0,
                          'counter': 0}
        self.counter=0
        # counter=0
        self.patch=[self.empty_patch.copy() for i in range(self.n)]

        for i in range(self.n):
            if i>0:
                self.patch[i]['position']['x']=np.random.uniform(self.m.xmin,self.m.xmax,self.nodes)
                self.patch[i]['position']['y']=np.random.uniform(self.m.ymin,self.m.ymax,self.nodes)
            else :
                xx=np.linspace(self.m.xs,self.m.xt,self.nodes)
                yy=np.linspace(self.m.ys,self.m.yt,self.nodes)
                self.patch[i]['position']['x']=xx[1:self.nodes-1]
                self.patch[i]['position']['y']=yy[1:self.nodes-1]
            # print(i)
            self.patch[i]['cost'],f = self.cost.get_cost(self.patch[i]['position'])
            # print(self.patch[i]['cost'])
            # new=i-1
            # print(self.patch[new]['cost'])
            self.patch[i]['size']=np.array([((self.m.xmax-self.m.xmin)/4.00),((self.m.ymax-self.m.ymin)/4.00)])
            self.patch[i]['stagnated']=0.00
            self.counter+=1
            self.patch[i]['counter']=self.counter
            
            # print(self.patch[i]['cost'])
        # self.size=np.linspace(0,1,self.n)
        # for i in range(self.n):
        #     print(self.patch[i]['cost'])
        self.patch=self.site_selection(self.patch)
        # for i in range(self.n):
        #     print(self.patch[i]['cost'])

    def site_selection(self,patch):

        patch=sorted(patch, key=lambda d: d['cost'])
        return patch 
        


    def search(self):
        best=np.inf 
        it=0
        opt_cost=np.zeros(self.max_it)
        self.bestnewbee={'position':{'x':np.zeros(self.nodes),'y':np.zeros(self.nodes)},
                            'cost':np.inf,
                            #'sol': 0,
                            'size': np.zeros(2),
                            'stagnated': 0,
                            'counter': 0}
        self.foragerbees={'position':{'x':np.zeros(self.nodes),'y':np.zeros(self.nodes)},
                            'cost':np.inf,
                            #'sol': 0,
                            'size': np.zeros(2),
                            'stagnated': 0,
                            'counter': 0}
        while(it<self.max_it):
            # np.random.seed(it)

            # if self.counter>=self.max_eval:
            #     break
            
            
            for i in range(self.n):
                # self.bestnewbee['cost']=self.patch[i]['cost']
                self.bestnewbee['cost']=np.inf 
                # self.bestnewbee={'position':{'x':np.zeros(self.nodes),'y':np.zeros(self.nodes)},
                #             'cost':np.inf,
                #             #'sol': 0,
                #             'size': np.zeros(2),
                #             'stagnated': 0,
                #             'counter': 0}
                # self.foragerbees={'position':{'x':np.zeros(self.nodes),'y':np.zeros(self.nodes)},
                #             'cost':np.inf,
                #             #'sol': 0,
                #             'size': np.zeros(2),
                #             'stagnated': 0,
                #             'counter': 0}
                self.assignment=self.d_tri_real_array(0,1,1,1,self.recruitment[i])[0]
                # arr=np.linspace(0,1,self.n)
                
                # self.assignment=np.zeros(int(self.recruitment[i]))
                # for mm in range(int(self.recruitment[i])):
                #     numb=np.random.randint(0,self.n)
                #     self.assignment[mm]=arr[numb]

                # print(self.assignment)

                for j in range(int(self.recruitment[i])):
                    if self.P==1:
                        self.foragerbees['position']['x']=self.integrated_foraging_stlim_all(self.patch[i]['position']['x'],self.assignment[j],self.m.xmax,self.m.xmin,self.patch[i]['size'][0])
                        self.foragerbees['position']['y']=self.integrated_foraging_stlim_all(self.patch[i]['position']['y'],self.assignment[j],self.m.ymax,self.m.ymin,self.patch[i]['size'][1])                    
                    else:
                        self.foragerbees['position']['x']=self.integrated_foraging_stlim(self.patch[i]['position']['x'],self.assignment[j],self.m.xmax,self.m.xmin,self.patch[i]['size'][0])
                        self.foragerbees['position']['y']=self.integrated_foraging_stlim(self.patch[i]['position']['y'],self.assignment[j],self.m.ymax,self.m.ymin,self.patch[i]['size'][1])
                    # print(self.foragerbees['position']['x'])
                    self.foragerbees['cost'],f = self.cost.get_cost(self.foragerbees['position']) 
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
                    al=self.n-1
                    self.patch[i]=self.patch[al]
                    # self.patch[i]['position']['x']=np.random.uniform(self.m.xmin,self.m.xmax,self.nodes)
                    # self.patch[i]['position']['y']=np.random.uniform(self.m.ymin,self.m.ymax,self.nodes)
                    self.patch[i]['size']=np.array([((self.m.xmax-self.m.xmin)/4.00),((self.m.ymax-self.m.ymin)/4.00)])
                    self.patch[i]['stagnated']=0
                    self.P*=-1
                    # self.n=self.n-1

            self.patch=self.site_selection(self.patch)
            # if it==0:

            #     self.optsol=self.patch[0]
            # else:
                
            tmp=self.patch[0]['cost']
            if tmp<best:
                best=tmp 
                self.optsol=self.patch[0]
            opt_cost[it]=best 
            # opt_cost=np.zeros(self.max_it+1)
            # opt_cost[0]=np.inf 
            # opt_cost[it+1]=self.optcost[it]
            # self.counter_sup[it]=self.counter
            print(best)
            print("Iteration=",it+1)
            # f1=open("savex.txt","a")
            # f1.write(str(self.optsol['position']['x'])+'\n')
            # f1.close()
            # f2=open("savey.txt","a")
            # f2.write(str(self.optsol['position']['y'])+'\n')
            # f2.close()
            # f3=open("savec.txt","a")
            # f3.write(str(best)+'\n')
            # f3.close()
            it+=1
        st.legacy_caching.clear_cache()
        return self.optsol,opt_cost,best
            
            
            




        
        

    def d_tri_real_array(self,k,t,b,baris,kolom):
        M=np.zeros((int(baris),int(kolom)))
        for i in range(int(baris)):
            for j in range(int(kolom)):
                # print(self.d_tri_real(k,t,b)[0])
                M[i][j]=(self.d_tri_real(k,t,b)[0])
        return M 

    def d_tri_real(self,k,t,b):
        m=np.random.randint(1,11)
        a=(t-k)/10.00 
        b1=(b-t)/10.00

        if m==1:
            angka=np.random.uniform((t-a),(t+b1),1)
        elif m==2:
            angka=np.random.uniform((t-2*a),(t+2*b1),1)
        elif m==3:
            angka=np.random.uniform((t-3*a),(t+3*b1),1)
        elif m==4:
            angka=np.random.uniform((t-4*a),(t+4*b1),1)
        elif m==5:
            angka=np.random.uniform((t-5*a),(t+5*b1),1)
        elif m==6:
            angka=np.random.uniform((t-6*a),(t+6*b1),1)
        elif m==7:
            angka=np.random.uniform((t-7*a),(t+7*b1),1)
        elif m==8:
            angka=np.random.uniform((t-8*a),(t+8*b1),1)
        elif m==9:
            angka=np.random.uniform((t-9*a),(t+9*b1),1)
        elif m==10:
            angka=np.random.uniform((t-10*a),(t+10*b1),1)
        
        return angka 


    def integrated_foraging_stlim_all(self,x,ass,vmx,vmn,size):
        
        r=ass*size
        # print(r)
        nvar=x.size 
        pert=np.random.randint(0,2,(1,nvar))
        # print(pert)
        y=x
        # print("Hello")
        # print((np.random.uniform(-1*r,r,1)[0]))
        y=y+(np.random.uniform(-1*r,r,1)[0])*pert 
        y=y[0]
        for i in range(y.size):
            if y[i]>vmx:
                y[i]=vmx 
            if y[i]<vmn:
                y[i]=vmn 
        return y 
    
    def integrated_foraging_stlim(self,x,ass,vmx,vmn,size):
        r=ass*size
        nvar=x.size 
        k=np.random.randint(0,nvar)
        y=x 
        
        y[k]=y[k]+r*(math.pow(-1,np.random.randint(1,3)))

        # if y[k]>vmx:
        #     y[k]=vmx 
        # if y[k]<vmn:
        #     y[k]=vmn 
        
        for i in range(y.size):
            if y[i]>vmx:
                y[i]=vmx 
            if y[i]<vmn:
                y[i]=vmn
        
        return y 
    




        

