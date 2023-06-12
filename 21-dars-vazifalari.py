# -*- coding: utf-8 -*-
"""
Created on Mon Jun 12 11:45:40 2023

@author: User
"""

# 1-vazifa

#def KattaHarf(matnlar):
#    """Matndagi har bir so`zni bosh harfini katta qilib beradigan funksiya"""
#    for i in range(len(matnlar)):
#        matnlar[i]=matnlar[i].title()#

#ismlar=['mansur','nosir','holiq','jalil']
#KattaHarf(ismlar)
#print(ismlar)    


# 2-vazifa

def KattHarf(matnlar):
    matnlar=matnlar[:]
    for i in range(len(matnlar)):
        matnlar[i]=matnlar[i].title()
        
ismlar = ['mardon', 'gani', 'toshmat', 'eshmat']
yangi_ismlar = KattHarf(ismlar)
print(ismlar)
print(yangi_ismlar)
        
        
