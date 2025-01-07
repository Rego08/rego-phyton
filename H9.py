# # 24.10.24 Rego Märk
# # Ülesanded 9 
import random

# Kuna tsüklid on oluline osa programmeerimisel, siis on oluline mõista selle kasutamist. Seepärast leiad natuke pikema nimekirja ülesannetega.

# # Genereeri ja kuva arvud arvud 1-20
# for i in range(0,20):
#     print(i+1, end=" ")

# # Genereeri ja kuva 20 suvalist arvu vahemikus 1-99
# for i in range(1,21):
#     print(random.randint(1,100), end=" ")
# print()

# # Kasuta loendit 60, 5, 4, 42, 99, 67, 47, 22, 34, 8, 85, 50, 94, 39, 54, 83, 27, 40, 17, 75
# # Leia paaris ja paaritud arvud ning lisa oma loendisse
# # Kuva paaris ja paritute arvude summad
# loend = [60, 5, 4, 42, 99, 67, 47, 22, 34, 8, 85, 50, 94, 39, 54, 83, 27, 40, 17, 75]
# paaris = []
# paaritu = []
# for i in loend:
#     if i%2==0:
#         paaris.append(i)
#     else:
#         paaritu.append(i)

# print(f"Paaris arvude summa: {sum(paaris)}")
# print(f"Paaritu arvude summa: {sum(paaritu)}")

# # Kuva arvud 1-42
# # Arvud, mis jagunevad 3, lisa tekst TIK (näiteks 3 TIK)
# # Arvud, mis jagunevad 5, lisa tekst TAK (näiteks 5 TAK)
# # Kui jagunevad mõlemaga, siis lisa tekst TIKTAK (näiteks 15 TIKTAK)
# for i in range(1,43):
#     if i%3==0 and i%5==0:
#         print(i,"tiktak", end=" ")
#     elif i%3==0:
#         print(i,"TIK", end=" ")
#     elif i%5==0:
#         print(i,"TAK", end=" ")
#     else:
#         print(i, end=" ")
# print()

# # Leia kõik arvud vahemikus 200 kuni 320, mis jaguvad 7-ga, kuid ei jagu 5-ga. Prindi need arvud komadega eraldatult ühele reale.

# for i in range(200,321):
#     if i%7==0 and i%5>0:
#         print(i, end=",")






# # Kuva nimekirjast unikaalsed nimed:
# nimed = ['Martin', 'Tõnu', 'Andres', 'Tõnu', 'Andres', 'Andres', 'Andres', 'Tõnu', 'Marko', 'Mari', 'Jüri', 'Liis', 'Marko', 'Piret', 'Anu']
# unikaalsed_nimed = []
# for nimi in nimed:
#     if nimi not in unikaalsed_nimed:
#         unikaalsed_nimed.append(nimi)

# for nimi in unikaalsed_nimed:
#     print(nimi)




# # Sulle on saadetud õpilaste keskmised hinded, mille lisasid loendisse. Eralda hinded ning leia kogu rühma parim ja kehvem tulemus ning keskmine hinne.
# ryhma_hinded = ["Mari 4.9", "Jüri 3.1", "Kadri 4.6", "Marko 4.7", "Liis 4.9", "Andres 4.2", "Anu 4.7", "Martin 4.2", "Piret 4.2", "Tõnu 4.1"]
# hinded = []

# for i in ryhma_hinded:
#     hinded.append(float(i.split(" ")[1]))

# print(f"Parim tulemus {max(hinded)}")
# print(f"Halvim tulemus {min(hinded)}")
# print(f"Keskmine tulemus {sum(hinded)/len(hinded)}")

# # Koosta programm, mis genereerib ja kuvab korrutustabeli, kus iga number korrutatakse iseendaga:
# # Näiteks:
# # 0 x 0 = 0
# # 1 x 1 = 1
# # 2 x 2 = 4

# for i in range(11):
#     print(f"{i} x {i} = {i*1}")

# # Loo programm, mis loob suvalised tehted 1-100 arvudega.

# # Kasuta tsükli puhul alakriipsu
# # kasuta suvalise tehte märgi jaoks loendit ja sealt suvalise märgi leidmiseks random.choice()
# # Näiteks:
# # 7 – 2=
# # 45 * 69=

# kysimustearv= 5
# punktid = 0
# tehted = ['+','-','*','/']
# for i in range(kysimustearv+1):
#     i = random.randint(1,10)
#     j = random.randint(1,10)
#     tehe = random.choice(tehted)
#     if tehe=="+":
#         print(f"{i} {tehe} {j} = ")
#         vastus = int(input("Vastus: "))
#         if vastus==i+j:
#             print("Õige")
#             punktid+=1
#         else:
#             print("Vale vastus")
#     elif tehe=="-":
#         print(f"{i} {tehe} {j} = ")
#         vastus = int(input("Vastus: "))
#         if vastus==i-j:
#             print("Õige")
#             punktid+=1
#         else:
#             print("Vale vastus")
#     elif tehe=="*":
#         print(f"{i} {tehe} {j} = ")
#         vastus = int(input("Vastus: "))
#         if vastus==i*j:
#             print("Õige")
#             punktid+=1
#         else:
#             print("Vale vastus")
#     else:
#         print(f"{i} {tehe} {j} = ")
#         vastus = float(input("Vastus: "))
#         if vastus=={round(i/j,2)}:
#             print("Õige")
#             punktid+=1
#         else:
#             print("Vale vastus")

# # Täienda eelmist ülesannet ja kasutaja käest küsitakse vastust.
# # Õiged vastused loetakse kokku
# # # Kui saab vähemalt poole punktid, siis saab A, muul juhul MA
# try:
#     if kysimustearv/punktid >= 0.5:
#         print(punktid, "A")
#     else:
#         print(punktid, "MA")
# except:
#     print("MA")


# Kuva samasugused kujundid:

# for i in range(1,6):
#     print("*"*i,end =" ")
#     print()
        
# for i in range(1,6):
#     print("*"*(6-i),end =" ")
#     print()

# for i in range(1,6):
#     print(" "*(6-i)+"*"*i,end =" ")
#     print()

# for i in range(1,6):
#     print(" "*i+"*"*(6-i),end =" ")
#     print()

# Paariarvude summa

# even_nums = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 3, 32, 34, 36, 38]
# # Kirjuta programm, mis summeerib paarisarve listis even_nums kuni esimese paaritu arvuni.
# # Katkesta tsükkel, kui leitakse paaritu arv, kasutades break.
# # Kui tsükkel lõpetab ilma paaritut arvu kohtamata, prindi sõnum “Tsükkel jõudis lõpuni” ja näita paarisarvude summat.
# sum_even = 0
# for i in even_nums:
#     if i%2 == 0:
#         sum_even+=i
#     else:
#         break
# print("Tsükkel jõudis lõpuni", sum_even)


# Mitmemõõtmelise massiivi kasutamine for-tsükliga
# Tutvu elektriautode nimekirjaga, mis sisaldab 10 elektriauto mudelit, nende läbisõidu ulatust ja hinda. Mõista, kuidas andmed on struktureeritud.

# ev_data = [
# ['vehicle', 'range', 'price'],
# ['Tesla Model Y Long Range', '330', '58990'],
# ['Volkswagen ID.4 Pro', '260', '39995'],
# ['Ford Mustang Mach-E', '300', '42995'],
# ['Audi e-tron GT', '238', '102700'],
# ['Nissan Leaf', '149', '27400'],
# ['BMW iX xDrive50', '324', '83995'],
# ['Polestar 2', '265', '45500'],
# ['Kia EV6 Long Range', '310', '47795'],
# ['Mercedes-Benz EQS 450+', '350', '102310'],
# ['Hyundai Kona Electric', '258', '37400']
# ]

# keskmineOdo= []
# keskmineHind= []

# for i in ev_data:
#     if i[0] != "vehicle":
#         keskmineOdo.append(int(i[1]))
#         keskmineHind.append(int(i[2]))
#         #print(i[1])
#     if i[0] != "vehicle" and int(i[1]) > 300:
#         print(i[0])

# print(sum(keskmineOdo)/len(keskmineOdo))
# print(sum(keskmineHind)/len(keskmineHind))
