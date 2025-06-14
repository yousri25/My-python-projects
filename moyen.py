from numpy import*
#Les Fonction
def saisir():
    n=int(input("donner la taille de la classe"))
    while(n<0):
        n=int(input("erreur,donner une taille valide"))
    return n
def saisir2():
    n=int(input("donner la note de la matiere"))
    while(n<0):
        n=int(input("erreur,donner une note valide"))
    return n
def saisirnom():
    ch=input("donner votre nom")
    a=ch.upper()
    for i in range(len(a)):
        while not((a[i]>"A")and(a[i]<"Z")):
            ch=input("erruer,donner un nom valide")
    return ch
def moyenne(a,b):
    return((a+b)//2)
def moyene():
    arc=saisir2()
    ars=saisir2()
    a=moyenne(arc,ars)
    frc=saisir2()
    frs=saisir2()
    b=moyenne(frc,frs)
    infc=saisir2()
    infs=saisir2()
    c=moyenne(infc,infs)
    return((a+b+c)//3)
def remplir(moy,nom,n):
    for i in range(n):
        nom[i]=saisirnom()
        moy[i]=moyene()
def tribulle(moy,nom,n):
    test=False
    while(test==False):
        test=True
        for i in range(n-1):
            if(moy[i]<moy[i+1]):
                aux=moy[i]
                moy[i]=moy[i+1]
                moy[i+1]=aux
                aux2=nom[i]
                nom[i]=nom[i+1]
                nom[i+1]=aux2
                test=False
def verif(moy,v,n):
    for i in range(n):
        if(moy[i]>=10):
            v[i]="ADMIS"
        else:
            v[i]="DOUBLE"
def affichage(moy,nom,v,n):
    for i in range(n):
        print("Les eleves Sont:",nom[i])
    for i in range(n):
        print("Les moyenes Sont:",moy[i])
    for i in range(n):
        print("Les resultats Sont:",v[i])
#Le Programme Principale
n=saisir()
moy=array([int()]*n)
nom=array([str]*n)
v=array([str]*n)
remplir(moy,nom,n)
tribulle(moy,nom,n)
verif(moy,v,n)
affichage(moy,nom,v,n)