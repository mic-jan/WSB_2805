#Program obliczający zyski z lokat bankowych


def potencjalny_zysk(wklad,procent,czas):
    print("Witaj w programie obliczającym zysk z lokaty bankowej netto. \n")
    odsetki = (wklad * (procent/100) * czas)/360
    podatek = odsetki * 0.19
    zysk = round((odsetki - podatek), 2)

    return zysk



if __name__== "__main__":
    print(potencjalny_zysk(100,5,180))




