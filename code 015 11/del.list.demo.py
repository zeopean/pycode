#!/usr/bin/python3

lst = [1,2,3,4,5,6,7,8]
del lst[2]   #删除指定项
print(lst)

del lst[2:5]	#删除切片
print(lst)

del lst[:]	#删除整个列表
print(lst)

lst = [1,23,4]
print('删除列表的整实体' )
del lst

