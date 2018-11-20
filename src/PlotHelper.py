import matplotlib.pyplot as plt

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
        plt.show()
