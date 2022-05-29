
def sprawdzenie_zdrowia (puls, temperatura):
    if (puls <=100 and puls >=60 and temperatura == 36.6):
        print ("zdrowy")
    else: print ("chory")

print ("wartosci: 80, 36.6")
sprawdzenie_zdrowia(88,36.6)

print ("wartosci:50, 36.4")
sprawdzenie_zdrowia(50,36.4)

print ("wartosci:102, 36.8")
sprawdzenie_zdrowia(102,36.8)