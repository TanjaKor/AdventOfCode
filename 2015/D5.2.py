#It contains a pair of any two letters that appears at least twice in the string without overlapping, 
# like xyxy (xy) or aabcdefgaa (aa), but not like aaa (aa, but it overlaps).
#It contains at least one letter which repeats with exactly one letter between them, 
# like xyx, abcdefeghi (efe), or even aaa.

#käytetään regexiä
import re
#avataan matskut
file1 = open("file.txt", "r")
#luetaan stringit filestä (lista stringejä)
strings = file1.readlines() 
#testi strings = ["abcccc","oigiigh","psdig","qjhvhtzxzqqjkmpb"]
#kivat stringit tänne
count = 0
#käydään läpi yksittäinen string listasta
for i, string in enumerate(strings):
    #tarkistetaan löytyykö mitä tahansa kahden kirjaimen yhdistelmää, mikä toistuu
    if re.search(r'([a-z]{2}).*\1', string) is not None:
        #tarkistetaan löytyykö kirjain, joka toistuu yhden kirjaimen välillä
        if re.search(r'([a-z]).\1',string) is not None:
            count += 1
print(count)
file1.close