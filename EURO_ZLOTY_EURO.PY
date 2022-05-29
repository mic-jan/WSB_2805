def rodzaj_waluty(ilosc,rodzaj_przelicznika):
    if rodzaj_przelicznika == "EUR/PLN":
        przelicz_waluty = int(ilosc) / 4.57
        return przelicz_waluty
    elif rodzaj_przelicznika == "PLN/EUR":
        przelicz_waluty = int(ilosc) * 4.57
        return przelicz_waluty
if __name__ == "__main__":
    print(rodzaj_waluty(100,'EUR/PLN'))
    print(rodzaj_waluty(100,'PLN/EUR'))
