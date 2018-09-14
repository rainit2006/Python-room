# -*- coding: utf-8 -*-
"""
Created on Wed Sep 12 18:06:33 2018

@author: toui
"""

import matplotlib.pyplot as plt
import numpy as np
from matplotlib.image import imread
from mpl_toolkits.mplot3d import Axes3D

x = z = np.linspace(-100, 100, 256)
x , z = np.meshgrid(x, z)
y = (255 - imread('lena_gray.png')*255) * 10 #バラけさせたい

root = Tk.Tk()
label = Tk.Label(root,text="3d animation").grid(column=0, row=0)



fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.scatter3D(np.ravel(x), np.ravel(z), np.ravel(y),s=10,marker='.')
ax.set_title("image")

canvas = FigureCanvasTkAgg(fig, master=root)
canvas.get_tk_widget().grid(column=0,row=1)





#plt.show()
Tk.mainloop()