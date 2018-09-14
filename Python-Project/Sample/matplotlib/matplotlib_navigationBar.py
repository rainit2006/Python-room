# -*- coding: utf-8 -*-
"""
Created on Thu Sep 13 11:22:15 2018

@author: toui
"""
import numpy as np
import tkinter as tk
import matplotlib as mpl
from mpl_toolkits.mplot3d import axes3d
from matplotlib.patches import Rectangle
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2TkAgg

# custom toolbar with lorem ipsum text
class CustomToolbar(NavigationToolbar2TkAgg):
    def __init__(self,canvas_,parent_):
        self.toolitems = (
            ('Home', 'Lorem ipsum dolor sit amet', 'home', 'home'),
            ('Back', 'consectetuer adipiscing elit', 'back', 'back'),
            ('Forward', 'sed diam nonummy nibh euismod', 'forward', 'forward'),
            (None, None, None, None),
            ('Pan', 'tincidunt ut laoreet', 'move', 'pan'),
            ('Zoom', 'dolore magna aliquam', 'zoom_to_rect', 'zoom'),
            (None, None, None, None),
            ('Subplots', 'putamus parum claram', 'subplots', 'configure_subplots'),
            ('Save', 'sollemnes in futurum', 'filesave', 'save_figure'),
            )
        NavigationToolbar2TkAgg.__init__(self,canvas_,parent_)


class MyApp(object):
    def __init__(self,root):
        self.root = root
        self._init_app()

    # here we embed the a figure in the Tk GUI
    def _init_app(self):
        self.figure = mpl.figure.Figure()
        #self.ax = self.figure.add_subplot(111)
        self.ax = self.figure.add_subplot(111, projection='3d')
        self.canvas = FigureCanvasTkAgg(self.figure,self.root)
        self.toolbar = CustomToolbar(self.canvas,self.root)
        self.toolbar.update()
        self.plot_widget = self.canvas.get_tk_widget()
        self.plot_widget.pack(side=tk.TOP, fill=tk.BOTH, expand=1)
        self.toolbar.pack(side=tk.TOP, fill=tk.BOTH, expand=1)
        self.canvas.show()

    # plot something random
    def plot(self):
        #self.ax.imshow(np.random.normal(0.,1.,size=[100,100]),cmap="hot",aspect="auto")
        #self.figure.canvas.draw()
        
        X, Y, Z = axes3d.get_test_data(0.1)
        self.ax.plot_wireframe(X, Y, Z, rstride=5, cstride=5)

def main():
    root = tk.Tk()
    app = MyApp(root)
    app.plot()
    root.mainloop()

if __name__ == "__main__":
    main()