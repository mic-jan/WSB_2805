#Klient jest zdrowy kiedy:
#puls jest od 60 do 100 uderzen na min
#temperatura = 36,6
#nalogi = 0
def sprawdzenie_zdrowia (puls, temperatura, nalogi):
    if (puls <=100 and puls >=60 and temperatura == 36.6 and nalogi == 0):
        print ("zdrowy")
    else: print ("chory")

print ("wartosci: 80, 36.6,0")
sprawdzenie_zdrowia(88,36.6,0)

print ("wartosci:50, 36.4,0")
sprawdzenie_zdrowia(50,36.4,0)

print ("wartosci:102, 36.8,1")
sprawdzenie_zdrowia(102,36.8,1)