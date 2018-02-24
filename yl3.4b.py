from random import randint
print("Sisestage visketabavuse protsent:")
protsent = int(input())
vise = 0
tabatud_visked = 0
while vise < 1000:
    vise += 1
    if randint(1, 100) <= protsent:
        print(str(vise) + ". vise tabas")
        tabatud_visked = tabatud_visked + 1
    else:
        print(str(vise) + ". vise mööda")
print("Tabas " + str(tabatud_visked) + " viset.")
    