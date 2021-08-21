#!/usr/bin/env python3.9
from flask import Blueprint, request, jsonify
from twilio.twiml.messaging_response import MessagingResponse, Message
from twilio.rest import Client

import sys
import os
from dotenv import load_dotenv

load_dotenv() 

if (os.getenv("ENV") == "PROD"):
    # Your Account SID from twilio.com/console
    account_sid = os.getenv('TW_ACCOUNT_SID')
    # Your Auth Token from twilio.com/console
    auth_token  = os.getenv('TW_AUTH_TOKEN')
else:
    # TESTING
    account_sid = os.getenv('TW_ACCOUNT_SID_TEST')
    auth_token  = os.getenv('TW_AUTH_TOKEN_TEST')

client = Client(account_sid, auth_token)

v0_blueprint = Blueprint('v0', __name__)

def get_response(body: str) -> str:
    if (body.startswith('!')):
        body = body[1:]
        if (body == 'help'):
            return help_message()
        elif (body == 'weather'):
            return weather_message(body[7:])
        elif (body == 'news'):
            return news_message(body[4:])
        elif (body == 'translate'):
            return translate_message(body[9:])
        elif (body == 'joke'):
            return joke_message()
        elif (body == 'time'):
            return time_message()
        elif (body == 'date'):
            return date_message()
        elif (body == 'directions'):
            return directions_message(body[10:])
        else:
            return error_message()
    else:
        return search_message(body)

@v0_blueprint.route("/query", methods=['POST'])
def sms_reply():
    from_number = request.form['From']
    to_number = request.form['To']
    body: str = request.form['Body']

            
    
    response = MessagingResponse()
    response.message(get_response(body))
    return str(response)