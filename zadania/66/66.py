def suma_cyfr(liczba):
    suma = 0
    for cyfra in liczba:
        suma += int(cyfra)
    return suma

def pierwsza(liczba): #dostanie int
    if liczba < 2:
        return False
    if liczba == 2:
        return True
    if liczba % 2 == 0:
        return False
    for i in range(3, int(liczba**0.5)+1, 2):
        if liczba % i == 0:
            return False
    return True

def czy_prostokatny(a, b, c):
    boki = sorted([a, b, c])
    return boki[0]**2 + boki[1]**2 == boki[2]**2

def czy_trojkat(a, b, c):
    boki = sorted([a, b, c])
    return boki[0] + boki[1] > boki[2]
        
lista_trojek = []
with open("C:/Users/bar.nowosad/Desktop/visual/zadania/66/trojki.txt") as plik:
    for linia in plik:
        lista_trojek.append(linia.split())

for liczby in lista_trojek:
    if suma_cyfr(liczby[0]) + suma_cyfr(liczby[1]) == int(liczby[2]):
        print(liczby)

for liczby in lista_trojek:
    if int(liczby[0]) * int(liczby[1]) == int(liczby[2]):
        if pierwsza(int(liczby[0])) and pierwsza(int(liczby[1])):
            print(liczby)

    for i in range(len(lista_trojek) - 1):
        wiersz1 = lista_trojek[i]
        wiersz2 = lista_trojek[i + 1]

    liczby = [int(wiersz1[0]), int(wiersz1[1]), int(wiersz1[2]), 
              int(wiersz2[0]), int(wiersz2[1]), int(wiersz2[2])]
    
    for j in range(len(liczby) - 2):
        for k in range(j + 1, len(liczby) - 1):
            for l in range(k + 1, len(liczby)):
                a, b, c = liczby[j], liczby[k], liczby[l]
                if czy_prostokatny(a, b, c):
                    print(f"{i+1} i {i+2}: {wiersz1} oraz {wiersz2}")

    licznik_trojkatow = 0

for liczby in lista_trojek:
    a, b, c = int(liczby[0]), int(liczby[1]), int(liczby[2])
    if czy_trojkat(a, b, c):
        licznik_trojkatow += 1

print(f"wiersze z dlugoscia bokow trojkata: {licznik_trojkatow}")

najdluzszy_ciag = 0
aktualny_ciag = 0

for liczby in lista_trojek:
    a, b, c = int(liczby[0]), int(liczby[1]), int(liczby[2])
    if czy_trojkat(a, b, c):
        aktualny_ciag += 1
        if aktualny_ciag > najdluzszy_ciag:
            najdluzszy_ciag = aktualny_ciag
    else:
        aktualny_ciag = 0

print(f"dlugosc najdluzszego ciągu: {najdluzszy_ciag}")
