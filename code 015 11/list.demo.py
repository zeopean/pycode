#!/usr/bin/python3

stack = []
for x in range(1,10):
	stack.append(x)    #追加元素 append  --> 入栈
	print('push',x,end='')
	print(stack)

print('Now stock is' , stack)

while len(stack)>0:
	print('pop' , stack.pop() , end=' ')  #表示出栈
	print(stack)
