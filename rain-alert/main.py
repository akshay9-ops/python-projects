import requests
import os
from twilio.rest import Client

# Twilio credentials — from GitHub Secrets
account_sid = os.environ.get("ACCOUNT_SID")
auth_token = os.environ.get("AUTH_TOKEN")

OWM_Endpoint = "https://api.openweathermap.org/data/2.5/forecast"
api_key = os.environ.get("OWM_APIKEY")

weather_params = {
    "lat": 45.133,
    "lon": 7.367,
    "appid": api_key,
    "cnt": 4,
}

response = requests.get(OWM_Endpoint, params=weather_params)
response.raise_for_status()
weather_data = response.json()

will_rain = False

for weather in weather_data["list"]:
    condition_code = weather["weather"][0]["id"]
    if condition_code <= 700:
        print("bring Umbrella")
        will_rain = True
    else:
        print("not bring Umbrella")

print(will_rain)

if will_rain:
    client = Client(account_sid, auth_token)
    message = client.messages.create(
        body="Take umbrella!",
        from_='+17372508034',
        to='+17372508034'
    )
    print(message.status)
