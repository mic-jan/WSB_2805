dochód = float(input("Wprowadź roczny dochód: "))

if dochód < 85528:
    podatek = (dochód * 0.18) - 556
else:
    podatek = ((dochód - 85528) * 0.32) + 14839

if podatek < 0: podatek = 0

podatek = round(podatek, 0)
print("Podatek wynosi:", podatek)
