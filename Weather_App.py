import requests
import tkinter as tk
from PIL import Image, ImageTk
from tkinter import messagebox

def get_forecast(city, api_key):
    base_url = 'http://api.openweathermap.org/data/2.5/forecast?q={}&appid={}&units=metric'.format(city, api_key)
    response = requests.get(base_url)
    if response.status_code == 200:
        data = response.json()
        return data
    else:
        return None

def get_average_weather(city, api_key):
    forecast_data = get_forecast(city, api_key)

    if forecast_data:
        daily_weather = {}
        for forecast in forecast_data['list']:
            date = forecast['dt_txt'].split(' ')[0]  # Extracting date without time
            if date not in daily_weather:
                daily_weather[date] = {
                    'temp_sum': forecast['main']['temp'],
                    'humidity_sum': forecast['main']['humidity'],
                    'count': 1
                }
            else:
                daily_weather[date]['temp_sum'] += forecast['main']['temp']
                daily_weather[date]['humidity_sum'] += forecast['main']['humidity']
                daily_weather[date]['count'] += 1

        for date, data in daily_weather.items():
            data['temp_avg'] = data['temp_sum'] / data['count']
            data['humidity_avg'] = data['humidity_sum'] / data['count']

        return daily_weather
    else:
        return None

def get_weather_info():
    city = city_entry.get()
    api_key = 'e0b73cbf9b75943553e83a512a322655'  # Replace with your actual API key from OpenWeatherMap

    daily_weather = get_average_weather(city, api_key)

    if daily_weather:
        result = "Weather :\n\n"
        for date, data in sorted(daily_weather.items()):
            result += f"Date: {date}\n"
            result += f"Temperature: {data['temp_avg']:.2f}°C\n"
            result += f"Humidity: {data['humidity_avg']}%\n\n"

        result_label.config(text=result)
    else:
        messagebox.showerror("Error", "Weather data not found for the given city.")

# Create the main window
root = tk.Tk()
root.title("Weather App")

# Create widgets
city_label = tk.Label(root, text="Enter city name:")
city_label.pack()

city_entry = tk.Entry(root)
city_entry.pack()

get_weather_button = tk.Button(root, text="Get Weather", command=get_weather_info)
get_weather_button.pack()

result_label = tk.Label(root, text="", wraplength=300)
result_label.pack()

root.mainloop()