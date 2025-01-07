import turtle

# 6.10.2024 Rego Märk
# Ülesanded 4

#Ringi pindala ja Turtle

try:
    r = int(input("Sisesta ringi raadius: "))
    s = 3.14*r**2
    p = 2*3.14*r
    print(f"Ringi pindala on {s:.2f} ja ümbermõõt on {p:.2f}")
    turtle.circle(r*2, 360)
    turtle.done()
except:
    print("Sisestus vale!")

#Kingituste pakkimine

try:
    kast = 5
    kingitusteArv = int(input("Lisa kingituste arv: "))
    komplektid = kingitusteArv//kast #täisarvu saamine
    yle = kingitusteArv%kast # jäägi saamine
    print(f"Saad teha {komplektid} täis kinkekasti. Üle jääb {yle} kingitust.")
except:
    print("Lisasid koguse valesti")

#Faili allalaadimine

try:
    failiSuurus = int(input("Sisesta faili suurus: "))
    kiirus = int(input("Sisesta allalaadimise kiirus: "))
    aeg = failiSuurus/kiirus
    print(f"Allalaadimiseks kulub {aeg} sekundit")
except:
    print("Sa ei sisestanud täisarvu!")

#Raamatute allahindlus

ale = 0.3
hind = 12.3
kogus = int(input("Lisa raamatute kogus: "))
summa = (hind-(hind*ale)) * kogus
print(f"{kogus} raamatur hind soodustusega on {summa:0.2f}€.")

# Aia pikkus

a = int(input("Lisa 1 külg: "))
b = int(input("Lisa 2 külg: "))
P = 2*(a+b)
print(f"Aia kogupikkus on {P} meetrit.")
