#Klient jest zdrowy kiedy:
#puls jest od 60 do 100 uderzen na min
#temperatura = 36,6
#nalogi = NIE

puls =float(input("Wprowadź puls: "))
temperatura =float(input("Wprowadź temperature: "))
nalogi =str(input("Wprowadź TAK/NIE: "))

def sprawdzenie_zdrowia (puls, temperatura, nalogi):
    if (puls <=100 and puls >=60 and temperatura == 36.6 and nalogi == "NIE"):
        print ("Jest zdrowy")
    else: print ("Jest chory")

print ("Czy klient jest zdrowy?")
sprawdzenie_zdrowia(puls, temperatura, nalogi)
