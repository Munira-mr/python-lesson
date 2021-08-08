# -*- coding: utf-8 -*-
"""
Created on Sat Aug  7 18:11:23 2021

@author: Nodir
"""

# =============================================================================
# =============================================================================
# yosh= int(input("Yoshingizni kiriting\n>>>"))
# if yosh <= 4 or yosh >=60:
#      print("Siz uchun muzey bepul")
# elif yosh <=18:
#      print("Muzey narxi 10 ming")
# elif yosh > 18:
#      print("Muzey narxi 20 ming")
# =============================================================================
# =============================================================================
# son1 = int(input("Istagan 1-sonni kiriting\n>>>"))
# son2 = int(input("Istagan 2-sonni kiriting\n>>>"))
# if son1==son2:
#     print("Sonlar teng.")
# elif son1 > son2:
#     print(f"{son1} katta {son2} dan!")
# else:
#     print(f"{son1} kichik {son2} dan!")
#     
# =============================================================================
# # =============================================================================
# mahsulotlar=["un","non","choy","olma","sabzi","qand","ip","osh","nok","til"]
# savat=[]
# for n in range(5):
#     savat.append(input(f"Savatga {n+1} mahsulot nomini kiriting\n>>>"))
# =============================================================================

# =============================================================================
# for mahsulot in savat:
#     if mahsulot in mahsulotlar:
#         print(f"{mahsulot} do'konimizda bor")
#     else:
#         print(f"{mahsulot} do'konimizda yo'q")
# =============================================================================
# # =============================================================================
# bor_ruyhatlar=[]
# mavjud_emas=[]
# for mahsulot in savat:
#     if mahsulot in mahsulotlar:
#         bor_ruyhatlar.append(mahsulot)
#     else:
#         mavjud_emas.append(mahsulot)
# if mavjud_emas:
#     print("Do'konimizda quyidagi mahsulotlar yo'q:")
#     for mahsulot in mavjud_emas:
#         print(mahsulot)
# else:
#      print("Do'konimizda xamma mahsulotlar bor!")       
# =============================================================================
# # =============================================================================
# foydalanuvchilar=["Anvar","Yusuf","Munira","Nodirjon","Ali"]
# foydalanuvchi=input("Login kirgizing:\n>>>")
# if foydalanuvchi.title() in foydalanuvchilar:
#     print("Login band yangi login tanlang!")
#     
# else:
#     print(f"Xush kelibsiz, {foydalanuvchi.title()}!")
# =============================================================================
son = int(input("Istalgan butun son kirgizing"))
for i in range(2, 11):
    if son % i== 0:
        print(f"{son} soni {i} ga qoldiqsiz bo'linadi")
    