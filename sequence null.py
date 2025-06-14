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
    count = 0
    for i in range(n):
        s = 0
        for j in range(i, n):
            s += t[j]
            t2[j-i] = t[j]
            if s == 0:
                print("Séquence nulle trouvée :",t2[:j-i+1])
                count += 1
                reset(t2,n)
    print("Nombre total de séquences nulles :",count)
    return count
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
