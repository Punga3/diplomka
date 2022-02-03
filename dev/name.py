import math
import scipy.special
from random import sample

k=int(input("k="))
n=int(input("n="))
m=1#math.floor(math.sqrt(n**k))
p=float(input("p="))

mpr=1


Pm=[]
for i in range(math.factorial(n)):
    P=[]
    R=[j for j in range(n)]
    I=i
    for j in range(n):
        P.append(R[I%(n-j)])
        R.remove(R[I%(n-j)])
        I//=n-j
    Pm.append(P)

uni=[[i//(n**j)%n for j in range(k)] for i in range(n**k)]

for i in range(100):

    T=sample(range(m,len(uni)),int((len(uni)-m)*p))

    print(T)


    succ=0
    for P in Pm:
        Tn=[]
        for i in T:
            En=[P[uni[i][j]] for j in range(k)]
            Tn.append(uni.index(En))
            if uni.index(En)<m:
                succ+=1
                break

    pr=succ/len(Pm)
    if pr<mpr:
        mpr=pr

print(mpr)
