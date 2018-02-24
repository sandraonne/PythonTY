def kodeeri(sümbol, nihe):
     return chr(ord(sümbol) + nihe)
 
def šifreeri(failinimi, nihe):
    f = open(failinimi, "w")
    kiri = input("Sisesta lause ")
    for sümbol in kiri:
        f.write(kodeeri(sümbol, nihe))
    f.close()
 
failinimi = input("Faili nimi? ")
nihe = int(input("Nihe? "))
šifreeri(failinimi, nihe)