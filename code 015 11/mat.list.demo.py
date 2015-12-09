#!/usr/bin/python3

mat = [[1,2,3,] ,[4,4,5,6] , [7,8,9]]

new_mat = [ [ row[i] for  row in mat ] for i in [0,1,2] ] #嵌套
print(new_mat)

