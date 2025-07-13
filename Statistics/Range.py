import numpy

values1 = [13, 21, 25, 40 ,50, 72]

print(numpy.ptp(values1))

values2 = [21, 13, 40, 25, 72, 50] # Sort it First => 13 21 25 40 50 72 

print(numpy.ptp(values2)) # 72 -13 = 59 
