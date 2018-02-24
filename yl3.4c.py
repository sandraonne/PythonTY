print("Sisestage täisarv:")
arv = int(input())
i = 1
nisuterad = 1
while i < arv:
    nisuterad = nisuterad * 2
    i = i + 1
print("Nisuteri " + str(arv) + ". ruudu eest:" + str(nisuterad))