# -*- coding: utf-8 -*-
"""
Created on Sat Sep 21 14:59:24 2024

@author: PC
"""

km = float(input("nhập số km đi được: "))
tien = 0
if km==1:
    tien = 15000
    print("số tiền:", tien)
elif 2<=km<=5:
    tien = 15000 + (km-1)*13500
    print("số tiền:", tien)
elif km>=6:
    tien = 15000 + 4*13500 + (km-5)*11000
    print("số tiền:", tien)
if km>120:
    tien = (15000+ 4*13500 + (km-5)*11000)*0.9
    print("số tiền được giảm 10% là:", tien)