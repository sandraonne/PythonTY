fail = open("konto.txt", encoding="UTF-8")
konto = []
for rida in fail:
    konto.append(float(rida))
    if float(rida) >= 0:
        print(rida)
fail.close()


