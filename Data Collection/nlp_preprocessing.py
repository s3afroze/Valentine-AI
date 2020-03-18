"""
@author: Shahzeb Afroze
This script will be used to clean the data scraped using the crawler earlier

Notes concerning data:
Good Reads quotes are always in same format with quotation and author
"""

# apply regex to extract relevant information
# also note to keep a in loop writing file because w will overwrite the data and the string will be the ones in the end

import re
import os
import string
from language_checker_script import detect_language


good_reads_scraped_data_files = os.listdir('scraped_data')

# makes sure that data scraed are .txt files
good_reads_scraped_data_text_files = [file for file in good_reads_scraped_data_files if file.endswith(".txt") ]

max_len_quote = 250 #arbitary number, longer lines usually tend to become a description of a movie scene

# punctuation removal
translator = str.maketrans('', '', string.punctuation)
remove_string_translator = str.maketrans('', '', string.digits)

for scraped_text_file in good_reads_scraped_data_text_files:
	file_path = os.path.join('scraped_data', scraped_text_file)

	with open(file_path,'r') as f:
		raw_quote = f.read()
		content = raw_quote.split("\n")
		# regex for double quotes does not working owing to multiple conversation point in some quotes.
		# usually a movie scene		
		with open(f'quotes_extracted/{scraped_text_file}','a') as fp:			
			for quote in content:
				# conditional statement: meet max character and - criteria in order to remove authors
				if (len(quote)<=max_len_quote) and ("―" not in quote):
					language = detect_language(quote)
					if language == 'english':
						# adjustments so that translator can remove them
						quote = quote.replace('“','"')
						quote = quote.replace('”','"')

						# removes puntuation					
						quote = quote.translate(translator)	

						# removes numbers				
						quote = quote.translate(remove_string_translator)

						# basic preprocessing
						quote = quote.strip()
						quote = quote.lower()

						fp.write('\n'*2)
						fp.write(quote)
					else:
						print(quote)

				


