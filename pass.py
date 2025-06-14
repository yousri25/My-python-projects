# Les Fonctions
def penal(ch):
    return (longmaj(ch)*2) +(longmin(ch)*2)
def longmin(ch):
    nb=0
    for i in range(len(ch)-1):
        if(('a'<= ch[i]<='z')and(('a'<= ch[i+1]<='z'))):
            nb+=1
    return nb
def longmaj(ch):
    nb=0
    for i in range(len(ch)-1):
        if(('A'<= ch[i]<='Z')and(('A'<= ch[i+1]<='Z'))):
            nb+=1
    return nb
def nbnalph(ch):
    nb=0
    for i in range(len(ch)):
        if not (('A'<= ch[i]<='Z') or ('a'<=ch[i]<='z')):
            nb+=1
    return nb
def totalmin(ch):
    nb=0
    for i in range(len(ch)):
        if((ch[i]>="a"))and((ch[i]<="z")):
            nb+=1
    return nb
def totalmaj(ch):
    nb=0
    for i in range(len(ch)):
        if((ch[i]>="A"))and((ch[i]<="Z")):
            nb+=1
    return nb
def bonus(ch):
    total=len(ch)
    mj=totalmaj(ch)
    mi=totalmin(ch)
    nb=nbnalph(ch)
    return (total*4)+((total-mj)*2)+((total-mi)*3)+(nb*4)
def score(ch):
    return bonus(pw)-penal(pw)
# Le Programme Principale
pw=input("donner votre mot passe")
print(score(pw))