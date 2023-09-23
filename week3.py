#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Sep 23 20:00:10 2023

@author: 0yuan_0124
"""

import os
import time

#創建CS目錄
os.mkdir('CS')
#創建homework檔案
file = open('CS/homewoek.txt','w+')
#write
file.write('4111052121_溫翎媛')
#read
content = file.read()
#size
file_size = os.path.getsize('CS/homewoek.txt')
print(f'文件大小：{file_size}字節')
#time
modification_time = os.path.getmtime('CS/homewoek.txt')
formatted_time = time.ctime(modification_time)
print(f'最後修改時間：{formatted_time}')
#delete
os.remove('CS/homewoek.txt')
os.rmdir('CS')

