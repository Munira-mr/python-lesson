# -*- coding: utf-8 -*-
"""
Created on Fri Aug  6 17:08:54 2021

@author: Nodir
"""

davlatlar=["Amerika","Germaniya","Japan","China","Korea"]
#print(davlatlar)
#print(len(davlatlar))
#print(sorted(davlatlar))
#print(sorted(davlatlar, reverse=True))
#print(davlatlar)
#davlatlar.reverse()
print(davlatlar)

davlatlar.sort()
print(davlatlar)
davlatlar.sort(reverse=True)
print(davlatlar)

sonlar=list(range(120,1200))
print(sum(sonlar))
print(max(sonlar)-min(sonlar))
print(len(sonlar))
print(sonlar[:20])
print(sonlar[-20:])
print(sonlar[530:550])

taomlar=["shourma","lagmon","shashlik","pizza","osh"]
print(taomlar)
nonushta=taomlar[:]
print(nonushta)
nonushta.remove("shourma")
nonushta.remove("lagmon")
nonushta.remove("shashlik")
nonushta.append("qaymoq")
nonushta.append("non")
print(nonushta)
print(taomlar)
nonushta=tuple(nonushta)
nonushta[0]="choy"