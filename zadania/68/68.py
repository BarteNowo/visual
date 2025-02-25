lista_napisow = []
with open("C:/Users/bar.nowosad/Desktop/visual/zadania/68/dane_napisy.txt") as plik:
    for linia in plik:
        lista_napisow.append(linia.split())
print(lista_napisow)