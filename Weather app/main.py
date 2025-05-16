# Import the module.
import unit_convert
import python_weather
import asyncio
import os
import sys

async def main() -> None:
 
  # Declare the client. The measuring unit used defaults to the metric system (celcius, km/h, etc.)
  async with python_weather.Client(unit=python_weather.IMPERIAL) as client:

    # Fetch a weather forecast from a city.
   try:
    location=input("Please Enter the Location ::")
    weather = await client.get(location)
   except Exception as e:
     print("Location not found:")
     sys.exit()

   def current_weather():
    # Fetch the temperature for today.
    #weather.temperature=5*((weather.temperature-32)/9)
    print(f"Date and Time of {location} is :->",weather.datetime)
    print(f"Temperature of {location} is :-> ", unit_convert.f(weather.temperature))
    print(f"The weather of {location} is :->",weather.description)

   def weather_anyday(date1):   
     for daily in weather:   
      if(str(daily.date)==date1):
        for hourly in daily:
          print("Time:->",hourly.time ,":Description:->",hourly.description,":Expected Temperature:->",unit_convert.f(hourly.temperature))

  print("Welcome to Weather Forcast::")
  choice=int(input("Enter 1 for current weather reports\nEnter 2 for weather reports on any of the 3 following days::\n"))
  match choice:
      case 1:
        current_weather()
      case 2:
        datez=input("Enter the date for weather report in the form of YYYY-MM-DD:\n")
        weather_anyday(datez)


if __name__ == '__main__':


  if os.name == 'nt':
    asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())

  asyncio.run(main())