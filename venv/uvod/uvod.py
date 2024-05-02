import math

total=0
i=0
while i <= 20:
    total = total + i
    i = i + 1
print ("The total = ", total)
# "Vanja's   "

# """Vanja je rekla 'Cao'."""
#%%
a=input( "Enter a real value:" )
a
#01234
#VANJA
#   -3-2-1
#%%
#1.	Napisati program koji omogućava korisniku unos imena i broja godina.
# Program ispisuje poruku korisniku koja ga obaveštava koje godine će
# korisnik napuniti 100 godina.

from datetime import datetime
ime = input( "Unesi ime\n" )
godine = int(input( "Unesi godine\n" ))
trenutnaGod=datetime.now().year
resenje = trenutnaGod-godine+100
print("\n"+ime+", imaces 100 godina "+str(resenje)+" godine")



#%%
#2.	Omogućiti korisniku unos broja. Ispisati poruku o tome da li je
# broj paran ili ne.

broj = int(input( "Unesi broj\n" ))
if broj%2==0:
    print("\nBroj je paran")
else:
    print("\nBroj nije paran")
#%%

#%%
#3.	Napisati program koji od liste  a = [5, 10, 15, 20, 25]
# pravi novu listu koja se sastoji samo od prvog I poslednjeg elementa liste a.

def novaListaFja(a):
    novaLista = [a[0],a[-1]]
    return novaLista
a = [5, 10, 15, 20, 25]
#novaLista = [a[0],a[-1]]
# #novaLista = [a[0],a[len(a)-1]]
novaLista=novaListaFja(a)
print(novaLista)


#%%
#4.	Napisati funkciju koja prima tri broja kao parametre i vraca najveći.
# Nije dozvoljeno korišćenje funkcije max().
#            2 5 8
def maxodtri(a,b,c):
    if a>b and a>c:
        return a
    elif  b>a and b>c:
        return b
    else:
        return c
a=5
b=10
c=17
#najveci = max(a,max(b,c))
najveci= maxodtri(a,b,c)
print(najveci)

#%%
#5.	Data je lista a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89] .
# Napisati program koji ispisuje sve elemente koji su manji od 5.

a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
novaLista=[]
for element in a:
    if element <5:
        print(element)
        novaLista.append(element)
print(novaLista)
print([element for element in a if element<5])







#%%

#6.	Napisati program koji omogućava korisniku unos broja. Program zatim ispisuje sve delioce ovog broja.

broj = int(input( "Unesi broj\n" )) #10, 1 2 3 4..10
delioci=[]

for i in range(1,broj+1):
    if(broj%i==0):
        delioci.append(i)

print(delioci)
#%%

#7.	Date su dve liste a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89] i
# b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]. Napisati program koji vraća treću
# listu koja predstavlja uniju ove dve liste, ali tako da se elementi ne ponavljaju.

a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
unija=[]
for element in a:
    if element not in unija:
        unija.append(element)

for element in b:
    if element not in unija:
        unija.append(element)
print(unija)
set_a = set(a)  # {1,2,3}
set_b = set(b)
set_unija = set_a.union(set_b)
set_presek = set_a.intersection(set_b)
set_razlika = set_a.difference(set_b)
set_simetricna_razlika = set_a.symmetric_difference(set_b)
lista_unija = list(set_unija)
print(set_unija)
print(lista_unija)


#%%
#8.	Napisati program koji omogućava korisniku unos stringa. Program zatim ispisuje korisniku poruku
# o tome da li je string palindrom ili ne.
#anavolimilovana
rec = input("Unesite neki string:\n")
invertovanaRec = rec[::-1]
print(invertovanaRec)
if invertovanaRec == rec:
    print("Jeste palindrom")
else:
    print("Nije palindrom")


#%%
#9.	Napisati program koji omogućava korisniku unos broja n. Ovaj broj predstavlja broj
# elemenata fibonačijevog niza koji program treba da ispiše.
# 0 1 1 2 3 5 8 ....
n = int(input( "Unesi n\n" )) #5
fibonaci =[0,1]  #0 1 1 2 3
if n==1:
    print(fibonaci[0])
elif n==2:
    print(fibonaci)
else:
    for i in range(1,n-1):  #i=4
        fibonaci.append(fibonaci[i]+fibonaci[i-1])
        #fibonaci.append(1+0)
        #fibonaci.append(2+1)
print(fibonaci)

#%%
#10.	Napisati funkciju koja omogućava korisniku unos broja.
# Funkcija ispisuje poruku o tome da li je broj prost ili ne.
broj = int(input( "Unesi broj\n" ))
if(broj==1):
    print("Broj jeste prost\n")
else:
    brojac=0
    for i in range(1,broj+1):
        if broj%i==0:
            brojac=brojac+1
            print(i)

    if(brojac==2):
        print("Broj jeste prost\n")
    else:
        print("Broj nije prost\n")


#%%

#11.Napišite funkciju koja izračunava i štampa faktorijel broja. Funkcija prihvata broj
# (trebalo bi da bude pozitivan ceo broj) kao svoj jedini ulazni argument.
#5!=5*4*3*2
def faktorijel(broj):
    if(broj==0):
        return 1
    if (broj<=0):
        return -1
    rezultat=1
    for i in range(1,broj+1):
        rezultat=rezultat*i
    return  rezultat


broj = int(input( "Unesi broj\n" ))
resenje= faktorijel(broj)
if(resenje==-1):
    print("Broj koji ste uneli nije pozitivan ceo broj\n")
else:
    print("Resenje je "+str(resenje))

#%%
#12.	Napisati funkciju koja prima listu reči i vraća novu s rečima koje imaju više od n karaktera.
def viseodNkaraktera(lista,n):
    novaLista=[]
    for element in lista:
        if(len(element)>n):
            novaLista.append(element)
    return novaLista
   # return [element for element in novaLista if len(element)>n]
lista= ["asdsa",  "asdsaasda", "asdsaasdsa", "sa"]
n = int(input( "Unesi broj\n" ))
novaLista=viseodNkaraktera(lista,n)
print(novaLista)
#%%
 #13.	Napišite funkciju koja prima listu celih brojeva i vraća tuple sa tri vrednosti - zbir
# svih parnih brojeva u listi, proizvod svih neparan brojeva u listi, razlika između najvećeg i
# najmanjeg broja u listi.

def funkcijaz13(lista):
    zbirParnih=0
    proizvodNeparnih=1
    najmanji = min(lista)
    najveci=max(lista)
    razlika= najveci-najmanji
    for element in lista:
        if( element%2==0):
            zbirParnih=zbirParnih+element
        else:
            proizvodNeparnih=proizvodNeparnih*element

    return (zbirParnih,proizvodNeparnih,razlika)

a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
resenje = funkcijaz13(a)
print(resenje)


#%%
#15.	Napisati program koji generise random broj od 1 do 9. Napisati funkciju koja
# omogućava korisniku da pogađa broj sve dok ga ne pogodi. Nakon svakog pokušaja program
# ispisuje poruku korisniku da li je broj veći ili manji od unetog broja.
import random
def pogodiBroj():
    broj = random.randint(1,9)
    while True:
        pokusaj = int(input( "Unesi broj\n" ))
        if(pokusaj==broj):
            print("POGODJENO!")
            break
        elif pokusaj>broj:
            print("Broj je manji od unetog")
        else:
            print("Broj je veci od unetog")
pogodiBroj()
#%%
# #16.	Napišite funkciju koja prima listu brojeva i graničnu vrednost.
# Funkcija kreira novu listu sa jedinstvenim elementima iz ulazne liste koji
# su ispod praga, ispisuje broj elemenata u novoj listi, sortira elemente nove
# liste u opadajućem redosledu i štampa ih, po jedan element po redu.
#lista: 1 2 3 1 2 3 4 5 9
#novaLista:
def funkcijaz16(lista,gr):
    novaLista=[]
    for element in lista:
        if element <gr:
            if element not in novaLista:
                novaLista.append(element)

    novaLista=sorted(novaLista,reverse=True)
    for element in novaLista:
        print(element)

a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
funkcijaz16(a,13)



#%%
#17.	Napišite funkciju (sve_parne_cifre) koja pronalazi cele brojeve između 100 i 400
# (uključujući i ove brojeve) gde je svaka cifra broja parna. Brojeve koji odgovaraju
# ovom kriterijumu treba prikazati kao string u kome su brojevi odvojeni zarezom.

def sve_parne_cifre():
    resenje=[]
    for broj in range(100,401):
        string_broj = str(broj)   #"200"
        sve_parne=True
        for cifra in string_broj:   #cifra: "1","0","0"
            int_cifra=int(cifra)
            if(int_cifra%2!=0):
                sve_parne=False

        if(sve_parne==True):
            resenje.append(string_broj)
    print(", ".join(resenje))

sve_parne_cifre()

def sve_parne_cifre2():
    resenje=[]
    for broj in range(100,401):
        cifre=[ int(cifra) for cifra in str(broj) ]   #"1","0,0
        if all(cifra%2==0 for cifra in cifre):
            resenje.append(str(broj))

    print(", ".join(resenje))
sve_parne_cifre2()
#%%

#18.	Napišite funkciju (anagrami) koja prima dva stringa i proverava da li su anagrami.
# Funkcija vraća odgovarajuću logičku vrednost. Napomena: Anagram je reč ili fraza nastala
# preuređivanjem slova druge reči ili fraze. Dodatna uputstva: - Poređenje slova treba da bude
# neosetljivo na velika i mala slova. - Razmake i znake interpunkcije, ako postoje, treba zanemariti.

#lIs t4en           Si  le8nt
def anagrami(string1,string2):
    s1=""
    s2=""
    for element in string1:
        if element.isalpha():   #isDigit
            s1 = s1+element.lower()
    for element in string2:
        if element.isalpha():
            s2 = s2+element.lower()

    if len(s1)!=len(s2):
        return False
    s1 = sorted(s1)
    s2 = sorted(s2)
    if s1==s2:
        return True
    else:
        return False

string1="lIi-t4en "
string2="Si  le8nt"
print(anagrami(string1,string2))


def anagrami2(string1,string2):
    s1="".join(c for c in string1 if c.isalpha()).lower()
    s2="".join(c for c in string2 if c.isalpha()).lower()
    if len(s1)!=len(s2):
        return False
    s1 = sorted(s1)
    s2 = sorted(s2)
    if s1==s2:
        return True
    else:
        return False
string1="lIs-t4en "
string2="Si  le8nt"
print(anagrami2(string1,string2))
#%%

#20.	Napisati funkciju koja pronalazi I vraća drugi najveći element u listi.
#1 1 2 3    #2
def drugiNajveci(lista):
    lista = sorted(set(lista),reverse=True)
    if(len(lista) >=2) :
        return lista[1]
    else:
        return "NEMA"
lista = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
drugiNajveci(lista)

#%%
# 21.	Napisati funkciju koja iz liste izbacuje sve elemente koji se pojavljuju više puta
def izbaciDuplikate(lista):
    skup = set(lista)
    return list(skup)
def izbaciDuplikate2(lista):
    novaLista=[]
    for elem in lista:
        if(lista.count(elem)==1):
            novaLista.append(elem)
    return novaLista
lista = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
lista = izbaciDuplikate2(lista)
print(lista)

#%%
#22.	Napisati funkciju koja vraća broj jedinstvenih elemenata u listi.

def jedinstveni(lista):
    novaLista=[]
    for elem in lista:
        if(lista.count(elem)==1):
            novaLista.append(elem)
    return len(novaLista)
lista = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
resenje = jedinstveni(lista)
print(resenje)

#%%

#23.	Napisati funkciju koja kao parametar prima dve liste a I b. Funkcija vraća 1 ili 0
# u zavisnosti od toga da li je lista b podlista liste a.

def podlista(a,b):
    astring = "".join(map(str,a))
    #astring = "".join([str(element) for element in a])
    bstring = "".join([str(element) for element in b])

    if bstring in astring:
        return True  #return 1
    else:
        return False  #return 0

listaA = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
listaB = [1, 1, 2, 3, 5]
print(podlista(listaA,listaB))

#%%
#19.	Data su dva tekstualna fajla u kojima se nalaze brojevi. Napisati funkciju koja ispisuje brojeve
#       koji se pojavljuju u obe datoteke.

resenje=[]
lista1=[]
lista2=[]
# 1
# 2
# 3
# EOF
with open("datoteka1.txt") as dat1:
    linija = dat1.readline()   #"1"
    while linija:
        lista1.append(int(linija))
        linija = dat1.readline()

with open("datoteka2.txt") as dat2:
    linija = dat2.readline()   #"1"
    while linija:
        lista2.append(int(linija))
        linija = dat2.readline()

for element in lista1:
    if element in lista2:
        resenje.append(element)

print(resenje)
#%%





#%%
#24.	Napišite funkciju (povezi_po_indeksima) koja prima dve liste stringova jednake dužine
# i vraća novu listu dobijenu spajanjem ulaznih lista po indeksima, odnosno povezujući elemente
# koji se nalaze na istim pozicijama u listi. Primer:
# Ulazne liste: list1 = ["M", "na", "i", "Ke"],
#               list2 = ["y", "me", "s", "lly"]
#               Izlaz: ['My', 'name', 'is', 'Kelly']

def povezi_po_indeksima(list1, list2):
    izlaz=[]
    for i in range(0,len(list2)):
        novaRec =  list1[i]+list2[i]
        izlaz.append(novaRec)

    return izlaz


def povezi_po_indeksima2(list1, list2):
    izlaz=[]

    for i1,i2 in zip(list1,list2): # (M,y),(na,me),(i,s),(Ke,lly)
        izlaz.append(i1+i2)

    return izlaz
list1 = ["M", "na", "i", "Ke"]
list2 = ["y", "me", "s", "lly"]
izlaz = povezi_po_indeksima2(list1,list2)
print(izlaz)

#%%

#25.	Napišite funkciju (provera_lozinki) koja prihvata string koji
# sadrzi lozinke za proveru odvojene zarezom. Funkcija proverava njihovu validnost
# koristeći sledeće kriterijume:
#1. Najmanje 1 slovo između [a-z] tj. najmanje 1 malo slovo
#2. Najmanje 1 broj između [0-9] tj. najmanje 1 cifra
#3. Najmanje 1 slovo između [A-Z] tj. najmanje 1 veliko slovo
#4. Najmanje 1 od sledećih znakova: $,#,@
#5. Dužina u opsegu 6-12 (uključujući 6 i 12)
# Lozinke koje odgovaraju kriterijumima treba da budu prikazane u jednom redu odvojene zarezom.

def provera_lozinki(lozinke):  #"adsads,dsasda,dsada,dsda"
    lista = lozinke.split(",")  #["Dsadadas","dsdada","Dsdadsa"]
    novaLista=[]
    for lozinka in lista:
        uslovi = [False]*5  #False False False False False
        imaMaloSlovo=False
        imaVelikoSlovo=False
        imaCifru=False
        imaSpecKar=False
        dobraDuzina=False

        if len(lozinka)>=6 and len(lozinka)<=12:
            dobraDuzina=True  #uslovi[0]=True

        for karakter in lozinka:
            if karakter.islower():
                imaMaloSlovo=True #uslovi[1]=True
            elif karakter.isupper():
                imaVelikoSlovo=True #uslovi[2]=True
            elif karakter.isdigit():
                imaCifru=True #uslovi[3]=True
            elif karakter in ["$","#","@"]:
                imaSpecKar=True #uslovi[4]=True
        if all(uslovi):
            novaLista.append(lozinka)
        if (dobraDuzina and imaMaloSlovo and imaVelikoSlovo  and imaCifru and imaSpecKar):
            novaLista.append(lozinka)
    return novaLista

lozinke = "aaa,BBB,Baaa1$aaa,Baaa222%aaa,Baaa222%aaaaaaaaaa"
resenje = provera_lozinki(lozinke)
print(resenje)
#%%

#  26.	Napišite funkciju (stanje_servera) koja prima izveštaj (kao string) o stanju nekoliko servera.
#  Svaki red izveštaja se odnosi na jedan server i ima sledeći format: "Server<server_name> is<up/down>".
#  Obratite pažnju
#  da neki redovi mogu biti prazni. Takođe, neki serveri mogu biti pomenuti više puta, u kom slučaju,
#  najnoviji status (poslednji ispisan) bi trebalo smatrati važećim. Funkcija treba da obradi
#  izveštaj i odštampa:
#  - ukupan broj servera pomenutih u izveštaju
#  - procenat servera koji ne rade
#  - imena servera koji ne rade (ako ih ima)


def stanje_servera(izvestaj):
    lista = izvestaj.split("\n")
    ukupnoServera=0
    brojacNeRade=0
    naziviNeRade=[]
    stanjaSvihServera={}   #"s1":"down","s3":"up"
    for linija in lista:
        if linija.strip():
            deloviLinije = linija.split(" ") # ["Server","s1" "is" "up"]
            nazivServera = deloviLinije[1]
            stanjeServera = deloviLinije[3]
            stanjaSvihServera[nazivServera]=stanjeServera

    for ns,ss  in stanjaSvihServera.items():  #(s1,up), (s3,down)
        ukupnoServera = ukupnoServera+1
        if ss=="down":
            brojacNeRade=brojacNeRade+1
            naziviNeRade.append(ns)

    return ukupnoServera,brojacNeRade,naziviNeRade

izvestaj = """
Server s1 is up

Server s3 is up
Server s4 is down
Server s1 is down
"""
ukupnoServera,brojacNeRade,naziviNeRade = stanje_servera(izvestaj)

print("Ukupno servera: ",ukupnoServera)
print("Procenat servera koji ne rade: ",brojacNeRade*100/ukupnoServera)
print("Nazivi servera koji ne rade: ", naziviNeRade)
#%%
#PO KLJUCU
myDict = {'tanja': 10, 'maja': 9, 'sanja': 15, 'nikola': 2, 'aleksa': 32}
print(myDict.keys())
lista =list(myDict.keys())
lista.sort()
print(lista)
sortiranRecnik = {}
#'aleksa': 32
# 'maja': 9
for element in lista:   #['aleksa','maja'...]
    sortiranRecnik[element] = myDict[element]

soritraniRecnik2 = { element: myDict[element] for element in  lista}
# soritraniRecnik2 = { aleksa: 32 for element in  lista}

#PO VREDNOSTI
import operator
recnik = {'tanja': 10, 'maja': 9, 'sanja': 15, 'nikola': 2, 'aleksa': 32}
print(recnik.items())  # ('tanja',10),(maja,9)...
tupple= sorted(recnik.items(), key=operator.itemgetter(1))

print(tupple)
noviRecnik = {}

for kljuc,vrednost in tupple:
    noviRecnik[kljuc]=vrednost
    #noviRecnik[nikola]=2
print(noviRecnik)
#%%
#PRISTUP NEPOSTOJECEM KLJUCU
d = { 'a' : 1 , 'b' : 2 }

if 'c' in d:
    print(d['c'])
else:
    print("GRESKA")

print(d['a'])


#%%
#3.	Zbir svih elemenata rečnika
#Input : {‘a’: 100, ‘b’:200, ‘c’:300}

def zbirElemenataRecnika(recnik):
    zbir = 0
    for element in recnik:
       # print(element)
        zbir = zbir + recnik[element]
    return zbir
def zbirElemenataRecnika2(recnik):
    listaVrednosti=[]
    for element in recnik:
        listaVrednosti.append( recnik[element])

    #[100,200,300]
    return sum(listaVrednosti)
dict = {'a': 100, 'b': 200, 'c': 300}
print(zbirElemenataRecnika(dict))
#%%
studenti = [
    {'ime': 'Ana', 'ocena': 9},
    {'ime': 'Marko', 'ocena': 8},
    {'ime': 'Jovana', 'ocena': 10},
    {'ime': 'Stefan', 'ocena': 7}
]
suma = 0
brojStudentana =  len(studenti)
for student in studenti:
   # print(student)
    print( f"{student['ime']} - {student['ocena']}")
    suma += student['ocena']

prosek =  suma/brojStudentana
print(prosek)
# Ana - 9
# Marko - 8



knjige = [
    {'naslov': 'Harry Potter', 'autor': 'J.K. Rowling', 'godina': 1997},
    {'naslov': 'Lord of the Rings', 'autor': 'J.R.R. Tolkien', 'godina': 1954},
    {'naslov': 'Pride and Prejudice', 'autor': 'Jane Austen', 'godina': 1813}
]

with open("knjige.txt", "w") as knjige_file:
    for knjiga in knjige:
        knjige_file.write(f"Naslov: {knjiga['naslov']}, Autor: {knjiga['autor']},{knjiga['godina']}\n")


#%%
import operator
studenti = [
    {'ime': 'Ana', 'ocena': 9},
    {'ime': 'Marko', 'ocena': 8},
    {'ime': 'Jovana', 'ocena': 10},
    {'ime': 'Stefan', 'ocena': 7}
]
print(sorted(studenti, key=operator.itemgetter('ocena'),reverse=True))

print(sorted(studenti, key=operator.itemgetter('ime')))
#%%
#7.	Napisati funkciju koja prima celobrojnu vrednost (n) i   generiše rečnik sa unetim
# parovima u obliku x:S(x), gde je x  broj između 1 i n, a S(x) = 1 + 2 + ... + x.
# Funkcija takođe ispisuje rečnik u opadajućem redosledu ključeva,
# na sledeći način (za n=5):
# 5: 1+2+3+4+5=15
# 4: 1+2+3+4=10
# 3: 1+2+3=6
# 2: 1+2=3
# 1: 1=1
def generisi_recnik(n):
    recnik = {}  # recnik = dict()
    for kljuc in range(n,0,-1):
        vrednost =  sum(range(1,kljuc+1))
        recnik[kljuc] =vrednost
        sumaString = "+".join([str(i) for i in range(1,kljuc+1)])
        print(f"{kljuc}:{sumaString}={vrednost}")

    print(recnik)

n = 5
generisi_recnik(n)



#%%
#8.	Napisati funkciju koja kreira rečnik iz dve date liste, tako što elementi prve
# liste postaju ključevi, dok odgovarajući elementi druge liste postaju vrednosti.
# Ispisati rečnik sortiran na osnovu vrednosti elemenata. (savet: koristiti funkciju itemgetter()
# iz modula operator) Primer: lista zemalja i lista nacionalnih jela tih zemalja treba da
# se pretvori u rečnik gde su ključevi imena zemalja, a vrednosti odgovarajuća jela.


from itertools import zip_longest
import operator
def spojiDveListeURecnik(kljucevi,vrednosti):
    recnik = {} #dict()
    for kljuc,vrednost in zip_longest(kljucevi,vrednosti,fillvalue="NA"):
        recnik[kljuc]=vrednost

    print(recnik)
    sortiraniRecnik =  dict(sorted(recnik.items(), key=operator.itemgetter(1)))
    print(sortiraniRecnik)

zemlje = ['Italija', 'Francuska', 'Španija', 'Grčka','Srbija']
jela = ['Pizza', 'Baguette', 'Paella', 'Moussaka']
spojiDveListeURecnik(zemlje, jela)





#%%

#9.	Napisati funkciju koja prima string kao ulazni parametar i računa broj cifara,
# slova i znakova interpunkcije (.,!?;:) u datom stringu. Funkcija vraća rečnik sa izračunatim vrednostima.

#das487778.!

#{cifre:5,slova:20,znaci:5}
def stringRecnik1(string):
    brojacCifre=0
    brojacSlova=0
    brojacZnaci=0

    for karakter in string:
        if karakter.isalpha():
            brojacSlova+=1;
        elif karakter.isdigit():
            brojacCifre+=1;
        elif karakter in ('.,!?;:'):
            brojacZnaci+=1;

    recnik = {}
    recnik["slova"]=brojacSlova
    recnik["cifre"]=brojacCifre
    recnik["znaci"]=brojacZnaci

from collections import defaultdict
def stringRecnik2(string):
    recnik = defaultdict(int)

    for karakter in string:
        if karakter.isalpha():
            recnik["slova"]+=1;
        elif karakter.isdigit():
            recnik["cifre"]+=1;
        elif karakter in ('.,!?;:'):
            recnik["znaci"]+=1;
    return recnik
string = "sdasd:.784"
print(stringRecnik2(string))






#%%
#10.	Napisati funkciju koja prima listu web adresa (URL) različitih organizacija.
# Izračunati broj adresa za svaki sufiks (npr., com, org, net) prisutan u listi.
# Kreirati i vratiti rečnik sa izračunatim vrednostima (ključevi su sufiksi web adresa, vrednosti
# su odgovarajući brojevi).
from collections import defaultdict
def sufiksiULRRecnik(adrese):
    recnik=defaultdict(int)
    #www.vanjavizicasovi.com
    for adresa in adrese:
        #print(adresa.split(".")[-1])
        recnik[adresa.split(".")[-1]]+=1

    print(recnik)
adrese = ['www.example.com', 'www.organization.org', 'www.test.net', 'www.example2.com']
sufiksiULRRecnik(adrese)



from collections import Counter
def sufiksiULRRecnik2(adrese):
    sufiksi = [ adresa.split(".")[-1] for adresa in adrese ]
    print(sufiksi)
    brojaci = Counter(sufiksi)
    print(brojaci)
    recnik = dict(brojaci)
    print(recnik)
adrese = ['www.example.com', 'www.organization.org', 'www.test.net', 'www.example2.com']
sufiksiULRRecnik2(adrese)


def sufiksiULRRecnik3(urls):
    d = defaultdict(int)
    for url in urls:
        #          www.fon.bg.ac.rs
        _, suffix = url.rsplit(".",maxsplit=1)
        suffix = suffix.rstrip('/')
        d[suffix] += 1
    return dict(d)




#%%

# 11.	Napisati funkciju koja prima deo teksta i računa frekvenciju tokena u tekstu
# (podrazumeva se da je token niz uzastopnih karaktera (string) između dva razmaka).
# Izračunati frekvenciju tokena na način neosetljiv na velika i mala slova. Tokeni i
# njihove frekvencije treba sačuvati u rečniku (tokeni kao ključevi, frekvencije kao
# vrednosti). Funkcija ispisuje rezultujući rečnik nakon što sortira tokene alfabetski.
from collections import defaultdict
import operator
def funkcijaRecnikTokeni(string):
    d = defaultdict(int)
    tokens = string.lower().split(" ") #[ovo,je,neki,test, tekst, test, test]
    for token in tokens:
        d[token] += 1
        #d['je'] += 1
    for tok, freq in sorted(d.items()):
        print(f"{tok}:{freq}")

tekst = "Ovo je neki TEST tekst test TEST"
funkcijaRecnikTokeni(tekst)

#%%



from collections import Counter

def funkcijaRecnikTokeni2(string):
    tokens = string.lower().split() #[ovo,je,neki,test, tekst, test, test]
    counter = Counter(tokens)
    print(counter)
    # Sortiranje rečnika po ključevima u rastućem abecednom redosledu
    for tok, freq in sorted(d.items()):
        print(f"{tok}:{freq}")

tekst = "Ovo je neki TEST tekst test TEST"
print(funkcijaRecnikTokeni2(tekst))
#%%
# Nakon testiranja funkcije, izmeniti je tako da:
# - tokeni budu očišćeni od bilo kakvih suvišnih karaktera (npr. razmaci ili interpunkcijski znaci)
#           pre dodavanja u rečnik
# - samo tokeni sa najmanje 3 karaktera su dodati u rečnik
# - pre ispisa, unosi u rečnik su sortirani: prvo u opadajućem redosledu frekvencije tokena,
#       a zatim u rastućem abecednom redosledu
from collections import defaultdict
import operator
def funkcijaRecnikTokeni3(string):
    d = defaultdict(int)
    tokens = string.lower().split(" ")
    for token in tokens:
        token=token.strip(',.?!:; ')
        if(len(token)>=3):
            d[token] += 1

    for tok, freq in sorted(sorted(d.items()),key=operator.itemgetter(1), reverse =  True):
        print(f"{tok}:{freq}")


tekst = "Ovo je neki TEST tekst test TEST"
print(funkcijaRecnikTokeni3(tekst))





#%%
#  12.	Napisati funkciju koja prima sekvencu lozinki odvojenih zarezima i proverava
#  njihovu validnost koristeći sledeće kriterijume:
#  1. Najmanje 1 slovo između [a-z] => Najmanje 1 malo slovo
#  2. Najmanje 1 broj između [0-9] => Najmanje 1 cifra
#  3. Najmanje 1 slovo između [A-Z] => Najmanje 1 veliko slovo
#  4. Najmanje 1 od ovih znakova: $,#,@
#  5. Dužina u rasponu 6-12 (uključujući 6 i 12)
#Funkcija kreira i vraća rečnik sa proverenim lozinkama kao ključevima,
# gde vrednost ključa treba da bude lista sa: - jednim elementom "Ispravna lozinka",
# ako se odgovarajuća lozinka pokazala validnom - identifikovanim problemima, ako lozinka
# nije validna
def password_check(lozinke):
    d = dict()
    for p in [p.lstrip() for p in lozinke.split(',')]: #["Abcd@1234" , a#b2C6, XYZ@123, password1, passw0rd123]
        problemi = []
        if not any([ch.islower() for ch in p]): #[FALSE,TRUE...]
            problemi.append("no lower case letters")
        if not any([ch.isdigit() for ch in p]):  #[FALSE FALSE FALSE... TRUE]
            problemi.append("no digits")
        if not any([ch.isupper() for ch in p]):
            problemi.append("no upper case letters")
        if not any([ch in '$#@' for ch in p]):
            problemi.append("no special characters '@#$'")
        if len(p) < 6 or len(p) > 12:
            problemi.append("length should be in the [6,12] range")
        d[p] = ['Ispravna lozinka'] if len(problemi) == 0 else problemi
        # if len(problemi) == 0:
        #     d[p] = ['Ispravna lozinka']
        # elif
        #     d[p] = problemi
    return d


lozinke = "Abcd@1234 , a#b2C6, XYZ@123, password1, passw0rd123"
print(password_check(lozinke))




#%%
# 13.	Napisati funkciju koja kao ulaz prima listu rečnika sa podacima o članovima sportskog tima.
# Svaki rečnik sadrži sledeće podatke o jednom članu tima: ime, godine i takmičarski rezultat (0-100).
# Na primer: {ime:Bob, godine:19, rezultat:55.5} Funkcija računa i ispisuje sledeće statistike:
# - prosečne (srednje) godine članova tima
# - ime igrača sa najnižim rezultatom među onima mlađim od 21 godine
# - ime igrača sa najvišim rezultatom među onima mlađim od 21 godine
# Na kraju, funkcija ispisuje listu članova sortiranu po rezultatima članova(od najvišeg do najnižeg).
# Savet: modul 'statistics' pruža funkcije za potrebne statistike


from statistics import mean, quantiles
def team_stats(team_data):

    godine= [member['godine'] for member in team_data]
    print(godine)  #[ 19,25,20,22]
    mean_age = mean(godine)
    print(f"Average age of team members: {mean_age}")

    clanoviUnder21 = [member for member in team_data if member['godine'] < 21]
    worst_under21 = min(clanoviUnder21, key=itemgetter('rezultat'))
    print(f"Worst player under 21 is {worst_under21['ime']}")

    best_under21 = max(clanoviUnder21, key=itemgetter('rezultat'))
    print(f"Best player under 21 is {best_under21['ime']}")

lista_clanova = [
    {'ime': 'Bob', 'godine': 19, 'rezultat': 55.5},
    {'ime': 'Alice', 'godine': 25, 'rezultat': 70.8},
    {'ime': 'Charlie', 'godine': 20, 'rezultat': 60.2},
    {'ime': 'David', 'godine': 22, 'rezultat': 80.1}
]
# Poziv funkcije za izračunavanje i ispisivanje statistika
team_stats(lista_clanova)








#map(fja,lista), filter(fja,lista), reduce
#lambda izrazi
#%%
def kvadrat(x):
    return x ** 2

brojevi = [1, 2, 3, 4, 5]
kvadrati = map(kvadrat, brojevi)
print(list(kvadrati))  # Output: [1, 4, 9, 16, 25]

#%%
def je_paran(x):
    return x % 2 == 0

brojevi = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
parni = filter(je_paran, brojevi)
print(list(parni))  # Output: [2, 4, 6, 8, 10]
#%%

from functools import reduce

def saberi(x, y):
    return x + y

brojevi = [1, 2, 3, 4, 5]
suma = reduce(saberi, brojevi)
print(suma)  # Output: 15

#%%
# Recnik + Filter
def veci_od_5(item):
    return item[1] > 5

recnik = {'a': 3, 'b': 7, 'c': 2, 'd': 8}
filtrirani_recnik = dict(filter(veci_od_5, recnik.items()))  #[(a,3),(b,7)..]
print(filtrirani_recnik)  # Output: {'b': 7, 'd': 8}

#%%

# Recnik + Map
def udvostruci(item):
    return (item[0], item[1] * 2)

recnik = {'a': 3, 'b': 7, 'c': 2, 'd': 8}
udvostruceni_recnik = dict(map(udvostruci, recnik.items()))
print(udvostruceni_recnik)  # Output: {'a': 6, 'b': 14, 'c': 4, 'd': 16}
#%%
# Recnik + Reduce
from functools import reduce

def saberi(acc, item):
    return acc + item[1]

recnik = {'a': 3, 'b': 7, 'c': 2, 'd': 8}
suma_vrednosti = reduce(saberi, recnik.items(), 0)
print(suma_vrednosti)  # Output: 20


#%%
add = lambda x, y: x + y
print(add(3, 5))  # Output: 8

multiply = lambda x, y: x * y
print(multiply(4, 6))  # Output: 24

is_even = lambda x: x % 2 == 0  #False
print(is_even(7))  # Output: False
print(is_even(8))  # Output: True

#%%
words = ["apple", "banana", "cherry", "date"]
sorted_words = sorted(words, key=lambda x: len(x))
print(sorted_words)  # Output: ['date', 'apple', 'banana', 'cherry']

def duzina_reci(rec):
    return len(rec)

words = ["apple", "banana", "cherry", "date"]
sorted_words = sorted(words, key=duzina_reci)
print(sorted_words)  # Output: ['date', 'apple', 'banana', 'cherry']



#%%
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
even_numbers = list(filter(lambda x: x % 2 == 0, numbers))
print(even_numbers)  # Output: [2, 4, 6, 8, 10]

numbers = [1, 2, 3, 4, 5]
squared_numbers = list(map(lambda x: x**2, numbers))
print(squared_numbers)  # Output: [1, 4, 9, 16, 25]


from functools import reduce
numbers = [1, 2, 3, 4, 5]
sum_of_numbers = reduce(lambda x, y: x + y, numbers)
print(sum_of_numbers)  # Output: 15

#%%
students = {
    1: {'name': 'John', 'age': 21},
    2: {'name': 'Emma', 'age': 19},
    3: {'name': 'Alex', 'age': 22},
    4: {'name': 'Sophia', 'age': 20}
}
# (1,{'name': 'John', 'age': 21},)
# ( 2, {'name': 'Emma', 'age': 19},)
#
# Filtriranje studenata mlađih od 21 godine
young_students = dict(filter(lambda item: item[1]['age'] < 21, students.items()))
print(young_students)

# Mapiranje imena studenata na velika slova
uppercased_names = dict(map(lambda item: (  item[0], item[1]['name'].upper()  ), students.items()))
print(uppercased_names)

from functools import reduce
# Reduce funkcija za računanje ukupnog broja studenata
total_students = reduce(lambda acc, item: acc + 1, students.items(), 0)
print(total_students)
#%%




#%%
#7.	Napišite funkciju 'compute_product' koja prima proizvoljan broj numeričkih vrednosti i
# izračunava njihov proizvod.Funkcija takođe prima imenovani argument "squared" sa podrazumevanom
# vrednošću False, koji određuje da li treba koristiti date numeričke vrednosti kakve jesu ili
# njihove kvadrate. Izračunati proizvod je povratna vrednost funkcije. Implementirajte funkciju
# na dva različita načina:
# 1) koristeći for petlju
# 2) koristeći funkciju reduce() iz modula functools zajedno sa odgovarajućom lambda funkcijom.

from functools import reduce
def compute_product1(*brojevi, squared=False):
    resenje = 1
    for broj in brojevi:
        #resenje *=  broj if not squared else broj**2
        if squared:
            resenje *= broj ** 2
        else:
            resenje *= broj
    return resenje

def compute_product2(*brojevi, squared=False):
    if squared:
        squared_numbers = map(lambda x: x ** 2, brojevi)
        return reduce(lambda x, y: x * y, squared_numbers, 1)
    else:
        return reduce(lambda x, y: x * y, brojevi, 1)

    # return reduce(lambda x,y: x*y, [broj**2 if squared else broj for broj in brojevi]   )

result1 = compute_product1(2, 3, 4,squared=True)
print(result1)
result2 = compute_product2(2, 3, 4)
print(result2)
#%%

#8.	Napišite funkciju 'select_strings' koja prima proizvoljan broj stringova i vraća listu
# strigova koji imaju isto prvo i poslednje slovo (nezavisno od veličine slova) i ukupan broj
# jedinstvenih karaktera je veći od datog praga. Prag je imenovani argument funkcije sa
# podrazumevanom vrednošću 3. Implementirajte funkciju na tri različita načina:
# 1) koristeći for petlju
# 2) koristeći list comprehension
# 3) koristeći funkciju filter() zajedno sa odgovarajućom lambda funkcijom.

def select_strings1(*strings, prag=3):
    selected = []
    for s in strings:
        #s=s.lower();
        if s[0].lower() == s[-1].lower() and len(set(s.lower())) > prag:
            selected.append(s)
    return selected

def select_strings2(*strings, prag=3):
    return [s for s in strings if s[0].lower() == s[-1].lower() and len(set(s.lower())) > prag]

def select_strings3(*strings, prag=3):
    return list(filter(lambda s:s[0].lower() == s[-1].lower() and len(set(s.lower())) > prag, strings))


# Primer poziva funkcija sa argumentima
result1 = select_strings1("apple", "banana", "Civic", "date", prag=2)
print(result1)

result2 = select_strings2("apple", "banana", "Civic", "date")
print(result2)

result3 = select_strings3("apple", "banana", "Civic", "date", prag=2)
print(result3)

#%%

#9.	Napišite funkciju 'process_product_orders' koja prima listu porudžbina proizvoda, gde je svaka porudžbina
# 4-tuple oblika (order_id, product_name, quantity, price_per_item). Funkcija vraća rečnik sa elementima oblika
# <order_id: total_price> , gde je ukupna cena za porudžbinu proizvod količine i cene po stavci.
# Funkcija takođe prima dva imenovana  argumenta koja mogu uticati na izračunatu ukupnu cenu:
# - popust - popust, izražen u procentima, koji se primenjuje na ukupnu cenu;
#       podrazumevana vrednost ovog argumenta je None
# - troškovi dostave - troškovi dostave koji se dodaju na porudžbine sa ukupnom cenom manjom od 100;
#       podrazumevana vrednost ovog argumenta je 10. Implementirajte funkciju na tri različita načina:
#   1) koristeći for petlju
#  2) koristeći dictionary comprehension
#   3) koristeći funkciju map() zajedno sa odgovarajućom pomoćnom funkcijom

def process_product_orders1(orders, discount=None, shipping=10):
    def compute_total_price(quantity, price_per_item):
        tot_price = quantity * price_per_item
        tot_price *= (100-discount)/100 if discount else 1
        tot_price += shipping if tot_price<100 else 0
        return tot_price
    processed_orders = []
    for order_id, _, quantity, price_per_item in orders:
        tot_price = compute_total_price(quantity, price_per_item)
        processed_orders.append((order_id, tot_price))
    return dict(processed_orders)
def process_product_orders2(orders, discount=None, shipping=10):
    def compute_total_price(quantity, price_per_item):
        tot_price = quantity * price_per_item
        tot_price *= (100-discount)/100 if discount else 1
        tot_price += shipping if tot_price<100 else 0
        return tot_price

    return {order_id: compute_total_price(quantity, price_per_item) for order_id, _, quantity, price_per_item in orders}

def process_product_orders3(orders, discount=None, shipping=10):
    def compute_total_price(quantity, price_per_item):
        tot_price = quantity * price_per_item
        tot_price *= (100-discount)/100 if discount else 1
        tot_price += shipping if tot_price<100 else 0
        return tot_price

    return dict(map(lambda order: (order[0], compute_total_price(order[2], order[3])), orders))

orders = [
    (1, "Mleko", 2, 50),
    (2, "Hleb", 3, 30),
    (3, "Jaja", 1, 20),
    (4, "Sir", 1, 150)
]

print("Rezultat procesiranja porudžbina metodom 1:")
print(process_product_orders1(orders))
print("\nRezultat procesiranja porudžbina metodom 2:")
print(process_product_orders2(orders))
print("\nRezultat procesiranja porudžbina metodom 3:")
print(process_product_orders3(orders))

#%%





#%%





#%%





#%%





#%%





#%%





#%%





#%%




#%%