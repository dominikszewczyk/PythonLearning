# Magazyn wysyłki książek

class Magazyn(object):
    def __init__(self):
        self.ksiazki = {}

    def dodajKsiazke(self, ksiazka):
        """dodaje książkę do magazynu"""
        if ksiazka in self.ksiazki.keys():
            self.ksiazki[ksiazka.nazwa] = (1, ksiazka.cena)
        else:
            old_count = self.ksiazki[ksiazka] # !!!!!!!!!!! Zapytać jak inkrementować oto to !!!!!!!!!!

    def stanMagazynowy(self):
        return self.ksiazki



class Paczka(object):
    def __init__(self, klient):
        """inicjalizuję paczkę klienta"""
        self.klient = klient
        self.ksiazki = {}

    def dodaj(self, ksiazka):
        """dodaje książkę do paczki"""
        if ksiazka in self.ksiazki.keys():
            self.ksiazki[ksiazka] = 1
        else:
            self.ksiazki[ksiazka] = 1 #!!!!!!!!!!! Zapytać jak inkrementować oto to !!!!!!!!!!

    def oddaj(self, ksiazka):
        """oddaj książkę z paczki"""
        if not self.ksiazki[ksiazka] > 1:
            self.ksiazki[ksiazka].append(1)
        else:
            del self.ksiazki[ksiazka]

    def zawartosc(self):
        """raportuje zawartość paczki"""
        return self.ksiazki, self.klient


class Klient(object):
    def __init__(self, nazwa, adres):
        """inicjalizuje klienta"""
        self.nazwa = nazwa
        self.adres = adres

    def dajInfo(self):
        """zwraca informacje o kliencie"""
        return self.nazwa, self.adres


class Sprzedawca(object):
    def dodajKsiazke(self, ksiazka, paczka):
        """dodaje książkę do paczki"""
        paczka.dodaj(ksiazka)

    def oddajKsiazke(self, ksiazka, paczka):
        """usuwa książkę z paczki"""
        paczka.oddaj(ksiazka)

    def finalizuje(self, paczka):
        """wysyła paczkę"""
        print("-" * 40)
        print("Zamówienie dla klienta: {}".format(paczka.klient.nazwa))
        print("Wysyłane na adres: {}".format(paczka.klient.adres))
        print("-" * 40)
        suma = 0
        for index, ksiazka in enumerate(paczka.ksiazki.keys()):
            print("{}. {} ({} zł) - {} szt.".format(index+1, ksiazka.dajInfo()[0],
                                                    ksiazka.dajInfo()[1],
                                                    paczka.ksiazki[ksiazka]))
            suma += ksiazka.dajInfo()[1] * paczka.ksiazki[ksiazka]
        print("-" * 40)
        print("SUMA: {} zł".format(suma))
        print()
        print()


class Ksiazka(object):
    def __init__(self, nazwa, cena):
        """tworzy książkę"""
        self.nazwa = nazwa
        self.cena = cena

    def dajInfo(self):
        """zwraca informacje o książce"""
        return self.nazwa, self.cena


if __name__ == "__main__":
    klient1 = Klient("Dominik Szewczyk", "ul. Koszykarska 31A/73, 30-717 Kraków")
    # print("Klient: {}, i jej/jego adres: {}".format(klient1.dajInfo()[0], klient1.dajInfo()[1]))
    klient2 = Klient("Agnieszka Boguszewska-Szewczyk", "33-374 Klęczany 224")
    # print("Klient: {}, i jej/jego adres: {}".format(klient2.dajInfo()[0], klient2.dajInfo()[1]))

    paczka1 = Paczka(klient1)
    #p rint(paczka1.zawartosc()[0], paczka1.zawartosc()[1].dajInfo())
    paczka2 = Paczka(klient2)
    # print(paczka2.zawartosc()[0], paczka2.zawartosc()[1].dajInfo())

    ksiazka1 = Ksiazka("Python programowanie od podstaw", 100)
    # print("Książka: {}, i jej cena: {} zł".format(ksiazka1.dajInfo()[0], ksiazka1.dajInfo()[1]))
    ksiazka2 = Ksiazka("Podstawy C++", 250)
    # print("Książka: {}, i jej cena: {} zł".format(ksiazka2.dajInfo()[0], ksiazka2.dajInfo()[1]))
    ksiazka3 = Ksiazka("Alicja w Krainie Czarów", 15)
    # print("Książka: {}, i jej cena: {} zł".format(ksiazka3.dajInfo()[0], ksiazka3.dajInfo()[1]))

    sprzedawca = Sprzedawca()
    sprzedawca.dodajKsiazke(ksiazka1, paczka1)
    sprzedawca.dodajKsiazke(ksiazka2, paczka1)
    sprzedawca.dodajKsiazke(ksiazka3, paczka1)
    sprzedawca.dodajKsiazke(ksiazka3, paczka2)

    sprzedawca.finalizuje(paczka1)
    sprzedawca.finalizuje(paczka2)
