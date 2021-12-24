'''the api key : a952bc894d80eb9e83fa867c5eb20cd0

http://api.openweathermap.org/data/2.5/weather?q=Khulna&appid=a952bc894d80eb9e83fa867c5eb20cd0
'''

# twilio python semple code

# Download the helper library from https://www.twilio.com/docs/python/install
import os
from twilio.rest import Client


# Find your Account SID and Auth Token at twilio.com/console
# and set the environment variables. See http://twil.io/secure
account_sid = os.environ['TWILIO_ACCOUNT_SID']
auth_token = os.environ['TWILIO_AUTH_TOKEN']
client = Client(account_sid, auth_token)

message = client.messages \
                .create(
                     body="Join Earth's mightiest heroes. Like Kevin Bacon.",
                     from_='+15017122661',
                     to='+15558675310'
                 )

print(message.sid)