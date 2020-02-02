from Mandelbrot import Mandelbrot

def main ():
    resolution = 500
    maxIterations = 255
    mySet = Mandelbrot(resolution, resolution, maxIterations)
    mySet.showSet()

main()


