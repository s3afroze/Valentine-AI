# # loop and remove numbers
# with open('luvze.txt','r') as f:
# 	page = f.read()
# 	content = ''.join([i for i in page if not i.isdigit()])
# 	print(content)
# 	with open('processed/luvze_split_and_concquered.txt','a') as fp:
# 		fp.write(content)

# loop through and split by new lines.

with open('wow4u.txt','r') as f:
	content = f.read()

	# split by new lines
	split_data = content.strip().split('\n')

	with open('processed/wow4u_regex.txt','w') as fp:
		for el in split_data:
			if len(el) > 30:
				print(len(el))
				print(el)
				print('\n')
				fp.write(el+'\n'*2)
		