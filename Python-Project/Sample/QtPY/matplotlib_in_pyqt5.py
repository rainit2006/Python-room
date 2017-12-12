# -*- coding: utf-8 -*-
"""
Created on Fri Sep  1 13:36:20 2017

@author: svf14n29
"""
import sys
import random
import pandas as pd
  
from PyQt5.QtWidgets import QApplication, QMainWindow, QMenu, QVBoxLayout, QSizePolicy, QMessageBox, QWidget, QPushButton
from PyQt5.QtGui import QIcon

from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure
import matplotlib.pyplot as plt

class App(QMainWindow):
 
    def __init__(self):
        super().__init__()
        self.left = 150
        self.top = 100
        self.title = 'PyQt5 matplotlib example - pythonspot.com'
        self.width = 860
        self.height = 600
        self.initUI()
 
    def initUI(self):
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)
 
        m = PlotCanvas(self, width=9, height=5)
        m.move(0,0)
 
        #button_read_data = QPushButton('Read data form xls', self)
        #layout = QGridLayout()
#        layout.addWidget(self.start_button, 0, 0)
#        layout.addWidget(self.stop_button, 0, 1)
#        layout.addWidget(self.reset_button, 1, 0)
#        layout.addWidget(self.quit_button, 1, 1)
        
        self.show()
 
 
class PlotCanvas(FigureCanvas):
 
    def __init__(self, parent=None, width=5, height=4, dpi=100):
        fig = Figure(figsize=(width, height), dpi=dpi)
        self.axes = fig.add_subplot(111)
 
        FigureCanvas.__init__(self, fig)
        self.setParent(parent)
 
        FigureCanvas.setSizePolicy(self,
                QSizePolicy.Expanding,
                QSizePolicy.Expanding)
        FigureCanvas.updateGeometry(self)
        
        
        #data = [random.random() for i in range(25)]
        data = self.excelData()
        self.plot(data)
 
 
    def plot(self, data):
        
        ax = self.figure.add_subplot(111)
        ax.plot(data, 'r-')
        ax.set_title(r'PyQt Matplotlib Example')
        self.draw()
        

    def excelData(self):
        df = pd.read_excel(r'Data_Account_20170809.xlsx', sheetname=r'Manual Feedback', 
                           header = 1)
        df = df.fillna(0)
        #print(df)
        data = df.iloc[7, 4:20]
        print(data)
        return data
    

        
if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = App()
    sys.exit(app.exec_())


