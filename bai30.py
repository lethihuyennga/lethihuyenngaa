# -*- coding: utf-8 -*-
"""
Created on Wed Sep 18 01:41:11 2024

@author: PC
"""
month = 0
year = 0 
month = int(input("Nhập tháng (1-12):"))
while month<1 or month>12:
    month = int(input("tháng không hợp lệ. Vui lòng nhập lại"))
year = int(input("nhập năm:"))

#kiểm tra năm nhuận
nhuan = False
if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
    nhuan = True

# Xác định số ngày trong tháng
if month in [1, 3, 5, 7, 8, 10, 12]:
    days = 31  
elif month in [4, 6, 9, 11]:
    days = 30  
elif month == 2:
    if nhuan:
        days = 29  
    else:
        days = 28  

print(f"Tháng {month} năm {year} có {days} ngày.")
