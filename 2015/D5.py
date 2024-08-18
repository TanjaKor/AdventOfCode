#avataan luettavaksi file missä stringit ja importataan groupby
#tuplien etsimiseen
from itertools import groupby
file1 = open("file.txt", "r")
#luetaan stringit filestä (lista stringejä)
strings = file1.readlines() 
count = 0
#mapataan listan stringit listoiksi, jotta helpompi käsitellä
stringl = list(map(list,strings))
for string in stringl:
    #vokaalit ja kielletyt omiin listoihinsa
    vowels = ['a','e','i','o','u']
    forbidden = ['ab', 'cd', 'pq', 'xy']
    #apumuuttuja vokaalien laskemiseen
    isvowel = 0
    #etsitään vokaalit
    for i in string:
        if i in vowels:
            isvowel = isvowel + 1
        #jos on kolme tai enemmän mennään ifin kautta muut ehdot
    if (isvowel > 2):
    #etsitään tuplat
    #groupby jakaa stringin ryhmiin, joissa on vain samoja merkkejä
    #for loop käy läpi kaikki groupbyn luomat ryhmät
    #ja leng tarkistaa miten pitkät nuo ryhmät on (eli kuinka monta samaa merkkiä)
        isdouble = [len(list(j)) for _, j in groupby(string)]
        if (max(isdouble) > 1):
        #etsitään kielletyt stringit
            a = ''.join(map(str, string))
            if not any(h in a for h in forbidden):
                count = count + 1
print(count)
file1.close()
