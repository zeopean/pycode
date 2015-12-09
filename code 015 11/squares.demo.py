#!/usr/bin/python3

squares = [x**2 for x in range(10)]   #推导式
print(squares)

pairs = [ (x , y ) for x in [1,2,3] for y in [3,4,5,6] if x!=y] #推导式
print(pairs)

