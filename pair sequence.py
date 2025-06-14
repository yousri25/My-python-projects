from numpy import *
# les fonnction
def saisir():
    n=int(input("donner la taille du tableau"))
    while not(3<=n<=15):
        n=int(input("donner Une taille du tableau valide"))
    return n
def remplir(t,n):
    for i in range(n):
        t[i]=int(input("donner un nombre"))
def sequence(t2,t,n):
    a=0
    for i in range(n-1):
        if((t[i]%2==0)):
                t2[i]=t[i]
                a+=1
        else:
            t2[i]=0
    print(t2)
    print("totale sequence est",a)
def reset(t,n):
    for i in range(n):
        if(t[i]!=0):
            t[i]=0
# Le Programme Princlipal
print("code done by yousri")
n=saisir()
t=array([int()]*n)
t2=array([int()]*n)
remplir(t,n)
sequence(t2,t,n)

