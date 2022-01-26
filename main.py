#import math
#x=int(input("ievadi kvadrata malas garumu, kas ir lielaka par 5cm: "))
#kvadrataS=math.pow(x,2)
#y=x+5
#kvadrata2S=math.pow(y,2)
#z=(kvadrata2S-kvadrataS)/kvadrataS*100
#print(round(z),"%")

import math
x=int(input("ievadi riņķa līnijas radiusu: "))
y=int(input("ievadi vienādsānu taisnleņķa trijstūra hipotenūzas garumu: "))
rinkaS=math.pi*math.pow(x,2)
trissturaS=y*(y/2)/2
liel=rinkaS-trissturaS
print("Ŗiņķa laukims ir lielāks par ", round(liel, 1),"cm^3 neka trisstura laukums")

