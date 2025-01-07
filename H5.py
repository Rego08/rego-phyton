#18.10.2024 Rego Märk
# Ülesanded 5
import random
import turtle


# 4. Mündiviskaminse äraarvamine koos juhuslikkusega
# kull = 1
# kiri = 0
mynt = random.randint(0,1)
arva = (input("Vali kull või kiri: "))
if (mynt == 0 and arva == "kiri") or (mynt == 1 and arva == "kull"):
    vastus = "green"
else:
    vastus = "red"
print(mynt)
turtle.color(vastus)
turtle.circle(100)
turtle.done

# 3. Vanusepiiranguga üritus

vanus = int(input("Lisa vanus: "))
if vanus >= 18:
    print("Saab sisse!")
else:
    print("Liiga noor!")


# 2. Matemaatika test

a = random.randint(1,10)
b = random.randint(1,10)
vastus = int(input(str(a)+"*"+str(b)+"="))
if a*b ==vastus:
    print("Tubli")
else:
    print ("Vale")


# 1. Ilmaennustuse rakendus

try:
    c = int(input("Lisa kraadid: "))
    if c < 0: 
        print("Kanna talveriideid")
    elif c >= 0 and c <= 15:
        print("Kanna kevad-sügis riideid")
    else:
        print("Kanna suveriideid")
except:
    print("Pane täisarv!")