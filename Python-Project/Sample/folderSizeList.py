# -*- coding: utf-8 -*-
"""
List folder size

Created on Fri Aug 25 17:59:50 2017

@author: svf14n29
"""
import sys, os

def get_size(start_path = "."):
    total_size = 0
    for dirpath, dirnames, filenames in os.walk(start_path):
        for f in filenames:
            fp = os.path.join(dirpath, f)
            total_size += os.path.getsize(fp)
    return total_size


#arg = sys.argv
#directory = ""
#
#if arg is None:
#    directory = "C:\\Users\\svf14n29\\Desktop\\Code"
#else:
#    directory = arg    

directory = "C:\\Users\\svf14n29\\Desktop\\Code"
#print(directory)
dirs = os.listdir(directory)

# This would print all the files and directories
for dir in dirs: 
   dir_size = get_size(os.path.join(directory,dir))
   print (dir + ':'+ str(dir_size))




