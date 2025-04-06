def szyfruj_przestawieniowo(tekst, klucz):
    tekst = list(tekst)
    n = len(klucz)
    for i in range(len(tekst)):
        poz_klucza = i % n
        poz_w_tekscie = klucz[poz_klucza] - 1
        if poz_w_tekscie < len(tekst):
            tekst[i], tekst[poz_w_tekscie] = tekst[poz_w_tekscie], tekst[i]
    
    return ''.join(tekst)

tekst = "maturainformatykaalgorytmystrukturydanychzlozonosc"
klucz = [13, 10, 2, 3, 1, 12, 8, 4, 5, 7, 9, 6, 15, 14, 11]
zaszyfrowane = szyfruj_przestawieniowo(tekst, klucz)
print(f"Zaszyfrowane: {zaszyfrowane}")

def deszyfruj_przestawieniowo(zaszyfrowany, klucz):
    tekst = list(zaszyfrowany)
    n = len(klucz)
    for i in range(len(tekst) - 1, -1, -1):
        poz_klucza = i % n
        poz_w_tekscie = klucz[poz_klucza] - 1
        if poz_w_tekscie < len(tekst):
            tekst[i], tekst[poz_w_tekscie] = tekst[poz_w_tekscie], tekst[i]
    return ''.join(tekst)

zaszyfrowane = "rmtauanszoocolzhcynadyrutkurtsymtyroglaakytamrofni"
klucz = [6, 2, 4, 1, 5, 3]
odszyfrowane = deszyfruj_przestawieniowo(zaszyfrowane, klucz)
print(f"Odszyfrowane: {odszyfrowane}")