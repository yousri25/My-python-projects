from numpy import *
def inconnue(n):
    ch=str(n)
    s=0
    for i in range(len(ch)):
        s=s+int(ch[i])
    return(s)
def saisir():
    n=int(input("donner n"))
    while not(5<n<100):
        n=int(input("donner n"))
    return(n)
n= saisir()
def remplisage(t,n):
    for i in range (n):
        t[i]=int(input("donner un entier"))
t= remplisage(t,n)
for i in range (n):
    print(inconnue(n))

