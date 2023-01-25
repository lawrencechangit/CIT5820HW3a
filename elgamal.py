import random

from params import p
from params import g

q=(p-1)/2

def keygen():
    sk = random.randint(1,p)
    pk = pow(g,sk,p)

    #print("Secret key is ",sk)
    #print("Public key is ",pk)

    return pk,sk

def encrypt(pk,m):
    r=random.randint(1,q)
    c1 = pow(g,r,p)
    interim=pk*m
    c2 = interim%p
    #print("C1 is ",c1)
    #print("C2 is ",c2)
    return [c1,c2]

def decrypt(sk,c):
    c1=c[0]
    c2=c[1]
    #print("C1 is " , c1)
    #print("C2 is " , c2)
    interim=c2/pow(c1,sk)
    #print("interim is ",interim)
    m = pow(interim,1,p)
    #print("Message is ",m)
    return m

