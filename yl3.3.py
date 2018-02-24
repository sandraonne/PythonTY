from random import randint

print("Täringute arv:")
arv = int(input())
i = 1
tulemus = 0
while i <= arv:
    vise = randint(1,6)
    print(vise)
    tulemus += vise
    i += 1