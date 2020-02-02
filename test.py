import numpy as np

xDim = 5
yDim = 5

x = np.linspace(0,4,xDim)
y = np.linspace(0,4, yDim)
XX, YY = np.meshgrid(x,y)

for row in range(0,xDim):
    for col in range (0,yDim):
        xVal = XX[row][col]
        yVal = YY[row][col]
        print (xVal, yVal)