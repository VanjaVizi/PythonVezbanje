from datetime import datetime, date
from oop.pol import Pol
class Osoba:
    def __init__(self, ime, prezime, jmbg, datumrodjenja, pol=Pol.MUSKI):
        self.ime = ime
        self.prezime = prezime
        self.jmbg = jmbg
        self.datumrodjenja = datetime.strptime(datumrodjenja, '%Y-%m-%d').date()
        self.pol = pol
        self.br_godina = self._izracunaj_godine(self.datumrodjenja)


    def _izracunaj_godine(self, datumrodjenja):
        danas = datetime.now().date()
        razlika = danas - datumrodjenja
        br_godina = razlika.days // 365
        return br_godina

    def __str__(self):
        return (f"Ime: {self.ime}, Prezime: {self.prezime}, JMBG: {self.jmbg}, "
                f"Datum rođenja: {self.datumrodjenja}, Godine: {self.br_godina}, Pol: {self.pol.value}")

    @property
    def jmbg(self):
        if not hasattr(self, '_Osoba__jmbg'):  # Provera privatnosti
            self.__jmbg = None
        return self.__jmbg

    @jmbg.setter
    def jmbg(self, value):
        if isinstance(value, str) and len(value) == 13 and value.isdigit():
            self.__jmbg = value
        else:
            print("Greska u formatu JMBG.")
    @property
    def ime(self):
        return self._ime

    @ime.setter
    def ime(self, novo_ime):
        if len(novo_ime) >= 3:
            self._ime = novo_ime
        else:
            raise ValueError("Ime mora sadržati barem 3 karaktera.")







#%%
