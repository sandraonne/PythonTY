failinimi = input("Palun sisestage failinimi:")
fail = open(failinimi, encoding="UTF-8")
sihtkohad = []
for rida in fail:
    sihtkohad.append(rida)
    print("Võimalikud sihtkohad:" + rida)

print("Valige mitmes sihtkoht broneerida:")
mitmes = int(input())
failisisu = []
for rida in failisisu:
    failisisu += [rida.strip()]
print("Reis on broneeritud. Sihtkoht on " + sihtkohad [mitmes - 1])
fail.close()