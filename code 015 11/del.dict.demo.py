#!/usr/bin/python3

dict = {'name':'zeopean' , 'age':21 , 'class':'daxue'}

print('handle before:')
print(dict)

del dict['name'] 	 #删除指定值
print('handle after:')
print(dict)	

dict.clear()		 #删除所有条目
print('handle after:')
print(dict)
