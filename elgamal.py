import random

from params import p
from params import g

q=(p-1)/2

def keygen():
    sk = random.randint(1,p)
    pk = pow(g,sk,p)

    print("pk is ", pk)
    print("sk is ", sk)

    return pk,sk

def encrypt(pk,m):
    #print("pk is ",pk)
    r=random.randint(1,q)
    c1 = pow(g,r,p)
    c2_interim= m*pow(pk,r)
    c2 = pow(c2_interim,1,p)
    print("c2 is ",c2)
    print("c1 is ", c1)
    return [c1,c2]

def decrypt(sk,c):
    c1=c[0]
    c2=c[1]
    denominator=c1^sk
    fraction=c2/denominator
    m = fraction%p
    print("Message is ",m)
    return m

