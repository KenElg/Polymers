import numpy as np
import math
import matplotlib.pyplot as plt 
import rosenbluth
pi=math.pi
cos=math.cos
sin=math.sin
exp=math.exp
L = 2
T = 1
polsize = 150 #max polymer size
polpop = 10    # polymer population
anglenum=6
beadpos = np.zeros ((polsize,2))
beadpos[1,:] = [1,0]

endmat = np.zeros((polpop, polsize))
Radmat= np.zeros((polpop, polsize))
Weightvec = np.zeros((polpop,1))
for i in range(polpop):
    beadpos, Weightvec[i], L = rosenbluth.Addbead(beadpos,1,L,anglenum,0,polsize)  
    endmat[i,:]=rosenbluth.Calcendtoend2(beadpos)
    Radmat[i,:]=rosenbluth.RadofGyr(beadpos)

endmat_mean, endmat_var = rosenbluth.Stat(endmat,Weightvec,polpop,polsize)

#plt.figure()
#plt.plot(beadpos[:,0],beadpos[:,1])
#plt.show  

plt.xscale("log", nonposx='clip')
plt.yscale("log", nonposy='clip')
plt.errorbar(np.arange(3,polsize+1),endmat_mean[2:], endmat_var[2:],linestyle = 'none',marker='x')
##
#plt.xlim([2,polsize])
##plt.xlabel("N")
#plt.ylabel("R^2")
##plt.plot(R[:,0],R[:,1])
#
#a = 1
#x = np.arange(polsize)
#fit = a*(x-1)**1.5
#plt.plot(x,fit)
#plt.show()