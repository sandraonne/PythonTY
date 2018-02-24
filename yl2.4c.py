print("Inimeste arv:")
inimeste_arv = int(input())
print("Kohtade arv:")
kohtade_arv = int(input())
bussid = inimeste_arv // kohtade_arv
jääk = inimeste_arv % kohtade_arv
if bussid >= 1 and jääk!=0:
    bussid2 = int(bussid) + 1
    print("Busse vaja: " + str(bussid2))
    print("Viimases bussis inimesi: " + str(jääk))
if bussid >= 1 and jääk == 0:
    jääk2 = jääk + kohtade_arv
    print("Busse vaja: " + str(bussid))
    print("Viimases bussis inimesi: " + str(jääk2))
if bussid < 1:
    print("Busse vaja: 1")
    print("Viimases bussis inimesi: " + str(inimeste_arv))
    