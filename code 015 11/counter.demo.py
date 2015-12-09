#!/usr/bin/python3

from collections import Counter
demo = 'hello world ,welcome zeopean ,you are good!'

c = Counter(demo)

#获取出现频率最大的5个字符
print(c.most_common(5))

