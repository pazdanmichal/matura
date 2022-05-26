

plik = open('liczby.txt')
dane = plik.read().split()
for i in range(0, len(dane)):
    dane[i] = int(dane[i])
def sprawdzCzynniki(liczba):
    czyn = []
    for i in range(2,liczba+1):
        while liczba%i == 0:
            liczba /= i
            czyn.append(i)

    tab = list(dict.fromkeys(czyn))
    return [len(czyn), len(tab)]
    
def czyDobra3(x,y,z):
    if y%x == 0 and z%y == 0 and x!=y and x!=z and y!=z:
        return True
    return False
    
def czyDobra5(u,w,x,y,z):
    aaa = [u,w,x,y,z]
    if len(aaa) == len(list(dict.fromkeys(aaa))):
        return True
    return False



liczby = 0
was = False
for i in range (0, len(dane)):
    if str(dane[i])[0] == str(dane[i])[-1]:
        liczby += 1
        if not was:
            was = True
            print(dane[i])
print(liczby)

najw = 0
a = 0
najw2 = 0
a2 = 0
for i in range (0, len(dane)):
    lista = sprawdzCzynniki(dane[i])
    if lista[0] > najw:
        najw = lista[0]
        a = dane[i]
    if lista[1] > najw2:
        najw2 = lista[1]
        a2 = dane[i]
print(najw,a,najw2,a2)

dobre3 = 0
for i in range (0, len(dane)):
    for j in range (0, len(dane)):
        for k in range (0, len(dane)):
            if i!=j and j!=k and i!=k:
                if czyDobra3(dane[i],dane[j],dane[k]):
                    dobre3 += 1
print(dobre3)

dobre5 = 0
for i in range (0, len(dane)):
    for j in range (0, len(dane)):
        if dane[j]>dane[i] and dane[j]%dane[i] ==0:
            for k in range (0, len(dane)):
                if dane[k]>dane[j] and dane[k]%dane[j] == 0:
                    for p in range(0, len(dane)):
                        if dane[p]>dane[k] and dane[p]%dane[k] == 0:
                            for q in range(0, len(dane)):
                                if dane[q]>dane[p] and dane[q]%dane[p] == 0:
                                    dobre5 += 1
print(dobre5)

    
