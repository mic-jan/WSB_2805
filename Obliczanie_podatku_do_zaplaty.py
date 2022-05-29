def Podatek():
    dochod = float(input("Wprowadź roczny dochód: "))

    if dochod <= 124999 and dochod >= 5000:
        podatek = (dochod * 0.12) - 556
    elif dochod > 125000:
        podatek = (dochod * 0.32) - 556
    else:
        podatek = 0


    podatek = round(podatek, 0)
    return podatek

print("Podatek wynosi:", Podatek() )
