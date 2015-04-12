#Rosenbluth
import numpy as np
import scipy.optimize as opt
import math
from LJcalc import ljcalc
import matplotlib.pyplot as plt 
pi=math.pi
cos=math.cos
sin=math.sin
exp=math.exp
    
def Addbead(beadpos,Weight,L,anglenum,U,polsize,Prunevec,num,beadposlist,WeightVec,weightlist): 
    
    startang=np.random.random()
    w = np.zeros((anglenum,1))
    compare=np.zeros((anglenum,2))
    alphaup=2
#    alphadown=0
    for i in range (anglenum):
        theta = startang + i* 2 * pi/anglenum
        beadpos[L,:]=[beadpos[L-1,0]+cos(theta),beadpos[L-1,1]+sin(theta)]
        compare[i,:]= beadpos[L,:]
        E=ljcalc(beadpos,L+1,U,polsize)
        w[i,0]=exp(-E)
    W = np.sum(w)
    WeightVec[L]=W
    if W ==0:
        print  "Last Beadnumber =", L
        newpos=np.zeros((L-1,2))
        newpos[0:L-1,:]=beadpos[0:L-1,:]
        beadposlist.append(newpos)
        weightlist.append(WeightVec)
    else:
#        print W
        Prunevec[L]=(Prunevec[L]+W)
        num[L]=num[L]+1.0
        AvW3=Prunevec[2]/num[2]
        AvWL=Prunevec[L]/num[L]
        Track = np.cumsum(w/W)
        Test=np.random.random()
        for i in range (len(Track)):   
            if Test < Track[i]:      
                numb = i   #check in which of the rows of track our test falls
                Test=Test+1 # Ensures we only have 1 found value
        beadpos[L,:]=compare[numb,:]
        Weight=(Weight*W)/(0.75*anglenum)
        WeightVec[L]=Weight
        UpLim=alphaup*AvWL/AvW3
#        LowLim=alphadown*AvWL/AvW3
        if L < polsize-1:
            if Weight > UpLim:
                print  "Multiplying strong chain"
                NewWeight=0.5*Weight
                Addbead(beadpos,NewWeight,L+1,anglenum,0,polsize,Prunevec,num, beadposlist,WeightVec,weightlist)
                Addbead(beadpos,NewWeight,L+1,anglenum,0,polsize,Prunevec,num, beadposlist,WeightVec,weightlist)
#            elif Weight < LowLim:
#                Elimnum=np.random.random()
#                print LowLim, Weight, UpLim
#                if Elimnum < 0.5:
#                    print "Pruning weak chain"
#                    NewWeight=2*Weight
#                    Addbead(beadpos,NewWeight,L+1,anglenum,0,polsize,Prunevec,num, beadposlist)
            else:
                Addbead(beadpos,Weight,L+1,anglenum,0,polsize,Prunevec,num, beadposlist,WeightVec,weightlist)
                
        else:
            beadposlist.append(beadpos)
            weightlist.append(WeightVec)
    return num, beadposlist,weightlist



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
    

def Stat(A,polpop,polsize):
#    weights = np.reshape(weights,(polpop))
    A_mask = np.ma.MaskedArray(A,mask=0)
    mean, sumweights = np.ma.average(A_mask,axis=0,returned=True)
    var = np.ma.std (A_mask,axis=0)/(np.arange(polsize)**(0.5))
#    var = np.ma.std(A_mask, axis=0)
    return mean, var

def func(x,a):
    return a*x**1.5   
    
def Fit(polsize,y,y_error,ylabel,title):
    x = np.arange(polsize)
    a,cov = opt.curve_fit(func,x,y,0.0,None)
    plt.figure()
    plt.xscale('log')
    plt.yscale('log')
    plt.errorbar(x[2:],y[2:], y_error[2:],linestyle = 'none',marker='x')
    plt.plot(x[2:],func(x[2:],a))
    plt.xlabel("N")
    plt.ylabel(ylabel)
    plt.title(title)
    return a