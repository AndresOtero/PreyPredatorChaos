from cProfile import label
from Model import  Model
import numpy as np
import scipy.integrate as spi
import matplotlib.pyplot as plt
from scipy.integrate import odeint
from mpl_toolkits.mplot3d import Axes3D
from matplotlib.colors import BoundaryNorm
from matplotlib.ticker import MaxNLocator
from matplotlib import cm

diccModelValues={
'a1': 2.5,
'a2': 0.05,
'a3': 0.4,
'd1': 0.16,
'd2': 0.004,
'b1': 6.0,
'b2': 4.0/3.0,
'k1': 6.0,
'k2': 9.0,
'k4': 9.0,
'y_a': 8.0,
'V' : 0
}

d1=diccModelValues['d1']
a1=diccModelValues['a1']
b1=diccModelValues['b1']

model=Model(diccModelValues)

def compareFixedMeanTrait(fixedMeanTraits,state0,t,legends,yLimMin=0,yLimMax=0,xLabel="x",yLabel="y"):
    print("Fixed Mean Traits ", fixedMeanTraits)
    fig = plt.figure()
    ax = fig.gca()
    for fixedMeanTrait in fixedMeanTraits:
        model.setFixedMeanTrait(fixedMeanTrait)
        model.simulate(state0,t)
        ax.plot(t, model.getXArray())
    ax.legend(legends)
    ax.set_ylim(yLimMin,yLimMax)
    ax.set_xlabel(xLabel)
    ax.set_ylabel(yLabel)
    plt.show()

def plot2d(states,t,leftLim=0,rigthLim=0):
    fig = plt.figure()
    ax = fig.gca()
    ax.plot(t, states[:, 0])
    ax.plot(t, states[:, 1])
    ax.plot(t, states[:, 2])
    ax.legend(["x","y","c"])
    if(rigthLim!=0 ):
        ax.set_xlim(leftLim,rigthLim)
    plt.show()

def plot2d_1vs1(state,t):
    fig = plt.figure()
    ax = fig.gca()
    ax.plot(t, state)
    ax.legend(["r"])
    ax.set_xlabel("t")
    plt.show()


def plot2d_r(states,r,t,leftLim=0,rigthLim=0):
    fig = plt.figure()
    ax = fig.gca()
    ax.plot(t, states[:, 0])
    ax.plot(t, states[:, 1])
    ax.plot(t, states[:, 2])
    ax.plot(t,r)
    ax.legend(["x","y","c","r"])
    if(rigthLim!=0 ):
        ax.set_xlim(leftLim,rigthLim)

    plt.show()

def plot2dvs(states,t):
    labels=["x","y","c"]
    plots=[(0,1),(0,2),(2,1)]
    for i,j in plots:
            fig = plt.figure()
            ax = fig.gca()
            ax.plot(states[:, i],states[:, j] )
            ax.set_xlabel(labels[i])
            ax.set_ylabel(labels[j])
            if(i==2 and j==1):
                ax.invert_xaxis()
            plt.show()


def plot3d(states,t):
    fig = plt.figure()
    ax = fig.gca(projection='3d')
    ax.plot(states[:,0],states[:,1],states[:,2])
    ax.set_xlabel('x')
    ax.set_ylabel('y')
    ax.set_zlabel('c')
    plt.show()

fixedMeanTrait=d1/(a1-b1*d1)
state0 = [2.0, 0.0, 0.0]
t = np.linspace(0.0, 80.0, 800)
legends=["c < d1/(a1-b1*d1)","c = d1/(a1-b1*d1)","c > d1/(a1-b1*d1)"]
fixedMeanTraits=[fixedMeanTrait-0.05,fixedMeanTrait,fixedMeanTrait+0.05]
compareFixedMeanTrait(fixedMeanTraits,state0,t,legends,yLimMin=t.min(),yLimMax=t.max(),xLabel="t",yLabel="x")


"""
diccModelValues["V"]=(1/3)
print(diccModelValues)
state0 = [0.5, 0.3, 0.5]
t = np.linspace(0.0,  5000,  5000)
model=Model(diccModelValues)
states=model.simulate(state0,t)
#plot2d(states,t)
#plot3d(states,t)
#plot2dvs(states,t)
diccModelValues["V"]=(1/3)*0.2
model=Model(diccModelValues)
states=model.simulate(state0,t)
#plot2d(states,t)
diccModelValues["V"]=(1/3)
t = np.linspace(0,  800,  800*5)
model=Model(diccModelValues)
states=model.simulate(state0,t)
#plot2d(states,t,250,800)
r=[model.r(state[0],state[1],state[2]) for state in states]
plot2d_r(states,r,t,250,800)
"""