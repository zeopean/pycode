#!/usr/bin/env python

import json 
d = {'first':'One' , 'second':3,'three':'nanmeme'}
json.dump(d , open('./test.txt' , 'w'))
