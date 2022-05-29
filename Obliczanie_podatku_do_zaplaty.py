dochód = float(input("Wprowadź roczny dochód: "))

if dochód < 125000:
    podatek = (dochód * 0.12) - 556
else:
    podatek = (dochód * 0.32) + 556

if podatek < 0: podatek = 0

podatek = round(podatek, 0)
print("Podatek wynosi:", podatek)
