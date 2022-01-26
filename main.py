import math
x=int(input("ievadi kvadrata malas garumu, kas ir lielaka par 5cm: "))
kvadrataS=math.pow(x,2)
y=x+5
kvadrata2S=math.pow(y,2)
z=(kvadrata2S-kvadrataS)/kvadrataS*100
print(round(z),"%")
