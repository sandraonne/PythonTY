from datetime import *
päev = datetime.now().day

failinimi = input("Sisestage failinimi:")
nimed = []
fail = open(failinimi, encoding="UTF-8")
for rida in fail:
    nimed.append(rida)
fail.close()
print("Vastama tuleb: " + nimed[päev - 1])