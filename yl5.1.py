fail = open("mopeedid.txt", encoding="UTF-8")
mopeedid = []
for rida in fail:
    mopeedid.append(int(rida))
fail.close()
print("Palun sisestage mitmes kuu:")
kuu = int(input())
print(str(kuu) + ". kuul registreeriti " + str(mopeedid[kuu - 1]) + " mopeedi.")

