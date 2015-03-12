#Rosenbluth
import numpy as np
import math
l = 1
kB = 1.38*10**-23
T = 1
eps = 0.25 
sig = 0.8
N=5
R = np.zeros ((2,2))
R[1] = [1,0]
#theta = np.zeros((1,6))
#r = np.zeros((1,6))
#E = np.zeros((1,6))
w = np.zeros((1,6))
for i in range (6):
    theta = np.random.random() + i * np.pi/6
    r = 2* l **2* (1-np.cos(theta))   
    E = 4 * eps * ( (sig/r)**12 - (sig/r)**6)
    w[0,i] = math.exp(-E)
    
W = np.sum(w)
w = w/W    
print w
#print W
