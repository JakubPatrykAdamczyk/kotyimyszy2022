from random import randint
import matplotlib.pyplot as plt
import math
from mysz import *
from kot import*
from kotek import*
import os

mypath=os.getcwd()
mypath+="\msroczynska\yfinal"
klk=[]
f=open(mypath+"\mysz.txt")
klk=f.read()
klk=klk.split(" ")
pmx=int(klk[0])   #pobrać zpliku potem
pmy=int(klk[1])
f.close()

f=open(mypath+"\kot1.txt")
klk=f.read()
klk=klk.split(" ")
pk1x=int(klk[0])   #pobrać zpliku potem
pk1y=int(klk[1])
f.close()

f=open(mypath+"\kot2.txt")
klk=f.read()
klk=klk.split(" ")
pk2x=int(klk[0])   #pobrać zpliku potem
pk2y=int(klk[1])
f.close()

f=open(mypath+"\kot3.txt")
klk=f.read()
klk=klk.split(" ")
pk3x=int(klk[0])   #pobrać zpliku potem
pk3y=int(klk[1])
f.close()






n=0
m1=mysz(pmx,pmy)
k1=kot(pk1x,pk1y)
kl1=kot(pk2x,pk2y)
km1=kotek(pk3x,pk3y)

for x in range(100):
    m1.myszruch()
    
    k1.kotruch()
    kl1.kotruch()
    km1.kotruch()

    if pow(k1.x-m1.x,2)<16 and pow(k1.y-m1.y,2)<16:
        m1.meat(pmx,pmy)
    elif pow(kl1.x-m1.x,2)<16 and pow(kl1.y-m1.y,2)<16 and 1== randint(1,1+math.exp(-0.1*n)):
        m1.meat(pmx,pmy)
        print(n)
        n+=1
    elif pow(km1.x-m1.x,2)<16 and pow(km1.y-m1.y,2)<16 and (km1.x-pk1x)*(km1.y-pk1y)<50*50:
        m1.meat(pmx,pmy)
    else:m1.zapisz()
    if pow(km1.x-m1.x,2)<16 and pow(km1.y-m1.y,2)<16 and km1.x*km1.y>50*50:
        km1.meat(pk3x,pk3y)
        print("fear")
    else:km1.zapisz()


    
# print(m1.mx)
# print(m1.my)

plt.plot(k1.mx,k1.my)
plt.plot(kl1.mx,kl1.my)
plt.plot(km1.mx,km1.my)
plt.plot(m1.mx,m1.my)
plt.show()




