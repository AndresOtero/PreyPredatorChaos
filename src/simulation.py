from cProfile import label
from Model import  Model
from PlotHelper import PlotHelper
import numpy as np
import sys

show=False
if(len(sys.argv)==3):
    if(sys.argv[1]=='-s' or sys.argv[1]=='--show'):
        if (sys.argv[2] in ['true',"True"]):
            show = True
if(show):
    print("Show plots")
else:
    print("Doesn't show plots")

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

def compareFixedMeanTrait(fixedMeanTraits,state0,t,legends=[],yLimMin=0,yLimMax=0,xLabel="x",yLabel="y",title="",show=True):
    list_of_lines=[]
    for fixedMeanTrait in fixedMeanTraits:
        model.setFixedMeanTrait(fixedMeanTrait)
        model.simulate(state0,t)
        list_of_lines.append( model.getXArray())
    PlotHelper.plot2d(list_of_lines,t,legends,yLimMin=yLimMin,yLimMax=yLimMax,xLabel=xLabel,yLabel=yLabel,title=title,show=show)

#First simulation with fixed mean traits
fixedMeanTrait=d1/(a1-b1*d1)
state0 = [2.0, 0.0, 0.0]
t = np.linspace(0.0, 80.0, 800)
legends=["c < d1/(a1-b1*d1)","c = d1/(a1-b1*d1)","c > d1/(a1-b1*d1)"]
fixedMeanTraits=[fixedMeanTrait-0.05,fixedMeanTrait,fixedMeanTrait+0.05]
compareFixedMeanTrait(fixedMeanTraits,state0,t,legends,yLimMin=t.min(),yLimMax=t.max(),xLabel="t",yLabel="x",title="Rasgo medio fijo",show=show)

#Second simulation with slow evolution dynamics, non chaotic system
state0 = [0.5, 0.3, 0.5]
t = np.linspace(0.0,  5000,  5000)
diccModelValues["V"]=(1/3)*0.2
model=Model(diccModelValues)
model.simulate(state0,t)
PlotHelper.plot2d([model.getXArray(),model.getYArray(),model.getCArray()],t,["x","y","mean_c"],xLabel="t",title="Interacciones Predador-Presa con variacion genetica lenta",show=show)
PlotHelper.plot2d([model.getXArray(),model.getYArray(),model.getCArray()],t,["x","y","mean_c"],xLimMax=2000,xLimMin=1000,xLabel="t",title="Interacciones Predador-Presa con variacion genetica lenta (zoom)",show=show)
PlotHelper.plot2d([model.getXArray(),model.getYArray()],t,["x","y"],xLimMax=2000,xLimMin=1000,xLabel="t",title="Interacciones Predador-Presa con variacion genetica lenta (zoom) sin c ",show=show)

#Third simulation with fast evolution dynamics, chaotic system
diccModelValues["V"]=(1/3)
model=Model(diccModelValues)
state0 = [0.5, 0.3, 0.5]
t = np.linspace(0.0,  5000,  10*5000)
states=model.simulate(state0,t)
PlotHelper.plot2d([model.getXArray(),model.getYArray(),model.getCArray()],t,legends=["x","y","mean_c"],xLabel="t",title="Interacciones Predador-Presa con caos",show=show)
PlotHelper.plot2d([model.getXArray(),model.getYArray(),model.getCArray()],t,legends=["x","y","mean_c"],xLabel="t",title="Interacciones Predador-Presa con caos (zoom)", xLimMin=500,xLimMax=2000,show=show)

#3d plot
PlotHelper.plot3d(model.getXArray(),model.getYArray(),model.getCArray(),label_x="x",label_y="y",label_z="mean_c",title="Interacciones Predador-Presa con caos 3-d",show=show)

#planes plot
PlotHelper.plot2d([model.getYArray()],model.getXArray(),yLabel="y",xLabel="x",title="Interacciones Predador-Presa con caos (plano xy)",show=show)
PlotHelper.plot2d([model.getCArray()],model.getXArray(),yLabel="mean_c",xLabel="x",title="Interacciones Predador-Presa con caos (plano xc)",show=show)
PlotHelper.plot2d([model.getYArray()],model.getCArray(),yLabel="y",xLabel="mean_c",title="Interacciones Predador-Presa con caos (plano cy)",invert_x=True,show=show)

#Calculate and plot fitness function r
c_array = np.linspace(0.0,  1.0,  25)
model=Model(diccModelValues)
state0 = [0.5, 0.3, 0.5]
t = np.linspace(0.0,  800.0 ,  800)
states=model.simulate(state0,t)
PlotHelper.plot2d([model.getXArray(),model.getYArray(),model.getCArray()],t,legends=["x","y","mean_c"],xLimMin=250,xLimMax=800,xLabel="t",title="Interacciones Predador-Presa con la funcion de aptitud",show=show)

#Plot heat Map
r_matrix=model.calculateR(c_array)
PlotHelper.plotHeatMapWithLines(t,c_array,r_matrix,line1=model.getCArray(),line2=model.getXArray(),legends=["mean_c","x"],xLimMin=250,xLimMax=800,label_x="t",label_y="c",title="Mapa de calor funcion de adaptacion",show=show)

#Plot fitness landscapes
PlotHelper.plot2d([r_matrix[:,400]],c_array,xLabel="c",yLabel="r",title="Funcion de adaptacion vs c en t=400",show=show)
PlotHelper.plot2d([r_matrix[:,560]],c_array,xLabel="c",yLabel="r",title="Funcion de adaptacion vs c en t=560",show=show)