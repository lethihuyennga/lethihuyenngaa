# -*- coding: utf-8 -*-
"""
Created on Fri Sep 20 23:44:46 2024

@author: PC
"""
import math
n = int(input("nhập số nguyên dương:"))
while n<=0:
    n = int(input("nhập lại n"))
can_bac2 = math.sqrt(n)
if n==can_bac2**2:
   print(f"{n} là số chính phương")
else:
    print("không phải số chính phương")