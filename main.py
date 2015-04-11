import numpy as np
import math
import matplotlib.pyplot as plt 
import rosenbluth
pi=math.pi
cos=math.cos
sin=math.sin
exp=math.exp

T = 1
polsize = 150 #max polymer size
polpop = 100    # polymer population
anglenum=9
Prunevec=np.zeros((polsize,1))
num=np.zeros ((polsize,1))
beadposlist=[]
Weightvec = np.zeros((polpop,1))
for i in range(polpop):
    L = 2
    beadpos = np.zeros ((polsize,2))
    beadpos[1,:] = [1,0]
    num, beadposlist = rosenbluth.Addbead(beadpos,1,L,anglenum,0,polsize,Prunevec, num, beadposlist)  

endmat = np.zeros((len(beadposlist), polsize))
Radmat= np.zeros((len(beadposlist), polsize))
for i in range(len(beadposlist)):  
    endmat[i,0:len(beadposlist[i])]=rosenbluth.Calcendtoend2(beadposlist[i])
    Radmat[i,0:len(beadposlist[i])]=rosenbluth.RadofGyr(beadposlist[i])

#
#endmat_mean, endmat_var = rosenbluth.Stat(endmat,Weightvec,polpop,polsize)
#
#x = np.arange(polsize)
#slope, intercept = rosenbluth.Fit(x,endmat_mean)
#print intercept
#plt.plot(x,np.power(10,intercept) * np.power(X,slope),'r')
#plt.figure()
#plt.plot(beadpos[:,0],beadpos[:,1])
#plt.show  

#plt.xscale("log", nonposx='clip')
#plt.yscale("log", nonposy='clip')
#plt.errorbar(np.arange(3,polsize+1),endmat_mean[2:], endmat_var[2:],linestyle = 'none',marker='x')
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