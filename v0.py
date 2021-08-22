#!/usr/bin/env python3.9
from flask import Blueprint, request, g
from twilio.twiml.messaging_response import MessagingResponse, Message
from twilio.rest import Client

import asyncio
import os
from dotenv import load_dotenv

load_dotenv() 

from responses.responses import get_response

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

@v0_blueprint.route("/query", methods=['POST'])
async def sms_reply():
    from_number = request.form['From']
    to_number = request.form['To']
    body: str = request.form['Body']   
    
    response = MessagingResponse()
    text = await get_response(body, from_number, g.get('conn'))
    response.message(text[:350])
    return str(response)