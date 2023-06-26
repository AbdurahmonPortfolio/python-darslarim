# -*- coding: utf-8 -*-
"""
24 Funksiyalar So'ngSo'z

"""

#sonlar=list(range(11))

#kvadrat=list(map(lambda x:x*x, sonlar))
#print(kvadrat)

#a=[3,5,8]
#b=[5,8,13]
#a_plus_b=list(map(lambda x,y:x+y,a,b))
#print(a_plus_b)


#import random as r
#sonlar=r.sample(range(100), 10)
#print(sonlar)
#def juftmi(x):
#    """x juft bo'lsa True aks holda False qaytaruvchi funksiya"""
#    return x%2==0

#juftsonlar=list(filter(juftmi, sonlar))
#print(juftsonlar)


#juftsonlar=list(filter(lambda x: x%2==0,sonlar))
#print(juftsonlar)


mevalar=['qizilolma','shaftoli','anor','anjir','olma','olcha','uzum','nok']
harf='o'
mevalar_a=list(filter(lambda meva:meva.startswith(harf), mevalar))
#print(mevalar)
#print(mevalar_a)


mevalar_2=list(filter(lambda meva:len(meva)<=5, mevalar))
#print(mevalar_2)


list(filter(lambda meva:(meva.startswith('a')and meva.endswith('r')), mevalar))


