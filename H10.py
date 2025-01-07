# Ülesanne 10
# Rego Märk
# 8.11.2024
import random


#Ül 2 Mäng

tulemused = []
katsed = 0
loop = 1
arv = random.randint(1,10)
print(arv)
while loop==1:
    katsed+=1
    vastus = int(input("Arva ära 1-10: "))
    if vastus==arv:
        print("Õige")
        print(f"Arvasid {katsed} korda")
        tulemused.append(katsed)
        uuesti = input("Kas soovid veel mängida (j/e): ")
        if uuesti=="j":
            katsed = 0
            arv = random.randint(1,10)
            print(arv)
        else:
            break
    else:
        print("Proovi uuesti")
print("Mäng läbi")
print(tulemused)


# Ül 1
# arvud = []

# loop = 1

# while loop==1:
#     arv = input("Sisesta arv: ")
#     if arv== "":
#         loop = 0
#         break
#     arvud.append(int(arv))

# print(sum(arvud)/len(arvud))