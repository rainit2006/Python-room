# -*- coding: utf-8 -*-
"""
Created on Fri Sep 14 13:31:59 2018

@author: toui
"""
import copy

def copyTest():
    a = list(range(0, 10))
    #a = [1, 2, 3, 4, 5]
    b = a
    b.append(11)
    print('a = %s' % a)
    print('a_id = %i' % id(a))
    print('b = %s' % b)
    print('b_id = %i' % id(b))
    
def copyTest_copy():
    print("### copy.copy() ####")
    a = list(range(0, 10))
    #a = [1, 2, 3, 4, 5]
    b = copy.copy(a)
    b.append(11)
    print('a = %s' % a)
    print('a_id = %i' % id(a))
    print('b = %s' % b)
    print('b_id = %i' % id(b))
    
    a_obj = [list(range(0,3)), list(range(4,6))]
    b_obj= copy.copy(a_obj)
    b_obj[0].append(12)
    print('a_obj = %s' % a_obj)
    print('a_obj_id = %i' % id(a_obj))
    print('b_obj = %s' % b_obj)
    print('b_obj_id = %i' % id(b_obj))
    print('\n')
    
    
def copyTest_deepcopy():
    print("###Deep copy####")
    a = list(range(0, 10))
    #a = [1, 2, 3, 4, 5]
    b = copy.deepcopy(a)
    b.append(11)
    print('a = %s' % a)
    print('a_id = %i' % id(a))
    print('b = %s' % b)
    print('b_id = %i' % id(b))
    
    a_obj = [list(range(0,3)), list(range(4,6))]
    b_obj= copy.deepcopy(a_obj)
    b_obj[0].append(12)
    print('a_obj = %s' % a_obj)
    print('a_obj_id = %i' % id(a_obj))
    print('b_obj = %s' % b_obj)
    print('b_obj_id = %i' % id(b_obj))
    print('\n')



if __name__ == '__main__':
    #copyTest()
    copyTest_copy()
    copyTest_deepcopy()