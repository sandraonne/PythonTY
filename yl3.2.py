print("Sisesta ostjate arv:")
ostjad = int(input())
arv = 1
summa = 0
while arv <= ostjad:
    summa = summa + arv
    arv += 2
print("Lillede koguarv on " + str(summa) + ".")
    