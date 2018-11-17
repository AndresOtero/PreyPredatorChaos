from cProfile import label
import numpy as np
import scipy.integrate as spi
import matplotlib.pyplot as plt
from scipy.integrate import odeint
from mpl_toolkits.mplot3d import Axes3D

class Model(object):

    def __init__(self,diccModelValues):
        # these are our constants
        self.diccModelValues=diccModelValues
        self.hasFixedMeanTrait=False
        self.a1 = self.diccModelValues['a1']
        self.a2 = self.diccModelValues['a2']
        self.a3 = self.diccModelValues['a3']
        self.d1 = self.diccModelValues['d1']
        self.d2 = self.diccModelValues['d2']
        self.b1 = self.diccModelValues['b1']
        self.b2 = self.diccModelValues['b2']
        self.k1 = self.diccModelValues['k1']
        self.k2 = self.diccModelValues['k2']
        self.k4 = self.diccModelValues['k4']
        self.y_a = self.diccModelValues['y_a']
        self.V = self.diccModelValues['V']


    def setFixedMeanTrait(self,fixedMeanTrait):
        self.fixedMeanTrait=fixedMeanTrait
        self.hasFixedMeanTrait=True

    def unSetFixedMeanTrait(self):
        self.hasFixedMeanTrait=False

    def function(self,state,t):
        x = state[0]
        y = state[1]
        c = state[2]

        if(self.hasFixedMeanTrait):
            c = self.fixedMeanTrait

        # compute state derivatives
        xd = x*(self.a1*(c/(1+self.b1*c))-self.a3*(y/(1+self.b2*x))-self.d1)
        yd = y*(self.a2*(x/(1+self.b2*x))-self.d2)
        cd = c*self.V*( (2*self.k2*self.d1) - (4*self.k4*self.d1)*c*c-(self.a1*self.k1)*(x/(1+self.b1*c)) )
        #cd=c*V*xd/x
        # return the state derivatives
        return [xd, yd, cd]

    def r(self,x,y,c):
        firstTerm=self.a1*(c/(1+self.b1*c))
        secondTerm=-1*self.d1#*(1-self.k2*(c**2-c**(-2))+self.k4*(c**4-c**(-4)))
        thirdTerm=self.a2*(x*y)/(1+self.b2*x)
        return (firstTerm+secondTerm+thirdTerm)

    def calculateR(self):
        return np.array([self.r(state[0], state[1], state[2]) for state in self.states])

    def simulate(self,state0,t):
        self.states=  odeint(self.function, state0, t)
        return  self.states

    def getStates(self):
        return self.states

    def getXArray(self):
        return  self.states[:,0]

    def getYArray(self):
        return  self.states[:,1]

    def getCArray(self):
        return  self.states[:,2]