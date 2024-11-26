# app.py
from flask import Flask, render_template, request
import requests

app = Flask(__name__)


API_KEY = 'your_api_key'


def get_weather(city):
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric"
    response = requests.get(url)
    data = response.json()
    return data

@app.route("/", methods=["GET", "POST"])
def index():
    weather_data = None
    error = None

    if request.method == "POST":
        city = request.form.get("city")
        
        if city:
            data = get_weather(city)
            if data.get("cod") != 200:
                error = f"City '{city}' not found. Please try again."
            else:
                weather_data = data

    return render_template("index.html", weather_data=weather_data, error=error)

if __name__ == "__main__":
    app.run(debug=True)
