#Rosenbluth
import numpy as np
import math
from LJcalc import ljcalc
import matplotlib.pyplot as plt 
pi=math.pi
cos=math.cos
sin=math.sin
exp=math.exp
    
def Addbead(beadpos,Weight,L,anglenum,U,polsize):
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
            Addbead(beadpos,Weight,L+1,anglenum,0,polsize)                   
        return beadpos, Weight, L



def Calcendtoend2(beadpos):
    end2end2=np.zeros((1,len(beadpos))) #end to end squared
    for j in range(2,len(beadpos)):
        end2end2[0,j] = np.sum(beadpos[j,:]**2) # end to end distance squared 
    return end2end2
    
def RadofGyr(beadpos):
    RG2=np.zeros((1,len(beadpos))) #end to end squared    
    for j in range(2,len(beadpos)):
        R0=np.zeros((1,2))
        Calc=0
        R0[0,0]=(1.0/j)*np.sum(beadpos[0:j,0])
        R0[0,1]=(1.0/j)*np.sum(beadpos[0:j,1])
        for k in range(j):
            Calc=Calc+(beadpos[k,:]-R0)**2
#            print Calc
        RG2[0,j]=(1.0/j)*np.sum(Calc)
    return RG2