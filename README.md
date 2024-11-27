**Installation**
1. Clone the Repository:

   git clone https://github.com/your-username/weather-app.git
   cd weather-app

2. install Dependencies: Install Flask using pip:

   pip install flask requests

3. Get an API Key:

    Sign up at OpenWeatherMap.
    Create an API key from the dashboard.

4. Set Up Environment Variables: Create a .env file in the project directory and add your OpenWeatherMap API key:

   API_KEY=your_api_key_here

**Usage**
1. Run the Application: Start the Flask development server:

   python app.py

2. Access the App: Open your browser and go to:

   http://127.0.0.1:5000/

3. Search for Weather Information:

    Enter the name of a city in the search box.
    Click "Get Weather" to display the current weather information.

**Known Issues**
  - Limited error handling for invalid city names.
  - OpenWeatherMap API key usage is rate-limited; ensure compliance with their policies.
