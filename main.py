import numpy as np 
import matplotlib.pyplot as plt 
import math as m 
from bees_algo import bees_algo as ba 
from uav import model as m 

m=m()
ba=ba()

ba.init()
# print(np.random.uniform(-1,1,1))
sol=ba.search()
print(sol['position']['x'])
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
for i in range(10):
    axes.plot(sol['position']['x'][i],sol['position']['y'][i],'ro')

plt.show()



