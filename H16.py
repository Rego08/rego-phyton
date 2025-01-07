# Rego Märk
# 20.11.2024
# Ülesanne 16

import os
import datetime

# OS kasutajanimi
print(os.getlogin())

# aktiivne kataloog
print(os.getcwd())

#Kataloogide loomine:
# Skript küsib kasutajalt, mitu kataloogi ta soovib luua
# Kataloogid luuakse praegusesse töökataloogi kuupäevaga märgistatud kataloogi sees, nummerdatuna (nt “1”, “2”)

try:
    mitu = 3
    x = datetime.datetime.now()
    for i in range(mitu):
        y = x.strftime("%d%m%Y")
        os.mkdir(str(y)+"_"+str(i+1))
except:
    print("Kataloogid juba olemas!")

valik = input("Lisa kataloogi nimi kustutamiseks: ")
try:
    os.rmdir(valik)
except:
    print("Sellist kataloogi ei saa kustutada")

items = os.listdir()
for item in items:
    if os.path.isdir(item):
        print(item)