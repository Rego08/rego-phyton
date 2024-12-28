#18.10.2024 Rego Märk
# Ülesanne 6
import turtle
import math

# Matemaatika
korgus = 4.4
nurk = math.radians(53)
kaugus = abs(korgus / math.tan(nurk))
c = math.sqrt((korgus**2)+ (kaugus**2))
print(kaugus, c)
#Joonis
kordaja = 10
turtle.fd(kaugus*kordaja)
turtle.lt(90)
turtle.fd(korgus*kordaja)
turtle.lt(180-37)
turtle.fd(c*kordaja)








turtle.done