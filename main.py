import requests
from twilio.rest import Client
import os



OWM_Endpoint = "http://api.openweathermap.org/data/2.5/forecast"
api_key = os.environ.get("OWM_API_KEY")
account_sid = os.environ.get("ACCOUNT_SID")
auth_token = os.environ.get("AUTH_TOKEN")


weather_params = {
    "lat": 23.275277,
    "lon": 77.450907,
    "appid": api_key,
    "cnt": 4,
}



response = requests.get(OWM_Endpoint, params=weather_params)
response.raise_for_status()
weather_data = response.json()
# print(weather_data["list"][0]["weather"][0]["id"])

will_rain = False
for hour_data in weather_data["list"]:
    condition_code = (hour_data["weather"][0]["id"])
    if int(condition_code) < 700:
        will_rain = True

if will_rain:
    client = Client(account_sid, auth_token)
    message = client.messages \
        .create(
            body = "It is going to rain today. Remember to bring an Umbrella.",
            from_= 'os.environ.get("FROM_NO"),
            to='os.environ.get("TO_NO"),
    )
    print(message.status)
