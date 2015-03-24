#Rosenbluth
import numpy as np
import math
from LJcalc import ljcalc
import matplotlib.pyplot as plt 
pi=math.pi
cos=math.cos
sin=math.sin
exp=math.exp
L = 2
T = 1
polsize = 25   #max polymer size
polpop = 10    # polymer population
R2 = np.zeros((polpop,polsize))
num=0
for j in range (polpop):
    R = np.zeros ((polsize,2))
    R[1,:] = [1,0]
    anglenum=6
    w = np.zeros((1,anglenum))
    compare=np.zeros((anglenum,2))
    def Addbead(R,Weight,L,anglenum,U):
        startang=np.random.random() 
        for i in range (anglenum):
            theta = startang + i* 2 * pi/anglenum
            R[L,:]=[R[L-1,0]+cos(theta),R[L-1,1]+sin(theta)]
            compare[i,:]= R[L,:]
            E=ljcalc(R,L+1,U,polsize)
            w[0,i]=exp(-E)
#            print E
        W = np.sum(w)
        if W ==0:
            print "Polymer number=", j, "Beadnumber =", L
        else:
            Track = np.cumsum(w/W)
            Test=np.random.random()
            for i in range (len(Track)):   
                if Test < Track[i]:      
                    num = i   #check in which of the rows of track our test falls
#                    Test=Test+1 # Ensures we only have 1 found value
                    # print num
            R[L]=compare[num,:]
#            print R[L,:]
            R2[j,L] = np.sum(R[L,:]**2) # end to end distance squared 
            Weight=Weight*W
            if L < polsize-1:
                
                Addbead(R,Weight,L+1,anglenum,0)
                       
        return R, Weight, L, R2
    R, Weight, L, R2 = Addbead(R,1,L,anglenum,0)
R2[np.where(R2==0)] = np.nan 
#print R2
R2mean = np.nanmean(R2,axis=0)
R2std = np.nanstd(R2,axis=0,dtype=float)

plt.xscale("log", nonposx='clip')
plt.yscale("log", nonposy='clip')
plt.errorbar(np.arange(3,polsize+1),R2mean[2:], R2std[2:],linestyle = 'none',marker='x')

plt.xlim([2,250])
plt.xlabel("N")
plt.ylabel("R^2")
#plt.plot(R[:,0],R[:,1])

a = 1
x = np.arange(polsize)
fit = a*(x-1)**1.5
plt.plot(x,fit)
plt.show()
