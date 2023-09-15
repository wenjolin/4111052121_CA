#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Sep 15 21:20:49 2023

@author: 0yuan_0124
"""

def memory_addressing(page_table, page_size, logical_address):
    #計算頁號和偏移量
    page_number, offset = divmod(logical_address, page_size)
    
    #查找頁表來獲得相應的框架號
    if page_number in page_table:
        frame_number = page_table[page_number]
        #計算物理位置
        physical_address = frame_number*page_size+offset
        print(f"The physical address is{physical_address}")
    else:
        print("Invalid page number,address translation failed")

#定義頁號，其中鍵是頁號
#將程式碼改為使用者輸入 Page Tabel
page_table = {}
while True:
    page_number = input("請輸入page number(或輸入END結束）:")
    if page_number.upper() == 'END' :
        break
    frame_number = int(input(f"請輸入{page_number}對應的frame number:"))
    page_table[int(page_number)] = frame_number
    

#定義頁大小（例如：4096字節）
page_size = 4096

#定義邏輯位置（例如：7000)
#將程式碼改為使用者輸入 logical address
logical_address = int(input("請輸入logical address:"))

#調用函數進行地址轉換
memory_addressing(page_table, page_size, logical_address)
