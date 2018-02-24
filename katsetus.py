from random import randint
print("Sisestage visketabavuse protsent:")
protsent = int(input())
vise = 0
tabatud_visked = 0
while vise < 1000:
    tabavus = randint(1, 100)
    tabatud_visked = tabatud_visked + vise
    vise = vise + 1
    if tabavus <= protsent:
        print(str(vise) + ". vise tabas")
    else:
        print(str(vise) + ". vise mööda")
print("Tabas " + str(tabatud_visked) + " viset.")