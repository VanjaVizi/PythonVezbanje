from datetime import datetime
from vezbe567.putnik import Putnik

class Let:
    poletanje_dt_format = '%Y-%m-%d %H:%M'

    def __init__(self, broj_leta, poletanje_dt, ruta):
        self.broj_leta = broj_leta
        self.vreme_poletanja = poletanje_dt
        self.ruta = ruta
        self.putnici = list()

    @property
    def vreme_poletanja(self):
        # if not hasattr(self, '_Let__vreme_poletanja'):
        #     self.__vreme_poletanja = None
        # return self.__vreme_poletanja
        try:
            return self.__vreme_poletanja
        except AttributeError:
            self.__vreme_poletanja = None
            return self.__vreme_poletanja


    @vreme_poletanja.setter
    def vreme_poletanja(self, value):
        if not isinstance(value, (datetime, str)):
            stderr.write(f"Iz vreme_poletanja.setter: ocekivan ulazni argument tipa datetime ili str; "
                         f"umesto toga, primljena vrednost tipa {type(value)}\n")
            return
        if isinstance(value, str):
            try:
                value = datetime.strptime(value, Let.poletanje_dt_format)
            except ValueError:
                stderr.write(f"Iz vreme_poletanja.setter: String zapis vremena poletanja ne odgovara ocekivanom formatu {Let.poletanje_dt_format}\n")
                return
        if value > datetime.now():
            self.__vreme_poletanja = value
        else:
            stderr.write("Iz vreme_poletanja.setter: vreme poletanja se mora odnositi na neki trenutak u buducnosti\n")


    def dodaj_putnika(self, obj):
        if not isinstance(obj, Putnik):
            print("Iz dodaj_putnika: ulazni argument nije objekat klase Putnik\n")
            return
        if obj in self.putnici:
            print("Iz dodaj_putnika: putnik se vec nalazi u listi putnika\n")
            return
        if not obj.COVID_bezbedan:
            print("Iz dodaj_putnika: putnik nema validno uverenje da je COVID bezbedan\n")
            return

        self.putnici.append(obj)
        print(f"Putnik {obj.ime} je uspesno dodat u listu putnika")

    @property
    def ruta(self):
        try:
            return self.__ruta
        except AttributeError:
            self.__ruta = None
            return self.__ruta

    @ruta.setter
    def ruta(self, value):  #Beograd, Rim
        if isinstance(value, (list, tuple)) and len(value) == 2:
            self.__ruta = tuple(value)
            return
        if isinstance(value, str) and sum([ch in ',->' for ch in value]) == 1:
            #[0, 0.... FALSE, 1, FAlSE FALSE FALSE]
            import re
            # alternativno, patter u narednoj liniji koda se moze zapisati: ',|-|>'
            # gde karakter '|' znaci 'ili'
            value_split = re.split('[,->]', value)    #[123]
            polazak, destinacija = value_split
            self.__ruta = polazak.strip(), destinacija.strip()
            return
        stderr.write(f"Iz ruta.setter: ruta leta je zadata u neodgovarajucem obliku\n")


    @classmethod
    def from_dict(cls, d):
        def key_val(kljuc):
            return d[kljuc] if kljuc in d.keys() else None
        try:
            return cls(d['br_leta'], d['vreme_poletanja'], (d['polazna_lokacija'], d['odrediste']))
        except KeyError:
            potrebni_kljucevi = ['br_leta', 'vreme_poletanja', 'polazna_lokacija', 'odrediste']
            validni_kljucevi = [kljuc for kljuc in d.keys() if kljuc in potrebni_kljucevi]
            print("Nisu raspolozivi svi podaci o letu -> Let objekat ce biti kreiran na osnovu sledecih podataka:")
            print(", ".join(validni_kljucevi))
            return cls(key_val('br_leta'), key_val('vreme_poletanja'),
                       (key_val('polazna_lokacija'), key_val('odrediste')))




    def __str__(self):
        let_str = f"Let {self.broj_leta}:\n"
        let_str += f"Planirano vreme poletanja: {self.vreme_poletanja}\n"
        let_str += f"Ruta leta: {self.ruta_str()}\n"
        if len(self.putnici) == 0:
            let_str += "Putnici: jos uvek nema prijavljenih putnika"
        else:
            let_str += "Putnici:\n" + "\n".join([str(p) for p in self.putnici])
        return let_str


    def vreme_do_poletanja(self):
        if not self.vreme_poletanja:
            return None
        poletanja_delta = self.vreme_poletanja - datetime.now()
        print(poletanja_delta)
        delta_dani = poletanja_delta.days
        delta_sati, ostatak_sec = divmod(poletanja_delta.seconds, 3600)
        delta_mins = ostatak_sec // 60
        return delta_dani, delta_sati, delta_mins


    def __iter__(self):
        self.__indeks_sledeceg = 0
        return self

    def __next__(self):
        if self.__indeks_sledeceg == len(self.putnici):
            raise StopIteration

        sledeci_putnik = self.putnici[self.__indeks_sledeceg]
        self.__indeks_sledeceg += 1
        return sledeci_putnik


    def generator_putnika_sa_uslugama(self):
        from collections import defaultdict
        usluge_dict = defaultdict(int)
       # lista=[]
        for putnik in self.putnici:
            if len(putnik.usluge) > 0:
                for usluga in putnik.usluge:
                    usluge_dict[usluga] += 1
              #  lista.append(putnik)
                yield putnik
        #return lista
        print(f"\nPutnici na letu {self.broj_leta} su narucili sledece usluge:")
        print("; ".join([f"{usluga.value}: {broj}" for usluga, broj in usluge_dict.items()]))


    def generator_kandidata_za_biznis_klasu(self, min_cena_karte):

       # kandidati = []
       # for putnik in self.putnici:
      #      if isinstance(putnik, PutnikEkonomskeKlase) and len(putnik.usluge) > 0 and putnik.cena_karte > min_cena_karte:
         #       kandidati.append(putnik)


        kandidati = [putnik for putnik in self.putnici
                     if isinstance(putnik, PutnikEkonomskeKlase) and len(putnik.usluge) > 0 and
                     putnik.cena_karte > min_cena_karte]
        sorted_kandidati = sorted(kandidati, reverse=True, key=lambda k: k.cena_karte)
        #return sorted_kandidati
        for kandidat in sorted_kandidati :
            yield kandidat




if __name__ == '__main__':

    lh1411 = Let('LF1411', '2025-05-05 6:50')
    lh992 = Let('LH992', '2025-05-25 12:20')

    print("\nLETOVI:\n")
    print(lh1411)
    print()
    print(lh992)
    print()

    bob = Putnik("Bob Smith", "UK", "123456", True)
    john = Putnik("John Smith", "USA", 987656, True)
    anna = Putnik("Anna Smith", "Spain", "987659")
    luis = Putnik.covid_bezbedan_Francuz("Luis Bouve", "123654")

    print(f"\nDodavanje putnika na let {lh1411.broj_leta}")
    for p in [bob, john, anna, luis]:
        lh1411.dodaj_putnika(p)

    print(f"\nPokusaj dodavanja putnika koji je vec u listi putnika za let {lh1411.broj_leta}:")
    lh1411.dodaj_putnika(Putnik("J Smith", "USA", "987656", True))
    print()

    print(f"\nPodaci o letu {lh1411.broj_leta} nakon dodavanja putnika na let:\n")
    print(lh1411)


    do_poletanja = lh1411.vreme_do_poletanja()
    print(do_poletanja)


    p_iter = iter(lh1411)
    try:
        while True:
            print(next(p_iter))
    except StopIteration:
        print("Svi putnici su izlistani")


    for p in iter(lh1411):
        print(p)


    g = lh1411.generator_putnika_sa_uslugama()
    while True:
        try:
            print(next(g))
        except StopIteration:
            print("------- kraj spiska putnika sa dodatnim uslugama --------")
            break
    print()

    g = lh1411.generator_putnika_sa_uslugama()
    for putnik in g:
        print(putnik)




#%%
