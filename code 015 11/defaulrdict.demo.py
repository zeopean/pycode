#!/usr/bin/python3

from collections import defaultdict

members = [
	['male' ,'user1'],
	['female' , 'user2'],
	['male','user11'],
	['female' , 'user22']
]

result = defaultdict(list)
for sex , name in members:
	result[sex].append(name)
print(result)
