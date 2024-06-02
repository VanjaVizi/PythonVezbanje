from oop.osoba import Osoba

class Ispit:
    def __init__(self, datum, ocjena, naziv):
        self.datum = datum
        self.ocjena = ocjena
        self.naziv = naziv

class Student(Osoba):
    def __init__(self, ime, prezime, jmbg, datumRodjenja, broj_indeksa, prosecna_ocena, esp_poena):
        super().__init__(ime, prezime, jmbg, datumRodjenja)
        self.broj_indeksa = broj_indeksa
        self.prosecna_ocena = prosecna_ocena
        self.esp_poena = esp_poena
        self.ispiti = []  # Lista ispita

    def dodaj_ispit(self, datum, ocjena, naziv):
        ispit = Ispit(datum, ocjena, naziv)
        self.ispiti.append(ispit)

    def __str__(self):
        ispit_str = "\n".join([f"Datum: {ispit.datum}, Ocena: {ispit.ocjena}, Naziv ispita: {ispit.naziv}" for ispit in self.ispiti])
        return (f"Ime: {self.ime}, Prezime: {self.prezime}, JMBG: {self.jmbg}, "
                f"Broj indeksa: {self.broj_indeksa}, Prosecna ocena: {self.prosecna_ocena}, ESP poeni: {self.esp_poena}\n"
                f"Ispiti:\n{ispit_str}")


    @property
    def broj_indeksa(self):
        return self.__broj_indeksa

    @broj_indeksa.setter
    def broj_indeksa(self, value):
        try:
            godina, broj = value.split('/')
            if len(godina) != 4 or len(broj) != 4:
                raise ValueError("Neispravan format broja indeksa")
            godina = int(godina)
            broj = int(broj)
            if godina < 2000 or godina > 2024:
                raise ValueError("Godina izvan dozvoljenog opsega")
            if broj < 0 or broj > 9999:
                raise ValueError("Broj izvan dozvoljenog opsega")
            self.__broj_indeksa = value
        except ValueError as err:
            print(f"Greška pri postavljanju broja indeksa: {err}")

    @property
    def prosecna_ocena(self):
        return self.__prosecna_ocena

    @prosecna_ocena.setter
    def prosecna_ocena(self, value):
        try:
            value = float(value)
            if value < 6.00 or value > 10.00:
                raise ValueError("Nedozvoljena prosječna ocjena")
            self.__prosecna_ocena = value
        except ValueError as err:
            print(f"Greška pri postavljanju prosječne ocjene: {err}")

    @property
    def esp_poena(self):
        return self.__esp_poena

    @esp_poena.setter
    def esp_poena(self, value):
        try:
            value = int(value)
            if value < 0 or value > 240:
                raise ValueError("Nedozvoljeni ESP poeni")
            self.__esp_poena = value
        except ValueError as err:
            print(f"Greška pri postavljanju ESP poena: {err}")

# Testiranje
student1 = Student("Marko", "Marković", "1234567890123", "1990-05-15", "2022/1234", 8.5, 150)
student1.dodaj_ispit("2024-05-05", 9, "Matematika")
student1.dodaj_ispit("2024-05-10", 8, "Fizika")
print(student1)


#%%
