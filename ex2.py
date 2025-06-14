from numpy import *
#Les Fonctions
def saisir2():
    n=int(input("donner votre numero"))
    while not(len(str(n))!=8):
        n=int(input("donner votre numero"))
    return n
def saisir():
    n=int(input("donner la taille du tableau"))
    while not(n>2):
        n=int(input("donner la taille du tableau"))
    return n
def remplir(t,n):
    for i in range(n):
        t[i]=dict()
        t[i]["nom"]=input("donner votre nom")
        t[i]["numero"]=saisir2()
#Le Programme Principale
n=saisir()
t=array([dict()]*n)
remplir(t,n)
affichage(t,n)