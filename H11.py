# Rego Märk
# 15.11.2024
# Ülesanne 11
import random
import turtle

# Kirjuta funktsioon pikim_sona(), mis võtab sisendiks sõnade listi ja tagastab pikima sõna pikkuse. Prindi tulemus konsooliaknasse.

def pikim_sona(a):
    pikimSona = 0
    for sona in a:
        if len(sona)>pikimSona:
            pikimSona = len(sona)
    print(pikimSona)

sonad = ["üks", "kaks", "kolm", "kuusteist", "sadakuuskümmend"]

pikim_sona(sonad)

#  Kirjuta funktsioon nimega kolm_pikimat_sona(), mis analüüsib sõnade listi ja leiab kolm kõige pikemat sõna. Lisa kontroll juhuks, kui sõnade arv pole piisav.

def kolm_pikimat_sona(a):
    uusSonastik = {}
    for sona in a:
        uusSonastik[sona] = len(sona)
    jar =sorted(uusSonastik.items(), key=lambda x:x[1], reverse=True)
    if len(a)<3:
        print("Sõnade arv pole piisav")
    else:
        for i in range(3):
            print(jar[i][0])


kolm_pikimat_sona(sonad)

# Kirjuta funktsioon, mis kontrollib, kas kahest sõnast koosnev sõne algab sama tähega.
# print(sarnased_esitahed('Vapper Vares')) # peaks tagastama True
# print(sarnased_esitahed('Lahe Känguru')) # peaks tagastama False

def sarnased_esitahed(a):
    tykk = a.split(" ")
    if (tykk[0][0]).lower()== (tykk[1][0]).lower():
        return "True"
    else:
        return "False"

print(sarnased_esitahed('Vapper Vares'))
print(sarnased_esitahed('Lahe Känguru'))

# Kilpkonn – kirjutada programm, mis lubab kasutajal valida kujundite tüübi (viisnurk, ring, ruut või suvaline) ja arvu. Programm joonistab seejärel antud arvu kujundeid valitud tüübiga või juhul, kui valik on “suvaline”, valib programm ise juhuslikult kujundi tüübi iga kujundi jaoks.
# Millist kujundit soovid joonistada (1 viisnurk, 2 ring, 3 ruut, 4 suvaline)? Suvaline
# Mitu kujundit soovid joonistada? 5
# [Joonistab 5 kujundit, igaüks juhuslikult valitud tüübiga suvalistesse kohtadesse]
# Pärast joonistamist peaks programm pakkuma võimalust sisestada uued väärtused või väljuda programmist, jättes sisendi tühjaks.

print("-------------Joonistame Kujundid-------------")
print("Vali kujund: \n1 viisnurk, \n2 ring, \n3 ruut, \n4 suvaline")
kujund = (int(input("Siseta number: ")))
arv = (int(input("Mitu kujundit tahad (1-100): ")))

def viisnurk(a):
    for j in range(a):
        turtle.speed(0)
        turtle.penup()
        turtle.goto(random.randint(-400,400), random.randint(-400,400))
        turtle.pendown()
        turtle.lt(random.randint(0,90))
        for i in range(5):
            turtle.fd(100)
            turtle.lt(144)

def ring(a):
    for j in range(a):
        turtle.speed(0)
        turtle.penup()
        turtle.goto(random.randint(-300,300), random.randint(-300,300))
        turtle.pendown()
        turtle.circle(100)

def ruut(a):
    for j in range(a):
        turtle.speed(0)
        turtle.penup()
        turtle.goto(random.randint(-400,400), random.randint(-400,400))
        turtle.pendown()
        turtle.lt(random.randint(0,90))
        for i in range(4):
            turtle.fd(100)
            turtle.lt(90)


def suvaline(a):
    for i in range(a):
        my_list = [viisnurk, ring, ruut]
        random.choice(my_list)(1)

if kujund == 1:
    viisnurk(arv)
elif kujund == 2:
    ring(arv)
elif kujund == 3:
    ruut(arv)
else:
    suvaline(arv)

turtle.done()