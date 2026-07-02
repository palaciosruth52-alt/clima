import requests

class WeatherApiClient:
    def __init__(self):
        self.base_url = "https://api.open-meteo.com/v1/forecast"

    def get_weather_data(self, lat, lon):
        # Solicitamos las 3 variables que elegiste
        params = {
            "latitude": lat,
            "longitude": lon,
            "current": "temperature_2m,relative_humidity_2m,precipitation_probability,wind_speed_10m"
        }
        response = requests.get(self.base_url, params=params)
        if response.status_code == 200:
            return response.json()["current"]
        return None