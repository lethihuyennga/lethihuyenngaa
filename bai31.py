# -*- coding: utf-8 -*-
"""
Created on Sat Sep 21 14:54:04 2024

@author: PC
"""

a = int(input("nhập canh a: "))
b = int(input("nhập cạnh b: "))
c = int(input("nhập cạnh c: "))
if a+b>=c or a+c>=b or b+c>=a:
    if a==b or b==c or c==a:
        print("tam giác cân")
    elif a==b==c:
        print("tam giác đều")
    elif a**2+b**2==c**2 or a**2+c**2==b**2 or b**2+c**2==a**2:
        print("tam giác vuông")
    else:
        print("tam giác thường")
else:
    print("không phải tam giác")
