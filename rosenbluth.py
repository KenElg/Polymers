#Rosenbluth
import numpy as np
import math
l = 1
kB = 1.38*10**-23
T = 1
eps = 0.25 
sig = 0.8
N=10
R = np.zeros ((N,2))
R[1] = [1,0]
pi=np.pi
cos=np.cos
sin=np.sin
exp=np.exp
anglenum=6
w = np.zeros((1,anglenum))
compare=np.zeros((anglenum,2))
def Addbead(R,Weight,L,anglenum):
    startang=np.random.random() 
    for i in range (anglenum):
        theta = startang + i* 2 * pi/anglenum
        R[L+1]=[R[L,1]+cos(theta),R[L,2]+sin(theta)]
        compare[:,i]=R[L+1]
        E=LJcalc(R)
        w[i]=exp(-E)
    W = np.sum(w)
    Track = np.cumsum(w/W)
    Test=np.random.random()
    num= #check in which of the rows of track our test falls
    R[L+1]=compare[:,num]
    Weight=Weight*W
    if L<N
        Addbead(R,Weight,L+1,anglenum)        

