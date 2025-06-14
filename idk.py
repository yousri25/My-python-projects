from numpy import *
n = int(input("donner un entier entre 2 et 100"))
while not(2 <= n <= 100):
    n = int(input("donner un entier entre 2 et 100"))
t = array([str]*n)
for i in range(n):
    t[i] = input("donner le numero de client")
    while not((t[i].isdecimal() == True) or (len(t[i]) != 8)):
        t[i] = input("repeter le numero")
c = array([int()]*n)
b = array([int()]*n)
for i in range(n):
    c[i] = int(input("donner le consomateur"))
print("le numero des client gagnant sont")
for i in range(n):
    if(c[i] > 150):
        print(t[i])
ch = ""
for i in range(n):
    if(c[i] > 150):
        ch = t[i]
        b[i] = (int(ch[0]) + int(ch[1]) * (c[i] - 150))