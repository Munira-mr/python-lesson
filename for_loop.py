# -*- coding: utf-8 -*-
"""
Created on Sat Aug  7 16:05:02 2021

@author: Nodir
"""

ismlar=["Nodirjon","Munira","Yusuf","Ali","Vali"]
for ism in ismlar:
    print(f"{ism} sizni xurmat qilamiz")
print("Kod 5 marta takrorlandi") 

toq_sonlar=list(range(11,100,2)) 
for toq_son in toq_sonlar:
    print(f"{toq_son} ning kubi",(toq_son**3)," ga teng")
    
#kinolar=[]
#print("Eng sevimli kinolaringiz qaysilar?")
#for kino in range(1,6):
 #   kinolar.append(input(f"{kino} Eng yaxshi kurgan kinoni kiriting:\n>>>"))
#print(kinolar)

n_people=int(input("Bugun nechta odam bn suhbatlashdingiz?"))
odamlar=[]

for n in range(n_people):
    odamlar.append(input(f"{n+1}uchrashgan odamiz ismi:\n>>>"))
print(odamlar)

     