from flask import Flask, request
from twilio.rest import Client

import os
from dotenv import load_dotenv

load_dotenv()

# Your Account SID from twilio.com/console
account_sid = os.getenv('TWILIO_ACCOUNT_SID')
# Your Auth Token from twilio.com/console
auth_token  = os.getenv('TWILIO_AUTH_TOKEN')

client = Client(account_sid, auth_token)

app = Flask(__name__)

@app.route('/sms', methods=['POST'])
def sms():
    number = request.form['From']
    message_body = request.form['Body']

    resp = twiml.Response()
    resp.message('Hello {}, you said: {}'.format(number, message_body))

    message = client.messages.create(
        to="+15558675309", 
        from_="+15017250604",
        body="Hello from Python!")
    return str(resp)


if __name__ == '__main__':
    app.run()