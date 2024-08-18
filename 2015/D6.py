import numpy as np
#luodaan gridi
lights = np.zeros([1000,1000], dtype=int)
#funktio millä laitetaan gridistä tietyt valot päälle
def turnOn(first, second):
    lights[first[0]:(second[0])+1,first[1]:(second[1]+1)]=1
    return lights
#valoja pois
def turnOff(first, second):
    lights[first[0]:(second[0])+1,first[1]:(second[1]+1)] = 0
    return lights
#valojen muutos
#def Toggle(first, second):
#    if lights[first[0]:(second[0])+1,first[1]:(second[1]+1)] == 1:
#        lights[first[0]:(second[0])+1,first[1]:(second[1]+1)]=0
#    else:
#        lights[first[0]:(second[0])+1,first[1]:(second[1]+1)]=1
#    return lights

pair1 = [0,0]
pair2 = [999,999]
turnOn(pair1,pair2)
unique, counts = np.unique(lights, return_counts=True)
print( dict(zip(unique, counts)))
turnOff([499,499],[500,500])
unique, counts = np.unique(lights, return_counts=True)
print( dict(zip(unique, counts)))