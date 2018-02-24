print("Sisestage ainepunktide arv:")
ainepunktid = int(input())
ajakulu = ainepunktid * 26
print("Sisestage nädalate arv:")
nädalad = int(input())
nädala_ajakulu = round(ajakulu/nädalad)
print(nädala_ajakulu)