# Weather Forecast API

## Description
This project is a RESTful API built with Django that provides weather forecasts for different cities. It leverages the OpenWeatherMap API to fetch real-time weather data.

## Features
- Fetch weather data by city name.
- Simple user interface to display weather data using Svelte.
- Easy to extend and modify.

## Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/weather-forecast-api.git
   cd weather-forecast-api
   ```

2. Set up the Django backend:
   - Navigate to the backend folder:
     ```bash
     cd backend
     ```
   - Install dependencies:
     ```bash
     pip install -r requirements.txt
     ```
   - Run migrations:
     ```bash
     python manage.py migrate
     ```
   - Start the Django server:
     ```bash
     python manage.py runserver
     ```

3. Set up the Svelte frontend:
   - Open another terminal and navigate to the frontend folder:
     ```bash
     cd frontend
     ```
   - Install dependencies:
     ```bash
     npm install
     ```
   - Start the Svelte development server:
     ```bash
     npm run dev
     ```

## Usage
1. Access the API at `http://localhost:8000/weather/{city}` to get weather data for the specified city.
2. Use the Svelte frontend to interact with the API.

## Contributing
Contributions are welcome! Please open an issue or submit a pull request.

## License
This project is licensed under the MIT License.