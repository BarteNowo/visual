def szyfruj(napis, a, b):
    zaszyfrowany = ""
    for znak in napis:
        askii = ord(znak) - 97
        askii = askii * a + b
        askii %= 26
        znakS = chr(askii + 97)
        zaszyfrowany += znakS
    return zaszyfrowany


with open("C:/Users/bar.nowosad/Desktop/visual/zadania/75/tekst.txt") as plik:
    tekst = plik.readline()

print(tekst)
wyrazy = tekst.split()

for wyraz in wyrazy:
    if wyraz[0] == "d" and wyraz[-1] == "d":
        print(wyraz)

for wyraz in wyrazy:
    if len(wyraz) >= 10:
        print(szyfruj(wyraz, 5, 2))

with open("C:/Users/bar.nowosad/Desktop/visual/zadania/75/probka.txt") as plik:
    for linia in plik:
        napisy = linia.split()
        for a in range(26):
            for b in range(26):
                if szyfruj(napisy[0], a, b) == napisy[1]:
                    print(napisy, a, b)
                    break
                    
# print(ord("a")-97)
# print(ord("z")-97)
# print(chr(22+97))