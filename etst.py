import time
test=True
i=0
n1=20
while(test):
    if(i<6):
       time.sleep(1)
       i+=1
       name=input("Mr or Mrs ?")
       nb=int(input("give a higher bet !"))
       if(nb>n1):
           i=10
    elif(i==10):
        print("Sold for",nb,"to",name)
        test=False
    else:
        print("time is up !")
        test=False
   