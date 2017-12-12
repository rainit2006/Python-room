# -*- coding: utf-8 -*-
"""
PCA Calculator

version: 1.0

PyQt4 Tutorial
http://www.slideshare.net/RansuiIso/pyqtgui

Created on Thu Jan 22 14:43:19 2015
@author: Tomoyuki Nohara
"""
import sys
#import PyQt4.QtGui as QtGui
#import PyQt4.QtCore as QtCore

from PyQt5.QtWidgets import (QApplication, QWidget, QPushButton, 
                             QGridLayout, QSizePolicy, QLCDNumber, 
                             QFrame, QVBoxLayout, QMainWindow)

from PyQt5.QtGui import QPainter, QPen
import PyQt5.QtCore as QtCore
import random
import numpy

class ButtonBoxWidget(QWidget):

    def __init__(self, parent=None):
        # コンストラクタ
        QWidget.__init__(self, parent=parent)
        # 実際の生成コード
        self.setup_ui()


    def setup_ui(self):
        
        self.setAutoFillBackground(True)
        p = self.palette()
        p.setColor(self.backgroundRole(), QtCore.Qt.red)
        self.setPalette(p)
        # QPushButtonのインスタンスを作る
        self.start_button = QPushButton("START", parent=self)
        self.stop_button = QPushButton("STOP", parent=self)
        self.reset_button = QPushButton("RESET", parent=self)
        self.quit_button = QPushButton("QUIT", parent=self)

        # Buttonをレイアウトマネージャに入れる
        layout = QGridLayout()
        layout.addWidget(self.start_button, 0, 0)
        layout.addWidget(self.stop_button, 0, 1)
        layout.addWidget(self.reset_button, 1, 0)
        layout.addWidget(self.quit_button, 1, 1)
        
        # レイアウトマネージャをWidgetに入れる
        self.setLayout(layout)
        



class CountDownWidget(QWidget):
    
    def __init__(self, parent=None):
        # コンストラクタ
        QWidget.__init__(self, parent=parent)
        self.interval = 10  
        
        self.setup_ui()
        
    def setup_ui(self):
        self.setAutoFillBackground(True)
        p = self.palette()
        p.setColor(self.backgroundRole(), QtCore.Qt.white)
        self.setPalette(p)
        
        self.setSizePolicy(QSizePolicy.Expanding, 
                           QSizePolicy.Expanding)
        self.timer = QtCore.QTimer(parent=self)
        self.timer.setInterval(self.interval)
        self.timer.timeout.connect(self.do_countdown)
        
        self.lcd_number = QLCDNumber(parent=self)
        self.lcd_number.setSizePolicy(QSizePolicy.Expanding, 
                                      QSizePolicy.Expanding)
        self.lcd_number.setFrameStyle(QFrame.NoFrame)
        self.lcd_number.setSegmentStyle(QLCDNumber.Flat)
        self.lcd_number.setDigitCount(6)
        
        layout = QVBoxLayout()
        layout.addWidget(self.lcd_number)
        self.setLayout(layout)
        
        self.reset_count()

        
    def update_display(self):
        self.lcd_number.display("%6.2f" % (self.count / 100))
        self.lcd_number.update()
    
    def do_countdown(self):
        self.count -= 1
        self.update_display()
        if self.count <= 0:
            self.stop_countdown()
            
    def start_countdown(self):
        if self.count > 0:
            self.timer.start()
            
    def stop_countdown(self):
        self.timer.stop()
        
    def reset_count(self):
        self.count = 18000
        self.update_display()
        
        
class GraphPanelWidget(QWidget):
    #self.panelsize = [300 ,200]
    def __init__(self, parent=None):
        QWidget.__init__(self, parent=parent)
        self.mx=[]
        self.my=[]
        self.pointList = QtCore.QPoint()
        self.pointPyList =[[],[]]
        self.pca_vector = [[0,0],[1,1]]
        self.x0 = 1
        self.y0 = 1      
        self.setup_ui()
    
    def setup_ui(self):
        self.setAutoFillBackground(True)
        p = self.palette()
        p.setColor(self.backgroundRole(), QtCore.Qt.yellow)
        self.setPalette(p)

        self.setFixedSize(320, 320)
        layout = QVBoxLayout()
        # レイアウトマネージャをWidgetに入れる
        self.setLayout(layout)
        
    """ PAINT EVENT """
    def paintEvent(self, pe):
        qp = QPainter()
        pen = QPen()
        pen.setColor(QtCore.Qt.black)
        pen.setWidth(3)
        qp.begin(self)
        qp.setPen(pen)
        """ Draw Method """
        self.drawOnePoints(qp)
        qp.end()

    def drawOnePoints(self, qp):
        # qp.drawPoint(self.mx, self.my)
        qp.drawPoints(self.pointList)
        
        for i in range(len(self.pointPyList[0])):
            qp.drawPoint(self.pointPyList[0][i], self.pointPyList[1][i])
        
        """ 主成分ベクトルの表示 """
        pen = QPen()
        pen.setWidth(2)
        """ 第1主成分 """
        pen.setColor(QtCore.Qt.red)
        qp.setPen(pen)
        px = self.pca_vector[0][0]
        py = self.pca_vector[0][1]
        qp.drawLine(-1*px+self.x0, -1*py+self.y0, px+self.x0, py+self.y0)
        
        """ 第2主成分 """
        pen.setColor(QtCore.Qt.blue)
        qp.setPen(pen)
        px = self.pca_vector[1][0]
        py = self.pca_vector[1][1]
        qp.drawLine(-1*px+self.x0, -1*py+self.y0, px+self.x0, py+self.y0)
         
    def mousePressEvent(self, e):
        size = self.size()
        self.x0 = size.width()/2
        self.y0 = size.height()/2
        print("axiszero(x0, y0) = (%0.2f, %0.2f)" % (self.x0, self.y0))
        
        self.mx = e.x()
        self.my = e.y()
        print("mouse press (x,y)=(%d, %d)" % (self.mx, self.my))
        
        """ ポイントを格納 """        
        self.pointPyList[0].append(self.mx)
        self.pointPyList[1].append(self.my)
        print(str(self.pointPyList))
        
        """ 主成分分析を実行 """
        points = numpy.array(self.pointPyList).T
        print("--- ana data ---")
        print(points)

        #print(points.T)
        pca = self.PCA(points)
        scale_pcav = 100
        pca1x = pca[0][0] * scale_pcav
        pca1y = pca[1][0] * scale_pcav
        pca2x = pca[0][1] * scale_pcav
        pca2y = pca[1][1] * scale_pcav
        self.pca_vector = [[pca1x, pca1y],[pca2x, pca2y]]
        print("---- pca ----")
        print(pca)
        
 
    def mouseReleaseEvent(self, e):
        print("mouse Release (x,y)=(%d, %d)" % (e.x(),e.y()))
        self.update()

    def mouseDoubleClickEvent(self, e):
        print("mouseDoubleClick")   
        
    def mouseMoveEvent(self, e):
        #print("mouseMove=" + bin(int(e.buttons())))
        self.mx = e.x()
        self.my = e.y()
        self.pointPyList[0].append(self.mx)
        self.pointPyList[1].append(self.my)

        
    def weelEvent(self, e):
        print("mouseWeel=")
        
    def PCA(self,P):
        m = sum(P)/ float(len(P))
        P_m = P - m
        l, v = numpy.linalg.eig(numpy.dot(P_m.T,P_m))
        return v.T
        
    def reset_cal(self):
        self.mx=[1]
        self.my=[1]
        self.pointList = QtCore.QPoint()
        self.pointPyList =[[],[]]
        self.pca_vector = [[0,0],[1,1]]
        self.x0 = 1
        self.y0 = 1      
        self.update()
        
def main():
    app = QApplication(sys.argv)
    panel = QWidget()
    
    """ 子Widget """
    countdown_widget = CountDownWidget(parent=panel)
    button_box_widget = ButtonBoxWidget(parent=panel)    
    graph_panel_widget = GraphPanelWidget(parent=panel)

    """ レイアウトマネージャ """    
    panel_layout = QVBoxLayout()
    panel_layout.addWidget(countdown_widget)
    panel_layout.addWidget(button_box_widget)
    panel_layout.addWidget(graph_panel_widget)

    """ Panel Widget """
    panel.setLayout(panel_layout)

    #panel.setFixedSize(320, 200)
    
    """ Main Window """
    main_window = QMainWindow()
    main_window.setWindowTitle("Ramen Timer")
    main_window.setCentralWidget(panel)
    
    main_window.show()
    
    """ Conectivity """
    button_box_widget.start_button.clicked.connect(countdown_widget.start_countdown)
    button_box_widget.stop_button.clicked.connect(countdown_widget.stop_countdown)
    button_box_widget.reset_button.clicked.connect(graph_panel_widget.reset_cal)
    button_box_widget.quit_button.clicked.connect(app.quit)
    
    app.exec_()
    
if __name__ == '__main__':
    print("app main start")
    main()
    