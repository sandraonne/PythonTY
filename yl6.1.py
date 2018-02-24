def banner(reklaamlause):
    return(reklaamlause.upper())

print("Mitu korda soovite reklaamlauset kuvada?")
kordus = int(input())
print("Sisestage reklaamlause:")
reklaamlause = input()

for i in range(kordus):
    print(banner(reklaamlause))