import numpy
from statistics import multimode

values1 = [11 , 12 ,4 ,6,90, 11 , 1, 2] # n => even

print(numpy.mean(values1)) # (11+11+12+4+6+90+1+2)/8 = 17.125
print(numpy.median(values1)) # (6 + 11) / 2 = 8.5
# 1 2 4 6 11 11 12 90

print(multimode(values1)) # 11

values2 = [21, 21, 13, 42, 40, 55, 48]  # n => odd

print(numpy.median(values2))  # 40
# 13 21 21 40 42 48 55

print(numpy.mean(values2))

print(multimode(values2)) # 21
