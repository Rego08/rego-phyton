# 24.10.2024 Rego Märk
# Ülesanded 8 Sõnastikud

# Tooted
ladu={
'piim': {'kogus': 20, 'hind': 1.19},
'küpsised': {'kogus': 20, 'hind': 4.99},
'või': {'kogus': 20, 'hind': 2.29},
'juust': {'kogus': 15, 'hind': 1.9},
'leib': {'kogus': 15, 'hind': 2.59},
'jogurt': {'kogus': 18, 'hind': 3.65},
'õunad': {'kogus': 35, 'hind': 3.15},
'apelsinid': {'kogus': 40, 'hind': 0.99},
'banaanid': {'kogus': 23, 'hind': 1.29}
}



valik = "piim"
kogus = 10
try:
    if valik in ladu:
        if kogus <= ladu[valik]["kogus"]:
            #kliendi tsekk
            summa = kogus*ladu[valik]["hind"]
            print(f"Toode: {valik}")
            print(f"Hind: {ladu[valik]["hind"]}")
            print(f"Kogus: {kogus}")
            print(f"Summa: {round(summa,2)}€")

            #laoseisu muutmine
            uus_kogus = ladu[valik]["kogus"] - kogus
            ladu[valik]["kogus"] = uus_kogus
        else:
            print("Meil pole sellist kogust")
    else:
        print("Seda toodet ei ole")
except:
    print("Mingi jama")

print(ladu)
#print(ladu['piim'])
#print(ladu['piim']['hind'])

"""
# Telefoninumbrid
telefonid={
'Mari': '5957503',
'Toomas': '5719979',
'Kertu': '5201750',
'Siim': '5580027',
'Piret': '5960799',
'Jaan': '5160415',
'Lea': '5760164',
'Mart': '5337951',
'Anni': '5004818',
'Tõnu': '5721873',
'Kai': '5811884',
'Rasmus': '5859489',
'Eva': '5039393',
'Oskar': '5635812',
'Liina': '5696114',
'Peeter': '5560756',
'Sandra': '5257415',
'Heiki': '5207248',
'Kristi': '5703338',
'Urmas': '5400549'
}
 
print(telefonid["Rasmus"])
telefonid['Arti'] = 58859344
telefonid.pop("Kristi")
telefonid["Eva"] = "55555555"
print(telefonid)

try:
    otsi = input("Lisa nimi: ")
    print(telefonid[otsi])
except:
    print("Otsitavat ei leitud!")
"""