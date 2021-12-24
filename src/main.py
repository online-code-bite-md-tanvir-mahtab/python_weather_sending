import requests
import os
from twilio.rest import Client


# constant
API_KEY ="a952bc894d80eb9e83fa867c5eb20cd0"

PLACE_NAME = "Khulna"

TIME = "daily,minutely,current"

PLACE_LATITUDE = 22.826238
PLACE_LONGITUDE = 89.545805
IS_RAINING = False

# for the tiwilio
TWILIO_SID = "ACb1405cf68b178ef4f9edf467217242eb"
TWILIO_AUTH_TOKEN = "36467113c7880fc3304576e92f18d8f3"




# for the units
API_UNITS = "metric"

# weebsite url
WEBSITE_URL = "https://api.openweathermap.org/data/2.5/onecall"

# making a url parsing request with the help of thee 
http_request = requests.get(url= f"{WEBSITE_URL}?lat={PLACE_LATITUDE}&lon={PLACE_LONGITUDE}&exclude={TIME}&units={API_UNITS}&appid={API_KEY}")

# print(f"{WEBSITE_URL}?lat={PLACE_LATITUDE}&lon={PLACE_LONGITUDE}&extend={TIME}&units={API_UNITS}&appid={API_KEY}")
# raising a error
http_request.raise_for_status()

data = http_request.json()
# printing the data with the help of the json
for i in range(0,12+1):
    # now i am going to create the client
    client = Client(TWILIO_SID,TWILIO_AUTH_TOKEN)
    id = (data['hourly'][i]['weather'][0]['id'])
    if id < 700:
        IS_RAINING = True
    else:
        IS_RAINING = False
if IS_RAINING:
    message = client.messages \
                .create(
                     body="Join Earth's mightiest heroes. Like Kevin Bacon.",
                     from_='+16893004611',
                     to='+8801839550323'
                 )
    print(message.sid)
else:
    message = client.messages \
                .create(
                     body="Join Earth's mightiest heroes. Like Kevin Bacon.",
                     from_='+16893004611',
                     to='+8801839550323'
                 )

    print(message.status)
