# Rego Märk
# 19.11.2024
# Ülesanne 13

import turtle
 
screen = turtle.Screen()
t = turtle.Turtle()
 
pikkus = screen.numinput("Vanuse sisestamine", "Mis on sinu vanus?", default=20, minval=0, maxval=100)

cm = 10
mm = 3
t.speed(0)
for i in range(int(pikkus)):
    for j in range(10):
        t.fd(mm)
        t.lt(90)
        t.fd(mm)
        t.lt(180)
        t.fd(mm)
        t.lt(90)
    t.lt(90)
    t.fd(cm)
    t.write(i+1, font=("Arial", 8, "normal"))
    t.lt(180)
    t.fd(cm)
    t.lt(90)




# print(f"Sinu vanus on {int(vanus)} aastat")
 
turtle.done()


# Loo Pythoni Turtle-iga programm, mis palub kasutajal sisestada joonlaua pikkuse sentimeetrites kasutades numinput funktsiooni.

# Seejärel joonistab programm ekraanile joonlaua, märkides iga sentimeetri kriipsu ja numbri.
# Iga sentimeetri kriips peaks olema lühem ja iga viie sentimeetri tagant pikem, et eristada erinevaid mõõtmeid selgemalt.
# Numbrid kirjutatakse vastavate pikemate kriipsude juurde, märkides sentimeetrite arvu alates joonlaua algusest.