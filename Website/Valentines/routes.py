# python libs
from flask import render_template, url_for, flash, redirect, request, jsonify, session, send_file
import time
import os
import requests
import random
# from weasyprint import HTML

from Valentines.messaging import send_message

# custom
from Valentines import app

APP_ROOT = os.path.dirname(os.path.abspath(__file__))
folder = os.path.join(APP_ROOT, "files")

with open("cleaned_generation.txt", "r") as fp:
	lines = fp.read()
	lines_split = lines.split('\n')

quotes = [quote for quote in lines_split if not len(quote) < 13]
quotes_to_be_sent = []

@app.route("/NLP", methods=['POST', 'GET'])
def NLP():
	import random	
	r1 = random.randint(0, len(quotes))	
		
	# quotes=["An authentic Valentine’s message is one that pleases and the heart that burns for that honour"]
	if request.method == 'POST':		
		from_person = request.form['from']
		to_person = request.form['to']
		number_of_person = request.form['number']

		if len(from_person)>0 and len(to_person)>0:
			send_message_body = f"From: {from_person}\nTo: {to_person}\n {quotes_to_be_sent[-1]}"
		else:
			send_message_body = f"{quotes_to_be_sent[-1]}"
		
		send_message(send_message_body, number_of_person)

	return render_template('random_quote.html', quotes_dump=quotes)

@app.route("/")
@app.route("/home")
def landing_page():
	return render_template('cat.html')

@app.route("/about")
def about():
	return render_template('about.html')

# need to receive quote previously selected aswell
@app.route("/submission_form/<quotes_dump>", methods=['POST', 'GET'])
def submission_form(quotes_dump):
	print('re')
	with open("quotes_sent.txt", "a") as fp:
		fp.write(quotes_dump + '\n')

	quotes_to_be_sent.append(quotes_dump)
	return render_template('submission_form.html', quote=quotes_dump)


	