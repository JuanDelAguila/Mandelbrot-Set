import sys
from Mandelbrot import Mandelbrot

args = sys.argv[1:]

if len(args) != 2:
    raise ValueError("You must provide two arguments: the resolution (side length in pixels) and the maximum number of iterations")
else:
    resolution = float(args[0])
    maxIterations = float(args[1])

def main ():
    resolution = 500
    maxIterations = 255
    mySet = Mandelbrot(resolution, resolution, maxIterations)
    mySet.showSet()

main()


