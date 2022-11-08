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
  #lasketaan itse paketin koko
  size = 2*l*w + 2*w*h + 2*h*l
  #etsitään pienin
  if l*w < w*h and l*w<l*h:
    smallest = l*w
  elif l*h < w*h:
    smallest = l*h
  else: 
    smallest = w*h
  #lasketaan kokonaistsyteemi 
  total += size + smallest
print (total)

