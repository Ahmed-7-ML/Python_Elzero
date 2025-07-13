import numpy 

values1 = [4, 11, 7, 14]

print(numpy.std(values1)) # Population Standard Deviation

print(numpy.std(values1,ddof=1))  # Sample Standard Deviation
