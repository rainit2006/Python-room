# -*- coding: utf-8 -*-
"""
Created on Fri Sep 29 2017
@author: Deng Wei (wei.deng@sony.com)
"""
import xlwt
import pandas as pd


if __name__ == '__main__':
    #read data from xls
    df = pd.read_excel(r'対象リストVer.0.02_Region別機種.xlsx', sheetname=r'Region別機種', 
                       header = 0)
    df = df.fillna(0)
    df = df.dropna()
    #print(df.head(5))
    data_list = df.loc[:, 'Model in PRS']
    #print(data)
    #print(data_list[1])
    book = xlwt.Workbook()
    sheet = book.add_sheet('result', cell_overwrite_ok=True)


    #replace pattern
    match_src = [r'[ITC', r'[ITE', r'[ITD', r'[AP', r'[CN']
    match_dst = [r'@[ITC', r'@[ITE', r'@[ITD', r'@[AP', r'@[CN']
    head_row = ['original', 'ITC', 'ITE', 'ITD', 'AP', 'CN', 'Other']
    
    for i in range(len(head_row)):
        sheet.write(0, i, head_row[i])
    
    for index, data in enumerate(data_list):
        sheet.write(index+1, 0, data)
        
        #replace the region word in order to slipt them easely. 
        dst = data
        for i, word in enumerate(match_src):
            dst = dst.replace(word, match_dst[i])     
        #print(dst)
        
        #split data into several small region group 
        dst = dst.split('@')
        for col in range(5): # 5 means the count of ITC/ITE/ITD/AP/CN
            cell = ''      
            #print('########'+ head_row[col+1] +'############')
            for j, item in enumerate(dst):
                if((head_row[col+1] in item) == True):
                    #print("find :"+item)
                    cell = cell+ item+ ';'
                    dst[j] = ''                   
            #print('-------------------')
            sheet.write(index+1, col+1, cell)
                    
                    
        if len(dst) != 0:
            #print("other is " + dst)
            sheet.write(index+1, 6, dst)
    #save result into a new xls
    book.save('result.xls')
    
 
    
    
