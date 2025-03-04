def ile_takich_samych_znakow_z_prawej_strony_dwoch_napisow(napis1, napis2):
    ile = 0
    if len(napis1) >= len(napis2):
        for i in range(len(napis2)):
            if napis2[-1-i] != napis1[-1-i]:
                return ile
            ile += 1
        return ile
    else:
        for i in range(len(napis1)):
            if napis2[-1-i] != napis1[-1-i]:
                return ile
            ile += 1
        return ile

lista_napisow = []
with open("C:/Users/bar.nowosad/Desktop/visual/zadania/72/napisy.txt", "r") as plik:
    for linia in plik:
        lista_napisow.append(linia.split())
print(lista_napisow)
licznik = 0
for napisy in lista_napisow:
    if len(napisy[0]) >= 3*len(napisy[1]) or len(napisy[1]) >= 3*len(napisy[0]):
        if licznik < 1:
            print(napisy)
        licznik += 1
print(licznik)
for napisy in lista_napisow:
    if napisy[0] == napisy[1][:len(napisy[0])]:
        print(napisy, napisy[1][len(napisy[0]):])

maks = 0
lista = []
for napisy in lista_napisow:
    k = ile_takich_samych_znakow_z_prawej_strony_dwoch_napisow(napisy[0], napisy[1])
    if k > maks:
        maks = k
        lista = []
        lista.append(napisy)
    if k == maks:
        lista.append(napisy)
print(maks, lista)