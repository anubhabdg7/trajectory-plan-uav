import numpy as np 
import matplotlib.pyplot as plt 
# import math as m 
from bees_algo import bees_algo as ba 
from uav import model as m 
from scipy import interpolate
# import streamlit as st 
from test_new import test as test 
m=m()
ba=ba()
t=test()
solution=t.run()
# ba.init()
# # print(np.random.uniform(-1,1,1))
# sol,cost,best=ba.search()
# print(sol['position']['x'])
fig,axes=plt.subplots()
axes.set_xlim([0,100])
axes.set_ylim([0,100])


c1=plt.Circle((m.xobs[0],m.yobs[0]),m.robs[0])
c2=plt.Circle((m.xobs[1],m.yobs[1]),m.robs[1])
c3=plt.Circle((m.xobs[2],m.yobs[2]),m.robs[2])
c4=plt.Circle((m.xobs[3],m.yobs[3]),m.robs[3])
c5=plt.Circle((m.xobs[4],m.yobs[4]),m.robs[4])
axes.set_aspect('equal')
axes.add_patch(c1)
axes.add_patch(c2)
axes.add_patch(c3)
axes.add_patch(c4)
axes.add_patch(c5)
axes.plot(m.xs,m.ys,'go')
axes.plot(m.xt,m.yt,'bo')


x=np.asarray(solution[0][0:10]) 
y=np.asarray(solution[0][10:20])
tt=np.linspace(0,1,1000)
k=x.size + 2
TS=np.linspace(0,1,k)
XS=np.insert(x,0,m.xs)
XS=np.append(XS,m.xt)
# self.YS=np.insert(self.y,[0,self.y.size],[self.m.ys,self.m.yt])
YS=np.insert(y,0,m.ys)
YS=np.append(YS,m.yt)

# xmax=self.XS[np.argmax(self.XS)]
# xmin=self.XS[np.argmin(self.XS)]
# self.tt=np.linspace(xmin,xmax,100)
xpts=interpolate.splrep(TS,XS)
ypts=interpolate.splrep(TS,YS)
# self.newXS=np.sort(self.XS)
# self.newXS,self.newYS = zip(*sorted(zip(self.XS,self.YS)))

# newpts=interpolate.splrep(self.newXS,self.newYS)
xx=interpolate.splev(tt,xpts) 
yy=interpolate.splev(tt,ypts)




# f = interp1d(sol['position']['x'], sol['position']['y'], kind='cubic')
# y_smooth=f(sol['position']['x'])
# plt.plot(sol['position']['x'],y_smooth)

# for i in range(10):
#     axes.plot(sol['position']['x'][i],sol['position']['y'][i],'ro')

# axes.plot(sol['position']['x'],sol['position']['y'])

axes.plot(xx,yy,color='orange')

# print("Best=",best)

plt.show()

# plt.plot(cost)
# plt.show()
# st.legacy_caching.clear_cache()



