ciagi = []
with open('C:\\Users\\DELL\\Documents\\GitHub\\informatyka-\\zadanie cke\\ciagi.txt') as plik:
    for linia in plik:
        liczby = []
        for liczba in linia.split():
            liczby.append(int(liczba))
        if len(liczby) > 1:
            ciagi.append(liczby)
print(ciagi)
licznik = 0
maks = 0
for ciag in ciagi:
    roznica = ciag[1]-ciag[0]
    for i in range(1, len(ciag)):
        if roznica != ciag[i]-ciag[i-1]:
            break
    else:
        licznik += 1
        if roznica > maks:
            maks = roznica
print(licznik,maks)
