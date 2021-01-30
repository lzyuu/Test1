import pyqtgraph as pg
import numpy as np 

app = pg.mkQApp()

window = pg.GraphicsWindow()
window.setWindowTitle(u"多条曲线")
window.resize(1080,720)

x = np.linspace(-5 * np.pi, 5*np.pi, 500)
y1 = 0.5*np.sin(x)
y2 = 2*np.cos(x)
y3 = np.sinc(x)

p = window.addPlot(Left = "Amplitude",bottom = "x",title = "y=sinx y2=cosx y3=sincx")
curve = p.plot(x,y1,pen = "r")
p.plot(x,y2,pen = "g")
p.plot(x,y3,pen = "y")

p.showGrid(x=True, y=True)
p.setRange(xRange = [-5 * np.pi, 5*np.pi],yRange = [-2.3,2.3],padding = 0)

app.exec_()

while 1 :
    pass

