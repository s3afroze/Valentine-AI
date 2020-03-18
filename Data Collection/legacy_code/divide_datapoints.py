# apply regex to extract relevant information

import re
from pprint import pprint

with open('RUBY.txt','r') as f:
	string = f.read()
	data = string.split('\n')

	for quote in data:
		# print(quote)
		
		# open the file with the larger lines
		if len(quote) <= 200:
			with open('processed/JADE_2.txt','a') as ll:
				ll.write(quote + '\n')

		# # open the file with smaller lines
		# elif len(quote) <= 5:
		# 	with open('short_lines.txt','a') as sl:
		# 		sl.write(quote + '\n'*2)

		# # open the file with acceptable
		# else:
		# 	with open('accept_lines.txt','a') as al:
		# 		al.write(quote + '\n'*2)

