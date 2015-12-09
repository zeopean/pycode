#!/usr/bin/python3

import sys 
import time
import string
from collections import deque

LoadingStr = deque('>---------------------')
while True:
	print('\r%s' % ''.join(LoadingStr)),
	LoadingStr.rotate(1)
	sys.stdout.flush()
	time.sleep(0.05)
