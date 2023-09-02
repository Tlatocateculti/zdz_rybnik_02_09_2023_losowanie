import random

class Losowanie:
    def __init__(self):
        self.__wyniki = set()
        self.__typ_uzytkownik = set()

    def losuj(self, ile = 1):
        for k in range(ile):
            tmp_list = []
            for i in range(6):
                tmp_list.append(random.randint(1, 51))
            self.__wyniki.add(tuple(tmp_list))

    def porownaj(self):
        for wynik in self.__wyniki:
            #licznik = 0
            #wyniki_uzytkownik = ""
            for uwynik in self.__typ_uzytkownik:
                licznik = 0
                #wyniki_uzytkownik += str(uwynik) + ", "
                for uliczba in uwynik:
                    if uliczba in wynik: licznik+=1
                print("W losowaniu", wynik, "użytkownik przy wytypowaniu", uwynik, "trafiłby", licznik)
            #print("W losowaniu", wynik, "użytkownik przy wytypowaniu", wyniki_uzytkownik, "trafiłby", licznik)

    def dodaj_recznie(self):
        tmp_lista = []
        i=1
        while i < 7:
        #for i in range(6):
            liczba = int(input("Podaj "+ str(i) + "liczbę z przedziału 1-50: "))
            if 1 <= liczba <= 50:
                tmp_lista.append(liczba)
                i+=1
        self.__typ_uzytkownik.add(tuple(tmp_lista))

    def dodaj_typ(self, liczby = None):
        if liczby is None:
            return self.dodaj_recznie()
        self.__typ_uzytkownik.add(tuple(liczby))

los = Losowanie()
los.losuj(5)
los.dodaj_typ((5,11,34,40,45,50))
los.dodaj_typ((7,28,1,46,34,12))
los.dodaj_typ((9,15,21,33,40,49))
los.dodaj_typ()
los.porownaj()





"""
Program ma za zadanie:
- pobierać od użytkownika 6 liczb z zakresu 1 - 50 (warunek ograniczający)
- program losuje 6 wartości między 1 - 50
- każdy z wyników zapisujemy w dowolnej zmiennej zbiorczej
- użytyknik, jeżeli wpisze słowo "SPRAWDZAM" ma otrzymać wszystkie zapisane wyniki z informacją ile liczb trafił
import random

random.randint(start, stop)
"""