# import euro_zloty
import potencjalny_zysk
import Obliczanie_podatku_do_zaplaty
import zdolnosc_kredytowa
import zdrowie
import os

def podaj_dane(self):
    saldo_pln = input("Podaj ile masz oszczednosci w PLN ")
    wiek = input("Podaj swoj wiek")
    plec = input("Podaj plec")


if __name__ == "__main__":
    while True:
        os.system("cls")
        print("MENU:\n")
        print("[1] - Przelicz EUR/PLN PLN/EUR")
        print("[2] - Oblicz zdolnosc kredytowa")
        print("[3] - Sprawdz swoje zdrowie")
        print("[4] - Oblicz podatek")
        print("[5] - Oblicz potencjalny zysk")
        print("[0] - Wyjscie")
        key = str(input("Wybierz od 0 do 5: "))
        if(key == "0"):
            break
        elif (key == "1"):
            euro_zloty.przeliczWaluty()
        elif(key == "2"):
            pass
        elif(key == "3"):
            pass
        elif(key == "4"):
            pass
        elif(key == "5"):
            pass
        else:
            print("Wybierz poprawnie od 0 do 5.")