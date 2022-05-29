def zdolnosc_kredytowa(wiek, plec, zarobki):
    if plec == "M":
        zdolnosc = ((65 - wiek) * 12 * zarobki) * 0.25
    elif plec == "K":
        zdolnosc = ((60 - wiek) * 12 * zarobki) * 0.25
    return int(zdolnosc)