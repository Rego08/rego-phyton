# Rego Märk
# 19.11.2024
# Ülesanne 14

# Loo programm, mis võimaldab kasutajatel hiire abil joonistada kujundeid (vali ise ruut, ring, kolmnurk vms) ekraanile ning muuta joonistusvärvi klaviatuuri abil.
# Kasutajad peaksid saama kasutada hiire vasakut nuppu joonistamiseks ja paremat nuppu joonistatud elementide kustutamiseks.
# Klaviatuuri klahvid ‘R’, ‘G’ ja ‘B’ võimaldavad vastavalt värvi muuta punaseks, roheliseks või siniseks.


import turtle
ekraan = turtle.Screen()

turtle.speed(0)

def ekraanile_klikkimine(x, y):
   turtle.penup()
   turtle.goto(x, y)
   turtle.pendown()
   for i in range(4):
      turtle.fd(50)
      turtle.lt(90)
 
def varv_red():
   turtle.color("red")
def varv_green():
   turtle.color("green")
def varv_blue():
   turtle.color("blue")

def puhasta_ekraan(x,y):
   turtle.clear()

ekraan.onscreenclick(ekraanile_klikkimine, 1)
ekraan.onscreenclick(puhasta_ekraan, 3)
ekraan.onkey(varv_red, "r")
ekraan.onkey(varv_green, "g")
ekraan.onkey(varv_blue, "b")

ekraan.listen()

turtle.mainloop()



