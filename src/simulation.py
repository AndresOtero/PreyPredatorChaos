from cProfile import label
from Model import  Model
from PlotHelper import PlotHelper
import numpy as np


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

def compareFixedMeanTrait(fixedMeanTraits,state0,t,legends=[],yLimMin=0,yLimMax=0,xLabel="x",yLabel="y",title=""):
    print("Fixed Mean Traits ", fixedMeanTraits)
    list_of_lines=[]
    for fixedMeanTrait in fixedMeanTraits:
        model.setFixedMeanTrait(fixedMeanTrait)
        model.simulate(state0,t)
        list_of_lines.append( model.getXArray())
    PlotHelper.plot2d(list_of_lines,t,legends,yLimMin=yLimMin,yLimMax=yLimMax,xLabel=xLabel,yLabel=yLabel,title=title)


fixedMeanTrait=d1/(a1-b1*d1)
state0 = [2.0, 0.0, 0.0]
t = np.linspace(0.0, 80.0, 800)
legends=["c < d1/(a1-b1*d1)","c = d1/(a1-b1*d1)","c > d1/(a1-b1*d1)"]
fixedMeanTraits=[fixedMeanTrait-0.05,fixedMeanTrait,fixedMeanTrait+0.05]
compareFixedMeanTrait(fixedMeanTraits,state0,t,legends,yLimMin=t.min(),yLimMax=t.max(),xLabel="t",yLabel="x",title="Rasgo medio fijo")

state0 = [0.5, 0.3, 0.5]
t = np.linspace(0.0,  5000,  5000)
diccModelValues["V"]=(1/3)*0.2
model=Model(diccModelValues)
model.simulate(state0,t)
PlotHelper.plot2d([model.getXArray(),model.getYArray(),model.getCArray()],t,["x","y","c"],xLabel="t",title="Interacciones Predador-Presa con variacion genetica lenta")
PlotHelper.plot2d([model.getXArray(),model.getYArray(),model.getCArray()],t,["x","y","c"],xLimMax=2000,xLimMin=1000,xLabel="t",title="Interacciones Predador-Presa con variacion genetica lenta (zoom)")
PlotHelper.plot2d([model.getXArray(),model.getYArray()],t,["x","y"],xLimMax=2000,xLimMin=1000,xLabel="t",title="Interacciones Predador-Presa con variacion genetica lenta (zoom) sin c ")

diccModelValues["V"]=(1/3)
model=Model(diccModelValues)
state0 = [0.5, 0.3, 0.5]
t = np.linspace(0.0,  5000,  10*5000)
states=model.simulate(state0,t)
PlotHelper.plot2d([model.getXArray(),model.getYArray(),model.getCArray()],t,legends=["x","y","c"],xLabel="t",title="Interacciones Predador-Presa con caos")
PlotHelper.plot2d([model.getXArray(),model.getYArray(),model.getCArray()],t,legends=["x","y","c"],xLabel="t",title="Interacciones Predador-Presa con caos (zoom)", xLimMin=500,xLimMax=2000)

PlotHelper.plot3d(model.getXArray(),model.getYArray(),model.getCArray(),label_x="x",label_y="y",label_z="c",title="Interacciones Predador-Presa con caos 3-d")

PlotHelper.plot2d([model.getYArray()],model.getXArray(),yLabel="y",xLabel="x",title="Interacciones Predador-Presa con caos (plano xy)")
PlotHelper.plot2d([model.getCArray()],model.getXArray(),yLabel="c",xLabel="x",title="Interacciones Predador-Presa con caos (plano xc)")
PlotHelper.plot2d([model.getYArray()],model.getCArray(),yLabel="y",xLabel="c",title="Interacciones Predador-Presa con caos (plano cy)",invert_x=True)

c_array = np.linspace(0.0,  1.0,  25)
model=Model(diccModelValues)
state0 = [0.5, 0.3, 0.5]
t = np.linspace(0.0,  800.0 ,  800)
states=model.simulate(state0,t)
PlotHelper.plot2d([model.getXArray(),model.getYArray(),model.getCArray()],t,legends=["x","y","c"],xLimMin=250,xLimMax=800,xLabel="t",title="Interacciones Predador-Presa con la funcion de aptitud")
PlotHelper.plot3d(r,t,model.getCArray(),yLimMin=250,yLimMax=800,label_x="r",label_y="t",label_z="c",title="Interacciones Predador-Presa con caos 3-d con la funcion de aptitud")

r_matrix=model.calculateR(c_array)
PlotHelper.plotHeatMapWithLines(t,c_array,r_matrix,line1=model.getCArray(),line2=model.getXArray(),legends=["c","x"],xLimMin=250,xLimMax=800,label_x="t",label_y="c",title="Mapa de calor funcion de adaptacion")

PlotHelper.plot2d([r_matrix[:,400]],c_array)
PlotHelper.plot2d([r_matrix[:,560]],c_array)