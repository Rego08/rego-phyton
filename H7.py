# 22.10.2024 Rego Märk
# Ülesanne 7 Massiivid


# Aastaajad
kuud = [('jaanuar',-6,-2,-9,-2,-2,-16,10,7,10,7,-6,2,-7,-16,3,-20,7,-5,3,9,-2,-1,-2,-3,-16,10,-2,2,6,-7,-3),
('veebruar',-12,-15,-15,-8,-2,-11,-17,-15,-12,4,-5,3,-1,-12,-7,-12,-20,-3,-15,-3,2,-15,4,-1,-16,-11,-9,8),
('märts',10,-6,-17,-14,-10,-8,-3,-1,6,0,6,6,-5,0,4,6,-6,-6,-14,-12,-15,-6,-19,-2,-10,-19,-3,-1,-8,-10,-19),
('aprill',-1,1,-18,-5,1,-8,3,-17,-14,2,-6,7,-20,-12,3,-10,8,0,-13,-2,6,-19,-1,7,9,-18,-9,7,-10,6),
('mai',4,-19,-3,-9,10,-11,10,-15,-4,0,-3,-11,7,6,-18,-1,-3,-1,0,-13,10,1,-20,-13,-1,8,-16,9,-7,-14,-8),
('juuni',-1,10,-12,-10,6,4,5,-18,-9,-11,2,3,-10,-4,-16,7,0,3,10,2,-12,6,0,7,-10,-12,-17,0,-3,10),
('juuli',-11,-14,-18,10,0,-17,-6,-16,-18,1,-9,-1,-7,3,-18,-17,-18,-19,-9,2,-16,-4,-12,8,3,6,-19,4,-17,-8,-8),
('august',-18,-2,-2,10,7,-2,-18,-9,-9,-2,-6,3,-3,-2,-4,-10,5,-5,-7,-10,-20,-10,-8,0,-10,0,-15,-10,10,7,-6),
('september',7,-9,-6,-13,-15,5,-11,-8,-17,7,-10,-13,-4,-1,-7,-18,-13,-4,4,-1,-13,-19,5,-1,-15,-2,-12,-6,-12,3),
('oktoober',-5,-6,6,6,5,7,-2,-13,-15,2,-11,2,-6,3,-6,0,-16,-17,-6,-14,0,-1,9,5,-4,-7,6,-1,-1,3,3),
('november',-14,-5,-11,-3,10,-10,-4,-12,-17,5,7,1,-9,-2,10,-9,5,-1,-20,-15,-19,-19,8,10,-9,-9,-17,1,-13,-3),
('detsember',3,-20,-4,-4,-17,-7,-5,-20,-18,-5,6,-11,-20,-19,-7,-18,7,-11,10,0,-19,-3,2,7,-7,-14,8,1,5,5,-20)]

print(f"Hetkekuu {kuud[9][0]}")
kuus_kokku = len(kuud[9])-1
print(f"Viimane mõõtmine: {kuud[9][kuus_kokku]}")
print("Selle kuu temperatuurid: ")
ajutine = []
for i in range(kuus_kokku):
    ajutine.append(kuud[9][i+1])
    print(kuud[9][i+1], end=", ")
print()
print(f"Max temp: {max(ajutine)}")
print(f"Min temp: {min(ajutine)}")
print(f"Keskmine temp: {round(sum(ajutine)/len(ajutine),2)}")
print(f"-20 esineb {ajutine.count(-20)} korda")
ajutine.pop(5-1)
ajutine.insert(5-1,16)
ajutine.sort()
print(ajutine)

"""
# Muusikapalad
laulud = ['ALIKA – "Bridges"','Anett x Fredi – "Read Between The Lines"','villemdrillem – "leekiv armastus"','Clicherik & Mäx – "PAKSUD"','nublu – "ära ärata"','NOËP – "Move Your Feet"','Trad.Attack! – "Bring It On"','Bedwetters – "It Is What It Is"','Reket – "Panama paberid"','Grete Paia – "Võluväel"']

for i in range(10):
    print(str(i+1)+". "+laulud[i])
try:
    valik = int(input("Vali lugu 1-10: "))
    print(f"Mängin: {laulud[valik-1]}")
except:
    print("Tegid vale otsuse!")
"""