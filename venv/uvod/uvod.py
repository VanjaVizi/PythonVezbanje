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


#27.	Napišite funkciju (rotiraj_niz) koja prima niz celih brojeva i broj m, i rotira niz za
# m mesta udesno. Na primer, ako je niz [1, 2, 3, 4, 5] i m = 2, rezultat treba da bude
# [4, 5, 1, 2, 3].








