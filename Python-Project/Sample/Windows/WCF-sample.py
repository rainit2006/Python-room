# -*- coding: utf-8 -*-
"""
Created on Wed Sep 13 16:56:12 2017

@author: svf14n29
"""

# coding: utf-8
import clr
clr.AddReference("System.ServiceModel")
clr.AddReference("WcfServiceLibrary1.dll")

from System.ServiceModel import *
from SampleLib import *

binding = NetNamedPipeBinding()
factory = ChannelFactory[ISampleService](binding, "net.pipe://localhost/sample")
#サービスプロキシの取得
service = factory.CreateChannel()

data = SampleData()
data.Id = 100
data.Name = "テストデータ"

#サービスの実行
service.AddData(data)

factory.Close()
