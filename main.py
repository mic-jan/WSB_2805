import euro_zloty
import potencjalny_zysk
# import Obliczanie_podatku_do_zaplaty
import zdolnosc_kredytowa
import zdrowie
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
    def zakonczyc(self):
        zakonczyc = input("zakonczyc? y or n: ")
        if zakonczyc == "y":
            return False
        else:
            return True

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
            pass
        elif (key == "2"):
            pass
        elif (key == "3"):
            pass
        elif (key == "4"):
            pass
        elif (key == "5"):
            mirek.oblicz_potencjalny_zysk()
            trwac=mirek.zakonczyc()
        else:
            print("Wybierz poprawnie od 0 do 5.")
