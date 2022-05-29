import EURO_ZLOTY_EURO
import potencjalny_zysk
# import Obliczanie_podatku_do_zaplaty
import zdolnosc_kredytowa
# import zdrowie
import os

class Osoba:
    def __init__(self):
        pass
    def oblicz_potencjalny_zysk(self):
        wklad = int(input("Podaj wklad wlasny [PLN]: "))
        procent = int(input("Podaj oprocentowanie lokaty [%]: "))
        czas = int(input("Jak dlugo [ilosc dni]: "))
        self.zysk = potencjalny_zysk.potencjalny_zysk(wklad, procent, czas)
        print("Potencjalny zysk: ", self.zysk, " PLN")
    def oblicz_zdolnosc_kredytowa(self):
        wiek = int(input("Podaj wiek: "))
        plec = input("Podaj plec (M/K): ")
        zarobki = int(input("Podaj miesieczne zarobki: "))
        print("Twoja zdolnosc kredytowa wynosi: " + str((zdolnosc_kredytowa.zdolnosc_kredytowa(wiek, plec, zarobki))) + " PLN")
    def zakonczyc(self):
        zakonczyc = input("zakonczyc? y or n: ")
        if zakonczyc == "y":
            return False
        else:
            return True
    def przelicz(self):
        self.kwota = int(input("Podaj kwote do przeliczenia: "))
        self.przelicznik = str(input("Podaj EUR/PLN lub PLN/EUR: "))
        self.kantor_wynik = EURO_ZLOTY_EURO.rodzaj_waluty(self.kwota,self.przelicznik)
        print("Przeliczono ", self.kwota," ",self.przelicznik[:3]," na ", self.przelicznik[4:],"\nWynik: ",self.kantor_wynik," ",self.przelicznik[4:])
if __name__ == "__main__":
    trwac = True
    mirek=Osoba()
    while trwac:
        os.system("clear")

        print("MENU:\n")
        print("[1] - Przelicz EUR/PLN PLN/EUR")
        print("[2] - Oblicz zdolnosc kredytowa")
        print("[3] - Sprawdz swoje zdrowie")
        print("[4] - Oblicz podatek")
        print("[5] - Oblicz potencjalny zysk")
        print("[0] - Wyjscie")
        key = str(input("Wybierz od 0 do 5: "))
        if (key == "0"):
            break
        elif (key == "1"):
            mirek.przelicz()
            trwac=mirek.zakonczyc()
        elif (key == "2"):
            mirek.oblicz_zdolnosc_kredytowa()
            trwac=mirek.zakonczyc()
        elif (key == "3"):
            pass
        elif (key == "4"):
            pass
        elif (key == "5"):
            mirek.oblicz_potencjalny_zysk()
            trwac=mirek.zakonczyc()
        else:
            print("Wybierz poprawnie od 0 do 5.")
