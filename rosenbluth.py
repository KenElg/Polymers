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
polsize = 100  #max polymer size
polpop = 10    # polymer population
    
def Addbead(beadpos,Weight,L,anglenum,U):
    startang=np.random.random()
    w = np.zeros((1,anglenum))
    compare=np.zeros((anglenum,2))
    for i in range (anglenum):
        theta = startang + i* 2 * pi/anglenum
        beadpos[L,:]=[beadpos[L-1,0]+cos(theta),beadpos[L-1,1]+sin(theta)]
        compare[i,:]= beadpos[L,:]
        E=ljcalc(beadpos,L+1,U,polsize)
        w[0,i]=exp(-E)
    W = np.sum(w)
    if W ==0:
        print  "Last Beadnumber =", L
    else:
        Track = np.cumsum(w/W)
        Test=np.random.random()
        for i in range (len(Track)):   
            if Test < Track[i]:      
                num = i   #check in which of the rows of track our test falls
                Test=Test+1 # Ensures we only have 1 found value
        beadpos[L]=compare[num,:]
#            print R[L,:]
#        end2end2[j,L] = np.sum(beadpos[L,:]**2) # end to end distance squared 
        Weight=Weight*W
        if L < polsize-1:          
            Addbead(beadpos,Weight,L+1,anglenum,0)                   
        return beadpos, Weight, L



#def Calcendtoend(beadpos):
#    end2end2=np.zeros((1,len(beadpos))) #end to end squared
#    for j in range(2,len(beadpos)):
#        end2end2[0,j] = np.sum(beadpos[j,:]**2) # end to end distance squared 
#    return end2end2
#
#
#R2[np.where(R2==0)] = np.nan 
##print R2
#R2mean = np.nanmean(R2,axis=0)
#R2var = np.nanvar(R2,axis=0,dtype=float)/(np.arange(polsize)**(0.5))
#
#plt.xscale("log", nonposx='clip')
#plt.yscale("log", nonposy='clip')
#plt.errorbar(np.arange(3,polsize+1),R2mean[2:], R2var[2:],linestyle = 'none',marker='x')
#
#plt.xlim([2,250])
#plt.xlabel("N")
#plt.ylabel("R^2")
##plt.plot(R[:,0],R[:,1])
#
#a = 1
#x = np.arange(polsize)
#fit = a*(x-1)**1.5
#plt.plot(x,fit)
#plt.show()

anglenum=6
beadpos = np.zeros ((polsize,2))
beadpos[1,:] = [1,0]
beadpos, Weight, L = Addbead(beadpos,1,L,anglenum,0)
plt.figure()
plt.plot(beadpos[:,0],beadpos[:,1])
plt.show