#!/usr/bin/python3

from collections import deque
#创建空队列
queue	= deque()
for x in range(1 , 6):
	queue.append(x)		#入队
	print('push' , x ,end=' ')
	print(list(queue))

print("now queue is" , list(queue))

while len(queue)>0:
	print('pop', queue.popleft() , end=' ')   #表示出列
	print(list(queue))

