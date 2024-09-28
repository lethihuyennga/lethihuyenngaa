# -*- coding: utf-8 -*-
"""
Created on Wed Sep 18 00:50:00 2024

@author: PC
"""

N = int(input("Nhập một số nguyên dương N:"))
while N <= 0:
    N = int(input("N không phải là số nguyên dương. Vui lòng nhập lại:"))
print(f"Các ước sô của {N} là:")
for i in range(1,N+1):
    if N % i == 0:
        print(i)