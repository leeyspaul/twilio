import os
from twilio.rest import Client
SID = os.getenv("twilio_SID")
TOKEN = os.getenv("twilio_TOKEN")
API = os.getenv("twilio_API")

client = Client(SID,TOKEN)

def send_message(to, message):
    to_ = "+1" + str(to)
    message = client.messages.create(
        to = to_,
        from_ = "+12727702947",
        body=message
    )
    print(message.sid)

send_message(9257883374,"this is my new message from twilio")