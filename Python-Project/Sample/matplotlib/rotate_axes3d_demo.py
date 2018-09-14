# -*- coding: utf-8 -*-
"""
Created on Thu Sep 13 10:51:18 2018

@author: toui
"""
import numpy as np
from mpl_toolkits.mplot3d import axes3d
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import matplotlib.animation as animation
import tkinter as Tk

def animate(angle):
    # rotate the axes and update
        ax.view_init(angle, angle)
        #plt.rcParams["font.size"] = 5
        #ax.margins(-5, -0.5)   
    

root = Tk.Tk()
label = Tk.Label(root,text="3d animation").grid(column=0, row=0)

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')


canvas = FigureCanvasTkAgg(fig, master=root)
canvas.get_tk_widget().grid(column=0,row=1)

# load some test data for demonstration and plot a wireframe
X, Y, Z = axes3d.get_test_data(0.1)
ax.plot_wireframe(X, Y, Z, rstride=5, cstride=5)
ani = animation.FuncAnimation(fig, animate, np.arange(0, 360), interval=25, blit=False)

    
Tk.mainloop()
    