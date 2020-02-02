import numpy as np
import matplotlib.pyplot as plt

class Mandelbrot (object):

    def __init__(self, xDim, yDim, maxIter):
        self.maxIter = maxIter
        self.xDim = xDim
        self.yDim = yDim
        x = np.linspace(-2.025,0.6,xDim)
        y = np.linspace(-1.125,1.125, yDim)
        self.XX, self.YY = np.meshgrid(x, y)
    
    def showSet (self):
        setArray = np.zeros((self.xDim, self.yDim))
        for row in range(0,self.xDim):
            for col in range (0,self.yDim):
                xVal = self.XX[row][col]
                yVal = self.YY[row][col]
                c = complex (xVal, yVal)
                setArray[row][col] = self.inMandelbrotSet(c)
        plt.imshow(setArray)
        plt.axis('off')
        plt.show()

    def inMandelbrotSet(self, c):
        iterations = 0
        z = 0
        magnitude = 0
        while magnitude <= 2 and iterations <= self.maxIter:
            nextZ = z*z + c
            magnitude = abs(nextZ)
            z = nextZ
            iterations += 1
        return iterations
