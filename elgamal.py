import random

from params import p
from params import g

q=(p-1)/2

def keygen():
    sk = random.randint(1,p)
    pk = pow(g,sk,p)

    return pk,sk

def encrypt(pk,m):
    r=random.randint(1,q)
    c1 = pow(g,r,p)
    interim=pk*m
    c2 = interim%p

    return [c1,c2]

def decrypt(sk,c):
    c1=c[0]
    c2=c[1]

    interim=c2/pow(c1,sk)
    m = pow(interim,1,p)

    return m

