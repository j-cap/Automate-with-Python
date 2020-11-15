
# getOpenWeather.py - Prints the weather for a location from the command line
         
import json, requests, sys, datetime, OpenWeatherMapToken

APPID = OpenWeatherMapToken.APPID
# Comute location from command line arguments
if len(sys.argv) < 2:
    print("Usage: getOpenWeather.py city_name, 2-letter_country_code")
    sys.exit()

location = "".join(sys.argv[1:])

with open("city.list.json", "r", encoding="cp866") as f:
    citylist_json = json.load(f)

for c in citylist_json:
    if c["name"] == location[:-3] and c["country"] == location[-2:]:
        city_id = str(c["id"])
        break

# TODO: Download the JSON data from OpenWeatherMap.org's API.
url = "http://api.openweathermap.org/data/2.5/forecast?id="+city_id+"&APPID="+APPID
response = requests.get(url)
response.raise_for_status()
#  print(response.text)
# TODO: Load JSON data into a python variable.
weatherData = json.loads(response.text)
# Print weather descriptions
w = weatherData["list"]
print(f"Current weather in {location}")
def get_date_and_time(d):
    date = d.split()[0].split('-') 
    time = d.split()[1]
    date = datetime.datetime(*list(map(int, date)))
    return date, time


for i in [0, 8, 16]:

    date, time = get_date_and_time(w[i]['dt_txt'])
    print(date.strftime('%A').ljust(len("wednesday")), "-",time, end="\t")
    print(w[i]['weather'][0]['main'].ljust(6),'-', w[i]['weather'][0]['description'].ljust(14), '-', f"Temp = {round(w[i]['main']['temp']-273.15, 1)}°C")

