print("Sisesta ostjate arv:")
ostjad = int(input())
ostja_järjenumber = 1
lillede_koguarv = 0
lillede_arv_ostjale = 1
while ostja_järjenumber <= ostjad:
    lillede_koguarv += lillede_arv_ostjale
    lillede_arv_ostjale += 2
    ostja_järjenumber += 1
print("Lillede koguarv on " + str(lillede_koguarv) + ".")
    