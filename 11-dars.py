# -*- coding: utf-8 -*-
"""
Created on Sat May 20 10:20:58 2023

@author: User
"""

mahsulotlar = ['un', "yog'", "sovun", 'tuxum', 'piyoz',
               'kartoshka', 'olma', 'banan', 'uzum', 'qovun']
savat=[]
for n in range(5):
    savat.append(input(f"savatga {n+1}-mahsulotni qo'shing:"))
for mahsulot in savat:
    if mahsulot in mahsulotlar:
        print(f"Do'konimizda {mahsulot} bor")
    else:
        print(f"Do'konimizda {mahsulot} yo'q")    