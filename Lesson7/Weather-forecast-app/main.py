import requests
import json
from datetime import datetime, timedelta

#original API link
#https://api.open-meteo.com/v1/forecast?latitude={latitude}&longitude={longitude}&daily=precipitation_sum&timezone=Europe%2FLondon&start_date={searched_date}&end_date={searched_date}

#---Check if the weather file exists---
try:
    with open("weather_record.json", "r") as file:
       checked_date = json.load(file)
except (FileNotFoundError, json.JSONDecodeError):
    checked_date = {}

# --- get the today's date ---
today = datetime.today().date()
print(f"Today's date: {today}")

latitude = 18.02945850
longitude = 48.31541980

#--- take the input and validate it---
while True:
    provided_date = input("Enter the date (eg. for January 2026-01-07). Leave empty for tomorrow: ").strip()
    if not provided_date:
        provided_date = (datetime.today() + timedelta(days=1)).strftime("%Y-%m-%d")
        break
    elif provided_date:
        try:
            datetime.strptime(provided_date, "%Y-%m-%d")
            break #valid entry
        except ValueError:
            print("invalid entry format. Use YYYY-MM-DD.")

if provided_date in checked_date:
    rain_number = checked_date[provided_date]["Rain"]
else:
    url = f"https://api.open-meteo.com/v1/forecast?latitude={latitude}&longitude={longitude}&daily=precipitation_sum&timezone=Europe%2FLondon&start_date={provided_date}&end_date={provided_date}"
    # response = requests.get(url)
    # result = response.json()

    try:
        response = requests.get(url)
        result = response.json()
    except requests.exceptions.RequestException as e:  # This is the correct syntax
        raise SystemExit(e)


    # ---validate error from api)
    if response.status_code != 200:
        print("Try another date. HTTP Error:", response.status_code)
        exit()
    if "error" in result:
        print("Error:", result.get("reason", "Unknown error"))
        exit()


    # print(result) #uncomment this to see all info about the weather
    rain = result["daily"]["precipitation_sum"]
    rain_number = float(rain[0])  # change the API result from list to float

    checked_date.update({provided_date: {"Rain": rain_number}})
#print(checked_date)

# --- Print the result---
if rain_number == 0.0:
    print(f"It won't rain on {provided_date}.")
elif rain_number > 0.0:
    print(f"It will rain on {provided_date}. With amount of {rain_number}mm.")
else:
    print("I don't know.")

#---Save the result---
with open("weather_record.json", "w") as file:
    json.dump(checked_date, file, indent=4)
