def saisir():
    n = int(input("donner un nombre: "))
    while not(n > 0):
        n = int(input("redonner un nombre: "))
    return n

def compress(n):
    ch = str(n)
    if len(ch) == 0:  # Handle empty string case
        return ""
    
    currentnum = ch[0]
    nb = 1
    ch1 = ""
    i = 1
    
    while i < len(ch):
        if ch[i] == currentnum:
            nb += 1
        else:
            if nb > 1:
                ch1 += str(nb) + currentnum
            else:
                ch1 += currentnum
            currentnum = ch[i]
            nb = 1
        i += 1
    
    # Add the last character(s)
    if nb > 1:
        ch1 += str(nb) + currentnum
    else:
        ch1 += currentnum
    
    return ch1

# Le Programme Principal
n = saisir()
print(compress(n))