print("Sisestage enda vanus:")
vanus = int(input())
print("Sisestage enda sugu:")
sugu = input().lower()
print("Sisestage treeningu tüüp:")
tüüp = int(input())
mehe_max = 220 - vanus
naise_max = 206 - ((vanus * 88) / 100)

mvähim1 = mehe_max * 50 / 100
msuurim1 = mehe_max * 70 / 100
mvähim2 = mehe_max * 70 / 100
msuurim2 = mehe_max * 80 / 100
mvähim3 = mehe_max * 80 / 100
msuurim3 = mehe_max * 87 / 100
if sugu == "m" and tüüp == 1:
    print("Pulsisagedus peaks olema vahemikus " + str(round(mvähim1)) + " kuni " + str(round(msuurim1)) + ".")
elif sugu == "m" and tüüp == 2:
    print("Pulsisagedus peaks olema vahemikus " + str(round(mvähim2)) + " kuni " + str(round(msuurim2)) + ".")
elif sugu == "m" and tüüp == 3:
    print("Pulsisagedus peaks olema vahemikus " + str(round(mvähim3)) + " kuni " + str(round(msuurim3)) + ".")

nvähim1 = naise_max * 50 / 100
nsuurim1 = naise_max * 70 / 100
nvähim2 = naise_max * 70 / 100
nsuurim2 = naise_max * 80 / 100
nvähim3 = naise_max * 80 / 100
nsuurim3 = naise_max * 87 / 100
if sugu == "n" and tüüp == 1:
    print("Pulsisagedus peaks olema vahemikus " + str(round(nvähim1)) + " kuni " + str(round(nsuurim1)) + ".")
elif sugu == "n" and tüüp == 2:
    print("Pulsisagedus peaks olema vahemikus " + str(round(nvähim2)) + " kuni " + str(round(nsuurim2)) + ".")
elif sugu == "n" and tüüp == 3:
    print("Pulsisagedus peaks olema vahemikus " + str(round(nvähim3)) + " kuni " + str(round(nsuurim3)) + ".")