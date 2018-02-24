print("Sisestage oma nimi:")
nimi = input()
print("Sisestage lubatud kiirus (km/h):")
lubatud_kiirus = int(input())
print("Sisestage tegelik kiirus (km/h:")
tegelik_kiirus = int(input())
esialgne_trahv = (tegelik_kiirus - lubatud_kiirus) * 3
miinimum = min(190, esialgne_trahv)
print(nimi + ", kiiruse ületamise eest on teie trahv " + str(miinimum) + " eurot")