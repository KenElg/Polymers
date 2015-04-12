import numpy as np
import math
import rosenbluth
pi=math.pi
cos=math.cos
sin=math.sin
exp=math.exp

T = 1
polsize = 150 #max polymer size
polpop = 1000    # polymer population
anglenum=9
Prunevec=np.zeros((polsize,1))
num=np.zeros ((polsize,1))
beadposlist=[]
weightlist = []
for i in range(polpop):
    L = 2
    beadpos = np.zeros ((polsize,2))
    WeightVec=np.zeros ((polsize,1))
    beadpos[1,:] = [1,0]
    num, beadposlist,weightlist = rosenbluth.Addbead(beadpos,1,L,anglenum,0,polsize,Prunevec, num, beadposlist,WeightVec,weightlist)  


endmat = np.zeros((len(beadposlist), polsize))
Radmat= np.zeros((len(beadposlist), polsize))
for i in range(len(beadposlist)):  
    endmat[i,0:len(beadposlist[i])]=rosenbluth.Calcendtoend2(beadposlist[i])
    Radmat[i,0:len(beadposlist[i])]=rosenbluth.RadofGyr(beadposlist[i])

# Plotting population size
#plt.figure()
#plt.plot(np.arange(150),num)
#plt.show()

#
endmat_mean, endmat_var = rosenbluth.Stat(endmat,polpop,polsize)
rosenbluth.Fit(polsize,endmat_mean,endmat_var,"R2","End-to-end distance")