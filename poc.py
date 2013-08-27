#!/usr/bin/env python

import sys, re
input=open(sys.argv[1],'r')

default_data = {'start': '', 'a': '', 'b': '','c': '','d': '', 'e': '', 'f': '', 'g': ''}
datasets = []
data = default_data.copy()

for line in input:
	if line == "\n":
		datasets.append(outputString)
		#flush the data array
		data = default_data.copy()
		outputString=""
		continue
	key, val = line.split(':')
	data[key] = val.strip()
	outputString=data['start']+"\t"+data['a']+"\t"+data['b']+"\t"+data['c']+"\t"+data['d']+"\t"+data['e']+"\t"+data['f']+"\t"+data['g']+"\n"

#import pprint
#pprint.pprint(datasets)
for line in datasets:
		print line
			
	

