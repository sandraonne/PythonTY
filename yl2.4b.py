from random import randint

print("Kas soovite istekohta ise valida (ise) või loosida (loos)?")
valik1 = input()
if valik1 == "ise":
    print("Kas soovite istuda akna ääres (aken) või mitte (muu)?")
    valik2 = input()
    if valik2 == "aken":
        print("Valisite ise. Aknakoht")
    else:
        print("Valisite ise. Vahekäigukoht")
if valik1 == "loos":
    suvaline = randint(1,3)
    if (suvaline <= 1):
        print("Istekoht loositi. Aknakoht")
    else:
        print("Istekoht loositi. Vahekäigukoht")