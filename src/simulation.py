from cProfile import label
from Model import  Model
import numpy as np
import scipy.integrate as spi
import matplotlib.pyplot as plt
from scipy.integrate import odeint
from mpl_toolkits.mplot3d import Axes3D



"""state0 = [2.0, 3.0, 4.0]
t = np.linspace(0.0, 30.0, 3000)


model=Model({})
state = odeint(model.Lorenz, state0, t)
print(state)
print(len(state))

# do some fancy 3D plotting
fig = plt.figure()
ax = fig.gca(projection='3d')
ax.plot(state[:,0],state[:,1],state[:,2])
ax.set_xlabel('x')
ax.set_ylabel('y')
ax.set_zlabel('z')
plt.show()
"""
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

def compareFixedMeanTrait(fixedMeanTraits,state0,t,legends):
    print("Fixed Mean Trait ", fixedMeanTraits)
    fig = plt.figure()
    ax = fig.gca()
    for fixedMeanTrait in fixedMeanTraits:
        model.setFixedMeanTrait(fixedMeanTrait)
        stateFixedMeanTrait = odeint(model.function, state0, t)
        ax.plot(t, stateFixedMeanTrait[:, 0])
    ax.legend(legends)
    ax.set_ylim(0,50)
    plt.show()

def simulateModel(diccModelValues,state0,t):
    model=Model(diccModelValues)

    #model.unSetFixedMeanTrait()
    states = odeint(model.function, state0, t)
    return  states
def plot2d(states,t):
    fig = plt.figure()
    ax = fig.gca()
    ax.plot(t, states[:, 0])
    ax.plot(t, states[:, 1])
    ax.plot(t, states[:, 2])
    ax.legend(["x","y","c"])
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
#compareFixedMeanTrait(fixedMeanTraits,state0,t,legends)



diccModelValues["V"]=(1/3)
print(diccModelValues)
state0 = [0.5, 0.3, 0.5]
t = np.linspace(0.0,  5000,  5000)
states=simulateModel(diccModelValues,state0,t)
#plot2d(states,t)
#plot3d(states,t)
#plot2dvs(states,t)
diccModelValues["V"]=(1/3)*0.2
states=simulateModel(diccModelValues,state0,t)
plot2d(states,t)
diccModelValues["V"]=(1/3)
t = np.linspace(0,  800,  800*4)
states=simulateModel(diccModelValues,state0,t)
plot2d(states,t)