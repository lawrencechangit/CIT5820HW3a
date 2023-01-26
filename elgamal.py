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
    firstpart=pow(pk,r,p)
    secondpart=m%p
    c2=(firstpart*secondpart)%p
    return [c1,c2]

def decrypt(sk,c):
    c1=c[0]
    c2=c[1]
    firstpart=pow(c2,1,p)
    secondpart=pow(c1,-sk,p)
    m = pow(firstpart*secondpart,1,p)
    return m


