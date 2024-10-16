import turtle
#Rego Märk
#Ülesanne 4

#Ringi pindala ja Turtle
r=int(input("Sisesta ringi raadius :"))
s=3.14*r**2
p=2*3.14*r
print("Ringi pindala on {s:.2f} ja ümbermõõt on {p:.2f}")
turtle.circle(r*10,360)
turtle.done()
except:
    print("sisestus vale")


#Kiniduste pakkimine
try:
    kast=5
    kingitusteArv=int(input("lisa kingituste arv:"))
    komplektid=kingitusteArv//kast#täisarvu saamine
    yle=kingitusteArv%kast
    print(f"Saad teha {komplektid} täis kinkekasti. üle jääb {yle} kingitust")
except:
    print("Lisasid koguse valesti")




#Faili allalaadimine
try:
    failisuurus=int(input("sisesta failisuurus:"))
    downlKiirus=int(input("Sisesta allalaadimis kiirus"))
    aeg=failisuurus/downlKiirus
    print(f"Allalaadimieks kulub {aeg} sekundit")
except:
    print("Palun sisesta täisarvud")




#Raamatute allahindlus
ale=0.3
hind=12.5
kogus=int(input("Lisa Raamatute kogus:"))
summa=(hind-(hind*ale))*kogus
print(f"{kogus}Raamatu hind soodustusega on {summa:0.2f}€.")






#aia pikkus
a=input("Lisa 1 külg:")
b=input("Lisa 2 külg")
p=2*(a+b)
print(f"aia kogupikkus on {p}meetri.")


