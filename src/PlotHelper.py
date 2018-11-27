import matplotlib.pyplot as plt
from matplotlib import  cm

class PlotHelper(object):
    def plot2d(list_of_lines, t, legends=[], xLimMin=0, xLimMax=0, yLimMin=0, yLimMax=0, xLabel="x", yLabel="y",
               title="", invert_x=False):
        fig = plt.figure()
        ax = fig.gca()
        for line in list_of_lines:
            ax.plot(t, line)
        ax.legend(legends, loc=1)
        if (xLimMax != 0):
            ax.set_xlim(xLimMin, xLimMax)
        if (yLimMax != 0):
            ax.set_ylim(yLimMin, yLimMax)
        ax.set_xlabel(xLabel)
        ax.set_ylabel(yLabel)
        ax.set_title(title)
        if invert_x:
            ax.invert_xaxis()
        plt.savefig(title + ".png")
        plt.grid(True)
        plt.show()

    def plot3d(x, y, z, xLimMin=0, xLimMax=0, yLimMin=0, yLimMax=0 ,label_x="x", label_y="y", label_z="z", title=""):
        fig = plt.figure()
        ax = fig.gca(projection='3d')
        ax.plot(x, y, z)
        ax.set_xlabel(label_x)
        ax.set_ylabel(label_y)
        ax.set_zlabel(label_z)
        ax.set_title(title)
        if (xLimMax != 0):
            ax.set_xlim(xLimMin, xLimMax)
        if (yLimMax != 0):
            ax.set_ylim(yLimMin, yLimMax)
        plt.savefig(title + ".png")
        plt.grid(True)

        plt.show()

    def scatter3d(x, y, z, xLimMin=0, xLimMax=0, yLimMin=0, yLimMax=0, label_x="x", label_y="y", label_z="z", title=""):
        fig = plt.figure()
        ax = fig.gca(projection='3d')
        ax.scatter(x, y, z)
        ax.set_xlabel(label_x)
        ax.set_ylabel(label_y)
        ax.set_zlabel(label_z)
        ax.set_title(title)
        if (xLimMax != 0):
            ax.set_xlim(xLimMin, xLimMax)
        if (yLimMax != 0):
            ax.set_ylim(yLimMin, yLimMax)
        plt.savefig(title + ".png")
        plt.grid(True)
        plt.show()

    def plotHeatMapWithLines(x,y,z,line1=[],line2=[],legends=[],xLimMin=0,xLimMax=0, yLimMin=0, yLimMax=0,label_x="x", label_y="y", title=""):
        # PlotHelper.scatter3d(r_matrix[:,0],r_matrix[:,1],r_matrix[:,2])
        fig = plt.figure()
        ax = fig.gca()
        ax.legend(legends, loc=1)
        ax.set_xlabel(label_x)
        ax.set_ylabel(label_y)
        # ax.imshow(r_matrix,interpolation='nearest',extent=[t[0],t[-1],c_array[0],c_array[-1]])
        cntr = ax.contourf(x, y, z, cmap=cm.RdYlBu_r)
        fig.colorbar(cntr, ax=ax)
        if (xLimMax != 0):
            ax.set_xlim(xLimMin, xLimMax)
        if (yLimMax != 0):
            ax.set_ylim(yLimMin, yLimMax)
        ax.plot(line1, color="k", linewidth=1, linestyle='dashed')
        ax.plot(line2, color="m", linewidth=1, linestyle='dashed')
        ax.set_title(title)
        plt.savefig(title + ".png")
        plt.grid(True)
        plt.show()