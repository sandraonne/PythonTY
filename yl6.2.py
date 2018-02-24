def teleri_diagonaal(kaugus):
    return round(kaugus * 100 * 0.39 / 2.5)

print("Sisesta kaugus:")
kaugus = input()
print(teleri_diagonaal(kaugus))