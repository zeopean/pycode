#!/usr/bin/python3
from collections import OrderedDict
items = (
	('A' , 1),
	('B' , 2),
	('C' , 3)
)

demoDict 	= dict(items)
orderedDict 	= OrderedDict(items)
print('Regular Dict:')
for key , val in demoDict.items():
	print(key , val)
print("Ordered Dict:")
for key ,val in orderedDict.items():
	print(key ,val)

