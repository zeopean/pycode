#!/usr/bin/python3

import string
import sys

#定义一个字典
words = {}
#什么鬼
strip = string.whitespace + string.punctuation + string.digits +'\"'
#遍历
for filename in sys.argv[1:]:
	for line in open(filename):
		for word in line.lower().split():
			word = word.strip(strip)
			if len(word) > 2:
				words[word] = words.get(word ,0)+1

for word in sorted(words):	
	print("'{0} occurs{1} times:'".format(word , words[word]))

