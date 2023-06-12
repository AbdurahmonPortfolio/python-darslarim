# -*- coding: utf-8 -*-
"""

22 MOSLASHUVCHAN FUNKSIYA

Uyga vazifalar                                                       12.06.2023

"""
# 1-vazifa

#def multiply(*sonlar):
#    kopaytma=1
#    for son in sonlar:
#        kopaytma *= son
#    return kopaytma

#print(multiply(54,10))


# 2-vazifa

def talaba_info(ism, familiya, **kwargs):
    kwargs['ism']=ism
    kwargs['familiya']=familiya
    return kwargs
talaba = talaba_info('olim','olimov',tyil=1995,fakultet='IT',yonalish='AT')