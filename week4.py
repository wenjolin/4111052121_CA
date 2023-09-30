#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Sep 30 10:45:19 2023

@author: 0yuan_0124
"""

import sqlite3

#連接到SQlite資料庫（如果不存在，將創建一個新的資料庫文件）
conn = sqlite3.connect('BBQ.db')

#創建一個游標對象，用於執行SQL查詢
cursor = conn.cursor()

#創建名為“meats"的表格
cursor.execute('''
    CREATE TABLE IF NOT EXISTS meats(
        id INTEGER PRIMARY KEY,
        name TEXT,
        price INTEGER,
        quantity INTEGER
        )'''
    )

#插入資料
cursor.execute("INSERT INTO meats (name, price, quantity) VALUES ('chicken', 30, 5)")
cursor.execute("INSERT INTO meats (name, price, quantity) VALUES ('beaf', 55, 10)")
cursor.execute("INSERT INTO meats (name, price, quantity) VALUES ('pork', 40, 15)")

#提交事務
conn.commit()

#查詢資料
cursor.execute("SELECT * FROM meats")
meats = cursor.fetchall()

print("烤肉列表：")
for meat in meats:
    print(meat)
    
#更新資料
cursor.execute("UPDATE meats SET price = 35 WHERE name = 'pork'")
cursor.execute("UPDATE meats SET quantity = 30 WHERE name = 'chicken'")
conn.commit()

#查詢資料
cursor.execute("SELECT * FROM meats")
meats = cursor.fetchall()

print("烤肉列表更動：")
for meat in meats:
    print(meat)

#刪除資料
cursor.execute("DELETE FROM meats WHERE price = 40")
conn.commit()

#查詢資料
cursor.execute("SELECT * FROM meats")
meats = cursor.fetchall()

print("烤肉列表更動：")
for meat in meats:
    print(meat)

#關閉游標和連接
cursor.close()
conn.close()

