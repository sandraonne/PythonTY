def lõimede_pikkus(vaiba_pikkus, lõimede_arv):
    return lõimede_arv * (vaiba_pikkus * 1.2 + 0.5)
 
failinimi = input("Sisestage failinimi: ")
pikemad_vaibad = int(input("Sisestage 5-meetriste ja pikemate vaipade lõimede arv: "))
lühemad_vaibad = int(input("Sisestage lühemate vaipade lõimede arv: "))
 
vaipade_pikkused = []
f = open(failinimi)
for rida in f:
    vaipade_pikkused += [float(rida)]
 
lõimede_pikkused = []
 
for pikkus in vaipade_pikkused:
    if pikkus >= 5:
        lõime_pikkus = lõimede_pikkus(pikkus, pikemad_vaibad)
        print(round(lõime_pikkus, 3))
        lõimede_pikkused += [lõime_pikkus]
    else:
        lõime_pikkus = lõimede_pikkus(pikkus, lühemad_vaibad)
        print(round(lõime_pikkus, 3))
        lõimede_pikkused += [lõime_pikkus]
         
arv = 0
summa = 0
for pikkus in lõimede_pikkused:
    if pikkus >= pikemad_vaibad:
        arv += 1
        summa += pikkus

print("Kõigi vaipade peale läheb vaja " + str(round(summa, 3)) + " meetrit lõimeniiti.")
