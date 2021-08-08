# -*- coding: utf-8 -*-
"""
Created on Sat Aug  7 17:03:07 2021

@author: Nodir
"""

cars=["toyota","mazda","gm","kia","hyundai"]
for car in cars:
    #if car=='gm':
     #  print(car.upper())
    # else:
     #  print(car.title())
     if car!='gm':
         print(car.title())
     else:
         print(car.upper())
         
# =============================================================================
# foydalanuvchi_ismi=input("Loginni kirgizing:\n>>>")
# if foydalanuvchi_ismi=='Admin':
#     print("Xush kelibsiz,Admin! Ro'yxatni ko'rasizmi?")
# else:
#     print(f"Xush kelibsiz {foydalanuvchi_ismi}")
# =============================================================================

# =============================================================================
# birinchi_son=float(input("1-sonni kiriting\n>>>"))
# ikkinchi_son= float(input("2-sonni kiriting\n>>>"))
# if birinchi_son==ikkinchi_son:
#     print("Sonlar teng")
# =============================================================================
son=int(input("Istalgan sonni kiriting\n>>>"))
# =============================================================================
# if son>0:
#    print("Son musbat")
# else:
#    print("Son manfiy")     
# =============================================================================
print(son**(1/2)) if son>0 else print("Musbat son kirgizing!")