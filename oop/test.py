from oop.osoba import Osoba
from oop.pol import Pol

person1 = Osoba("John", "Doe", "1234567890123", "1990-05-15")
person2 = Osoba("Jane", "Smith", "9876543210987", "1995-10-20", pol=Pol.ZENSKI)
print(person1._Osoba__jmbg)
print(person1.jmbg)
person1.jmbg="AAA"
print(person2)
#%%



#%%

string = "abc"
broj = int(string)  # Ovo će izazvati ValueError
#%%