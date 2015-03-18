#Rosenbluth
import numpy as np
import math
from LJcalc import ljcalc
pi=math.pi
cos=math.cos
sin=math.sin
exp=math.exp
L = 2
T = 1
eps = 0.25 
sig = 0.8
N=10
R = np.zeros ((N,2))
R[1,:] = [1,0]
anglenum=6
w = np.zeros((1,anglenum))
compare=np.zeros((anglenum,2))
U=0
def Addbead(R,Weight,L,anglenum,U):
    startang=np.random.random() 
    for i in range (anglenum):
        theta = startang + i* 2 * pi/anglenum
        R[L,:]=[R[L-1,0]+cos(theta),R[L-1,1]+sin(theta)]
        compare[i,:]= R[L-1,:]
        E=ljcalc(R,L+1,U,N)
        w[0,i]=exp(-E)
    W = np.sum(w)
    Track = np.cumsum(w/W)
    Test=np.random.random()
    for i in range (len(Track)):   
        if Test < Track[i]:      
            num= i   #check in which of the rows of track our test falls
    R[L-1]=compare[num,:]
    Weight=Weight*W
    if L < N-1:
        Addbead(R,Weight,L+1,anglenum,0)
    return R, Weight
print Addbead(R,1,L,anglenum,0)
