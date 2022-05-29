#Program obliczający zyski z lokat bankowych


def potencjalny_zysk():
    print("Witaj w programie obliczającym zysk z lokaty bankowej netto \n.")
    wklad = int(input("Podaj kwote jaką chesz zainwestować: "))
    procent = int(input("Podaj oprocentowanie lokaty: "))/100
    czas = int(input("Okres trwania lokaty(w dniach): "))
    odsetki = (wklad * procent * czas)/360
    podatek = odsetki * 0.19
    zysk = round(odsetki - podatek)

    return zysk
#potrzebne na potrzeby testowania programu :)
print(potencjalny_zysk())