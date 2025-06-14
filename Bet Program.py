import time
import threading

# Global variables
sb = 0
timer = True
sec = 6

# Functions
def saisir():
    try:
        n = int(input("Give the starting bet: "))
        if n > 0:
            return n
        else: 
            print("Error, Bet must be Positiv")
    except ValueError:
        print("Invalid input")
def getbet():
    global sb, timer, sec
    while timer:
        try:
            n = int(input("Give a higher bet: "))
            if n > sb:
                sb = n
                sec = 6
                print(f"New bet:",sb,"DT")
            else:
                print("Error: Bet must be higher than", sb)
        except ValueError:
            print("Invalid input")
def timeup():
    global sec, timer
    start = time.time()
    while timer:
        if time.time() - start >= sec:
            timer = False
            print("\n⏰ Time's up! The final bet is", sb, "DT")
        time.sleep(1)  
#Programme Principale
sb = saisir()
print("The bet starts from", sb, "DT")
threading.Thread(target=timeup, daemon=True).start()
getbet()