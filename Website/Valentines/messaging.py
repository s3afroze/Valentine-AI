"""
@Author: Shahzeb
Usecase: The script will be used as an interaction for people to set for sending a message on set time to people
"""

from twilio.rest import Client
from flask import Flask, request, redirect

# Your Account SID from twilio.com/console
account_sid = "ACf5ca01987caeaab295c56fb61a3b7cf7"
# Your Auth Token from twilio.com/console
auth_token  = "9ac026fea13eb7d66f307c02b0299d71"

client = Client(account_sid, auth_token)

# integrate html for country extension
# canadian numbers only - support

def send_message(send_message_body, number):
	print(send_message_body)
	print(number)
	message = client.messages.create(
    to=number, 
    from_="2898022404",
    body=send_message_body + " -Valentine-AI")
	print(message.sid)
