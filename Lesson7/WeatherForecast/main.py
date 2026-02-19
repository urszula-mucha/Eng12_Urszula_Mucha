from datetime import datetime, timedelta
from Lesson7.WeatherForecast.WeatherForecast import WeatherForecast


weather_forecast = WeatherForecast()
# --- get the today's date ---
today = datetime.today().date()
print(f"Today's date: {today}")


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

#SoC with error handling
try:
    rain_number = weather_forecast[provided_date] #__getitem__
except ValueError as e:
    print(e)
    print("The date is outside the forecast range.")
    exit()

# --- Print the result---
if rain_number == 0.0:
    print(f"It won't rain on {provided_date}.")
elif rain_number > 0.0:
    print(f"It will rain on {provided_date}. With amount of {rain_number}mm.")
else:
    print("I don't know.")

#---More info from the interfaces---
print("\nKnown dates:") #__iter__
for d in weather_forecast:
    print(d)

print("\nStored items:")
for d, r in weather_forecast.items(): #items()
    print(d, r)