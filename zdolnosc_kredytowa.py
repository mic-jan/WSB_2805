def zdolnosc_kredytowa(wiek, plec, zarobki):
    if plec == "M":
        zdolnosc = ((65 - wiek) * 12 * zarobki) * 0.25
    elif plec == "K":
        zdolnosc = ((60 - wiek) * 12 * zarobki) * 0.25
    if wiek < 18 or zdolnosc < 0:
        return 0
    return int(zdolnosc)

if __name__== "__main__":
    wiek = int(input("Podaj wiek: "))
    plec = input("Podaj plec (M/K): ")
    zarobki = int(input("Podaj miesieczne zarobki: "))
    print("Twoja zdolnosc kredytowa wynosi: " + str((zdolnosc_kredytowa(wiek, plec, zarobki))) + " PLN")

