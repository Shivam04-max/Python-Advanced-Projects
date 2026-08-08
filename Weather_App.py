from Weather_API import get_weather, get_weather_details, Weather

def main():
    user_city: str = input("Enter your city: ")

    current_weather: dict = get_weather(user_city, mock=True)
    weather_details: list[Weather] = get_weather_details(current_weather)

    dfmt = "%d/%m/%y"

    days = sorted({f"{weather.date:{dfmt}}" for weather in weather_details})

    for day in days:
        print(day)
        print("---")

        grouped = [
            weather
            for weather in weather_details
            if f"{weather.date:{dfmt}}" == day
        ]

        for weather in grouped:
            print(weather)

        print()

if __name__ == "__main__":
    main()