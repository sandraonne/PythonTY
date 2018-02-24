print("Sisestage kirja suurus:")
suurus = float(input())
print("Sisestage kirja teema pealkiri:")
pealkiri = input()
print("Kas kirjaga on kaasas fail?")
fail = input()
if pealkiri == "" or (fail == "jah" and suurus > 1):
    print("Kiri on spämm")
else:
    print("Kiri ei ole spämm")
    
    
    