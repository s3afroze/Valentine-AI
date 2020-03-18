# apply regex to extract relevant information
# also note to keep a in loop writing file because w will overwrite the data and the string will be the ones in the end

import re
from pprint import pprint

with open('tango.txt','r') as f:
	string = f.read()
	
	# some wierd quotations
	content = string.replace('“','"')
	content2 = content.replace('”','"')
	content3 = content2.replace('\n','')
	
	# author breakup
	data = content3.split('. ')
	
	# get data from quotations
	for el in data:
		# pprint(el)
		# print('\n')
		# regex for picking alphabetics only 
		# pre_quoted = re.findall(r'/^[A-Z]+$/i', el)

		# regex for picking quotations.
		pre_quoted = re.findall(r'(?<=")([^"]*)', el)
		print(pre_quoted)
		
		# print(quoted)
		# print('--')

		# scanned and approved
		if pre_quoted:
			with open('processed/tango_regex.txt','a') as fp:
				# new line before quoting all
				fp.write('\n'*2)
				# takes care of the multiple instances
				for quote in pre_quoted:
					# print(quote)
					fp.write(quote)

		# scanned and rejected - double check
		else:
			with open('processed/false_positive.txt','a') as fr:
				# new line before quoting all
				fr.write(el+'\n'*2)
				