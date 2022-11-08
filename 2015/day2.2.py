#haetaan tiedot
file1 = open(r"c:\Users\FB1091\AdventOfCode\2015\day2.txt", "r+")
#luetaan listaksi
list = file1.readlines()
#käydään koko lista läpi
total = 0
for x in list:
  #solu kerrallaan stringeinä, manipuloidaan joka mitta erikseen stringistä(x-erottimena)
  dim = x.split("x")
  #muutetaan stringit inteiksi
  l = int(dim[0])
  w = int(dim[1])
  h = int(dim[2])
  #etsitään pienin (luodaan inteistä uusi lista, sortataan ja sit käytetään 2 pienintä)
  newdim = [l, w, h]
  newdim.sort()
  #lasketaan pituus ja rusetti
  length = 2* newdim[0]+2*newdim[1]
  bow = l*w*h
  #lasketaan kokonaistsyteemi 
  total += length + bow
print (total)

