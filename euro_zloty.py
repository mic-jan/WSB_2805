def przeliczWaluty():
    # Pobranie informacji co użytkownik chce przeliczyć i w jakiej ilości
    podajWalute = input("Podaj walutę do przeliczenia:\n")
    ilosc = input("Podaj ilość PLN do przeliczenia na " + podajWalute + "\n")

    # program przelicza PLN na euro
    if podajWalute == "PLN" or podajWalute == "PLN":
        wynik = int(ilosc) * 4.57
        print('%0.2f' % wynik)
    else:
        print("Error: Sproboj jeszcze raz.")
        przeliczWaluty()


przeliczWaluty()