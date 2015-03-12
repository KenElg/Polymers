#Rosenbluth
import numpy as np
import math
from LJcalc import ljcalc
l = 1
T = 1
eps = 0.25 
sig = 0.8
N=10
R = np.zeros ((N,2))
R[1,:] = [1,0]
pi=math.pi
cos=math.cos
sin=math.sin
exp=math.exp
anglenum=6
w = np.zeros((1,anglenum))
compare=np.zeros((anglenum,2))
U=0
def Addbead(R,Weight,L,anglenum,U):
    startang=np.random.random() 
    for i in range (anglenum):
        theta = startang + i* 2 * pi/anglenum
        R[L+1]=[R[L,0]+cos(theta),R[L,1]+sin(theta)]
        compare[i,:]=R[L+1]
        E=ljcalc(R,L+1,U,N)
        w[i]=exp(-E)
    W = np.sum(w)
    Track = np.cumsum(w/W)
    Test=np.random.random()
    for i in range (len(Track)):   
        if Test < Track[i]:      
            num= i   #check in which of the rows of track our test falls
    R[L+1]=compare[num,:]
    Weight=Weight*W
    if L < N:
        Addbead(R,Weight,L+1,anglenum,0)
    return R, Weight
A = np.zeros((N,2))    
A,W = Addbead(R,1,1,anglenum,0)
