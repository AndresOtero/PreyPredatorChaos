class Model(object):

    def __init__(self,diccModelValues):
        # these are our constants
        self.diccModelValues=diccModelValues
        self.hasFixedMeanTrait=False

    def setFixedMeanTrait(self,fixedMeanTrait):
        self.fixedMeanTrait=fixedMeanTrait
        self.hasFixedMeanTrait=True

    def unSetFixedMeanTrait(self):
        self.hasFixedMeanTrait=False

    def Lorenz(self,state,t):
        # unpack the state vector
        x = state[0]
        y = state[1]
        z = state[2]

        sigma = 10.0
        rho = 28.0
        beta = 8.0 / 3.0
        self.sigma = sigma
        self.rho = rho
        self.beta = beta
        # compute state derivatives
        xd = self.sigma * (y-x)
        yd = (self.rho-z)*x - y
        zd = x*y - beta*z

        # return the state derivatives
        return [xd, yd, zd]

    def function(self,state,t):
        x = state[0]
        y = state[1]
        c = state[2]

        a1 = self.diccModelValues['a1']
        a2 = self.diccModelValues['a2']
        a3 = self.diccModelValues['a3']
        d1 = self.diccModelValues['d1']
        d2 = self.diccModelValues['d2']
        b1 = self.diccModelValues['b1']
        b2 = self.diccModelValues['b2']
        k1 = self.diccModelValues['k1']
        k2 = self.diccModelValues['k2']
        k4 = self.diccModelValues['k4']
        y_a = self.diccModelValues['y_a']
        V = self.diccModelValues['V']

        if(self.hasFixedMeanTrait):
            c = self.fixedMeanTrait

        # compute state derivatives
        xd = x*(a1*(c/(1+b1*c))-a3*(y/(1+b2*x))-d1)
        yd = y*(a2*(x/(1+b2*x))-d2)
        cd = c*V*( (2*k2*d1) - (4*k4*d1)*c*c-(a1*k1)*(x/(1+b1*c)) )
        #cd=c*V*xd/x
        # return the state derivatives
        return [xd, yd, cd]
