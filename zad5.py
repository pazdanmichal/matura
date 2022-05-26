plik = open("soki.txt")
dane = plik.read().split('\n')
import datetime
from traceback import print_tb
del dane[-1]
del dane[0]

magazyny = []

for i in range(0, len(dane)):
    magazyn = dane[i].split('\t')[-2]
    bylo = False
    for j in range (0, len(magazyny)):
        if magazyny[j][0] == magazyn:
            bylo = True
            magazyny[j][1] += 1
            magazyny[j][2] += int(dane[i].split('\t')[-1])
    if not bylo:
        magazyny.append([magazyn,1, int(dane[i].split('\t')[-1])])

for i in range(0, len(magazyny)):
    print(magazyny[i][0]+" "+str(magazyny[i][1]))


print("---")

pocz = datetime.date(2021,1,2)
BigPocz = pocz
BigKon = pocz
dzien = datetime.timedelta(1)
seria = 1
for i in range(3, len(dane)):
    magazyn = dane[i].split('\t')[-2]
    data = dane[i].split('\t')[1].split(".")
    if magazyn == "Ogrodzieniec":
        DataTeraz = datetime.date(int(data[2]),int(data[1]), int(data[0]))

        if DataTeraz == pocz+dzien:
            pocz = DataTeraz
            seria += 1
            BigKon = pocz
        else:

            if seria == 8:
                print(8)
                print(BigPocz,BigKon)
            pocz = DataTeraz
            BigPocz = pocz
            seria = 1
print("---")
mag = []
ilosci = []
for i in range(0, len(magazyny)):
    print(magazyny[i][0],magazyny[i][2])
print("wykres masz Pan w pdfie")
print("---")

glowny = 30000
filiaBoost = 0
filiaIlosc = 0
dodaj = 12000
pocz = datetime.date(2021,1,2)
for i in range(0, len(dane)):
    ilosc = int(dane[i].split('\t')[-1])
    data = dane[i].split('\t')[1].split(".")
    DataTeraz = datetime.date(int(data[2]),int(data[1]), int(data[0]))
    if DataTeraz == pocz + dzien:
        pocz = DataTeraz
        if DataTeraz.isoweekday() == 6 or DataTeraz.isoweekday() == 7:
            glowny += 5000
        else:
            glowny += dodaj
    if glowny >= ilosc:
        glowny -= ilosc
    else:
        filiaBoost += ilosc
        filiaIlosc += 1
print(filiaIlosc,filiaBoost)
print('---')


glowny = 30000
filiaBoost = 0
filiaIlosc = 0
dodaj = 13200
pocz = datetime.date(2021,1,2)
for i in range(0, len(dane)):
    ilosc = int(dane[i].split('\t')[-1])
    data = dane[i].split('\t')[1].split(".")
    DataTeraz = datetime.date(int(data[2]),int(data[1]), int(data[0]))
    if DataTeraz == pocz + dzien:
        pocz = DataTeraz
        if DataTeraz.isoweekday() == 6 or DataTeraz.isoweekday() == 7:
            glowny += 5000
        else:
            glowny += dodaj
    if glowny >= ilosc:
        glowny -= ilosc
    else:
        filiaBoost += ilosc
        filiaIlosc += 1
#print(filiaIlosc,filiaBoost)
#print('---')
print(13200)

