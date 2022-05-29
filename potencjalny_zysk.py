#Program obliczający zyski z lokat bankowych


def potencjalny_zysk():
    print("Witaj w programie obliczającym zysk z lokaty bankowej netto.")
    wklad = int(input("Podaj kwote jaką chesz zainwestować: "))
    procent = int(input("Podaj oprocentowanie lokaty: "))/100
    print(procent)
    czas = int(input("Okres trwania lokaty(w dniach): "))
    x = (wklad * procent * czas)/360
    y = x * 0.19
    z = x-y
    print(y)

    return z

print(potencjalny_zysk())