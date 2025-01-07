#Rego Märk
#harjutus 12

# kytus = lambda kytusekulu, kaugus: (kytusekulu / 100) * kaugus
# print(kytus(5, 150))


# def temp(t, yhik):
#     """
#     Teisenda temperatuuri Celsiusest Fahrenheitiks ja vastupidi.
 
#     Parameetrid:
#     t (int): Temperatuur.
#     yhik (String): "C" või "F".
 
#     Tagastab:
#     int: temperatuuri.
 
#     Näide:
#     >>> temp(0, "C")
#     32
#     >>> temp(0, "F")
#     -17.78
#     """
#     if yhik=="C":
#         v = t * 5/9+32
#     else:
#         v = (t-32) * 5/9
 
#     return round(v,2)

# print(temp.__doc__)
# print(temp(0,"F"))

konto = 10

def konto_haldur(algne_saldo, toiming, summa):
    global konto
    if toiming == "deposiit":
        v = algne_saldo+summa
        konto = v
    else:
        v = summa - algne_saldo
        konto = v
    return v





print(konto_haldur(20, "deposiit", konto))
print(konto_haldur(10, "deposiit", konto))
print(konto_haldur(20, "väljavõte", konto))