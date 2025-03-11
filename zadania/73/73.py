with open("C:/Users/bar.nowosad/Desktop/visual/zadania/73/tekst.txt", "r") as plik:
    tekst = plik.readline()
lista_napisow = tekst.split()

licznik = 0
for napis in lista_napisow:
    for i in range(len(napis)-1):
        if napis[i] == napis[i + 1]:
            licznik += 1
            break
print(licznik)

slownik = {}

for znak in tekst:
    if znak != " " and znak != "\n":
        if znak in slownik:
            slownik[znak] += 1
        else:
            slownik[znak] = 1
print(sorted(slownik.items()))
suma = sum(slownik.values())
print(suma)
for kr in sorted(slownik.items()):
    print(kr[0],":", kr[1], round(100*kr[1]/suma,2),"%")

samogloski = "AEIOUY"
maks = 0
for slowo in lista_napisow:
    n = 0
    for litera in slowo:
        if litera not in samogloski:
            n += 1
            if n > maks:
                maks = n
        else:
            n = 0
print(maks)