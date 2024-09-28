# -*- coding: utf-8 -*-
"""
Created on Sat Sep 21 13:31:05 2024

@author: PC
"""

n = int(input("nhập n:"))
tong = 0
while n>0:
    tong += n%10
    n = n//10
print("kết quả là:", tong)