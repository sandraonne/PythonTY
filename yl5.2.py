ostjad = int(input("Sisesta ostjate arv:"))
summa = 0
for i in range (1, ostjad + 1, 2):
    summa = summa + i
print("Lillede koguarv on " + str(summa) + ".")
    