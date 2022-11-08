#tässä sai jo tutustua uuteen aiheeseen. Hash-tarkistusluvut on itselle vielä vieraita, mutta
#onneksi googlesta löytyi selkeä ohje mistä kyse
import hashlib

i=0
result = ''
while True:
  str2hash = "abcdef"+str(i)
  encoded = str2hash.encode()
  md5 = hashlib.md5(encoded)
  result = md5.hexdigest
  result = str(result)  
  i += 1

print(i)
