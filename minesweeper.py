from numpy import *
from random import *

def saisir():
    n=int(input("give the side number of the square(the map)"))
    while n<=0:
        n=int(input("Please give a valid number"))
    return n

def remplir(t2,t,n):
    for i in range(n):
        for j in range(n):
            t[i,j]=str(randint(0,9))
            t2[i,j]="."

def mine(t,n,b):
    for i in range(b):
        t[randint(0,n-1),randint(0,n-1)]="x"

def search(t2,t,n,b):
    a = 0
    c = 0
    for i in range(n):
        for j in range(n):
            if t[i,j] == "x" and t2[i,j] == ".":
                a += 1
            if t[i,j] != "x" and t2[i,j] == ".":
                c += 1
    return a == b and c == 0

def game(t2,t,n,b):
    test=True	
    while(test):
        print(t)
        print(t2)
        try:
            x=int(input("enter your guess's row"))
            y=int(input("give your guess's coll"))
            while(x<0 or x>n-1 or y<0 or y>n-1):
                x=int(input("enter a valid row"))
                y=int(input("enter a valid coll"))
            if(t2[x,y] != "."): 
                print("you already choose this one")
                continue
            if(t[x,y]=="x"):
                test=False
                print("BOOOOM!! You Lost")
                for i in range(n):
                    for j in range(n):
                        if t[i,j]=="x":
                            t2[i,j]="X" 
                print(t2)
            else:
                print("safe you can guess again")
                t2[x,y]=t[x,y] 	
                print(t2)
                if search(t2,t,n,b):
                    print("congratulations, You Won")
                    break
        except(ValueError):
            print("that is not a valid input")

print("Welcome to minesweeper!! By Youssri")
n=saisir()
t=array([[str()]*n]*n)
t2=array([[str()]*n]*n)
remplir(t2,t,n)
b=int(input("how many mines do you want"))
while b<=0 or b>=n*n:
    b=int(input("Please give a valid number"))
mine(t,n,b)
game(t2,t,n,b)