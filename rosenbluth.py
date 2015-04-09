#Rosenbluth
import numpy as np
import math
from LJcalc import ljcalc
import matplotlib.pyplot as plt 
pi=math.pi
cos=math.cos
sin=math.sin
exp=math.exp
    
def Addbead(beadpos,Weight,L,anglenum,U,polsize,Prunevec,num):  
    if num < 1000:
        startang=np.random.random()
        w = np.zeros((1,anglenum))
        compare=np.zeros((anglenum,2))
        alphaup=2
        alphadown=1.2
        for i in range (anglenum):
            theta = startang + i* 2 * pi/anglenum
            beadpos[L,:]=[beadpos[L-1,0]+cos(theta),beadpos[L-1,1]+sin(theta)]
            compare[i,:]= beadpos[L,:]
            E=ljcalc(beadpos,L+1,U,polsize)
            w[0,i]=exp(-E)
        W = np.sum(w)
        if W ==0:
            print  "Last Beadnumber =", L
            num=num+1.0
        else:
            Prunevec[L]=(Prunevec[L]+W)
            AvW3=Prunevec[2]/num
            AvWL=Prunevec[L]/num
            Track = np.cumsum(w/W)
            Test=np.random.random()
            for i in range (len(Track)):   
                if Test < Track[i]:      
                    num = i   #check in which of the rows of track our test falls
                    Test=Test+1 # Ensures we only have 1 found value
            beadpos[L]=compare[num,:]
            Weight=Weight*W
            UpLim=alphaup*AvWL/AvW3
            LowLim=alphadown*AvWL/AvW3
            if L < polsize-1:
                if Weight > UpLim:
                    print  "Multiplying strong chain"
                    NewWeight=0.5*Weight
                    Addbead(beadpos,NewWeight,L+1,anglenum,0,polsize,Prunevec,num)
                    NewWeight=0.5*Weight
                    Addbead(beadpos,NewWeight,L+1,anglenum,0,polsize,Prunevec,num)
                elif Weight < LowLim:
                    Elimnum=np.random.random()
                    if Elimnum < 0.5:
                        print "Pruning weak chain"
                        NewWeight=2*Weight
                        Addbead(beadpos,NewWeight,L+1,anglenum,0,polsize,Prunevec,num)
                else:
                    Addbead(beadpos,Weight,L+1,anglenum,0,polsize,Prunevec,num)
            else:
                num=num+1
            return beadpos, Weight, L, Prunevec, num



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
        RG2[0,j]=(1.0/j)*np.sum(Calc)
    return RG2
    

def Stat(A,weights,polpop,polsize):
    weights = np.reshape(weights,(polpop))
    A_mask = np.ma.MaskedArray(A,mask=0)
    mean, sumweights = np.ma.average(A_mask,axis=0, weights=weights,returned=True)
    var = np.ma.var (A_mask,axis=0)/(np.arange(polsize)**(0.5))
#    var = np.ma.std(A_mask, axis=0)
    return mean, var

def Fit(x,y):
    logx = np.log10(x[2:])
    logy = np.log10(y[2:])
    X = np.vstack([logx, np.ones(len(logx))]).T
    slope, intercept = np.linalg.lstsq(X, logy)[0]
    plt.figure()
    plt.xscale('log')
    plt.yscale('log')
    plt.plot(x[2:],y[2:],'x')
#    plt.plot(logx,logy,'x')
#    plt.plot(x[2:],np.power(10,intercept) * np.power(X,slope),'r')
    plt.plot(x[2:],10**(slope*logx+intercept),'r')
    return slope, intercept