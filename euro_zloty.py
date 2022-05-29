def przeliczWaluty():
    # Pobranie informacji co użytkownik chce przeliczyć i w jakiej ilości
    podajWalute = input("Podaj walutę do przeliczenia:\n")
    ilosc = input("Podaj ilość do przeliczenia na " + podajWalute + "\n")

    # program przelicza PLN na euro
    if podajWalute == "PLN":
        wynik = int(ilosc) * 4.57
        print('%0.2f' % wynik)
        return wynik


    # program przelicza EUR na zloty
    elif podajWalute == "EUR":
        wynik2 = int(ilosc) / 4.57
        print('%0.2f' % wynik2)
        return wynik2

if __name__ == "__main__":
         przeliczWaluty()

