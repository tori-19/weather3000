import os
from flask import Flask, render_template, request
import requests

app = Flask(__name__)

# Get the API key from environment variable
API_KEY = os.getenv('WEATHER_API_KEY')

# Function to fetch weather data
def get_weather(city):
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric"
    response = requests.get(url)
    data = response.json()
    return data

@app.route("/", methods=["GET", "POST"])
def index():
    weather_data = None
    error = None
    icon_url = None

    if request.method == "POST":
        city = request.form.get("city")
        
        if city:
            # Fetch the weather data
            data = get_weather(city)
            if data.get("cod") != 200:
                error = f"City '{city}' not found. Please try again."
            else:
                weather_data = data
                # Get the weather icon code and build the URL for the icon
                icon_code = data['weather'][0]['icon']
                icon_url = f"http://openweathermap.org/img/wn/{icon_code}@2x.png"

    # Render the index.html template with weather data, error message, and icon URL
    return render_template("index.html", weather_data=weather_data, error=error, icon_url=icon_url)

if __name__ == "__main__":
    app.run(debug=True)
