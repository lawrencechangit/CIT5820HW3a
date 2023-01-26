import random

from params import p
from params import g

q=(p-1)/2

def keygen():
    sk = random.randint(1,p)
    pk = pow(g,sk,p)

    return pk,sk

def encrypt(pk,m):
    #print("pk is ",pk)
    r=random.randint(1,q)
    c1 = pow(g,r,p)
    print("c1 is ", c1)
    firstpart=pow(pk,r,p)
    secondpart=m%p
    c2=(firstpart*secondpart)%p
    print("c2 is ",c2)
    return [c1,c2]

def decrypt(sk,c):
    c1=c[0]
    c2=c[1]
    firstpart=c2%p
    secondpart=(c1**-sk)%p
    m = (firstpart*secondpart)%p
    print("Message is ",m)
    return m


