import os
import requests
from openai import AzureOpenAI
from dotenv import load_dotenv
import argparse

# Load environment variables
load_dotenv()

class WeatherAssistant:
    def __init__(self, location):
        self.location = location
        
        # Azure OpenAI Client
        self.client = AzureOpenAI(
            api_key=os.getenv("AZURE_OPENAI_API_KEY"),
            api_version=os.getenv("AZURE_OPENAI_API_VERSION"),
            azure_endpoint=os.getenv("AZURE_OPENAI_ENDPOINT")
        )

    def get_weather_data(self):
        """Get weather data from WeatherAPI"""
        api_key = os.getenv("WEATHERAPI_KEY")
        base_url = "http://api.weatherapi.com/v1/current.json"
        
        params = {
            "key": api_key,
            "q": self.location,
            "aqi": "no"
        }
        
        try:
            response = requests.get(base_url, params=params)
            if response.status_code == 200:
                data = response.json()
                return {
                    "temperature": data["current"]["temp_c"],
                    "humidity": data["current"]["humidity"],
                    "description": data["current"]["condition"]["text"],
                    "wind_speed": data["current"]["wind_kph"]
                }
            else:
                print(f"API Response: {response.text}")
                return f"Error: Unable to fetch weather data. Status code: {response.status_code}"
        except Exception as e:
            return f"Error: {str(e)}"

    def generate_weather_report(self, weather_data):
        # Create prompt for GPT-4
        prompt = f"""Berdasarkan data cuaca berikut untuk {self.location}, berikan laporan cuaca yang informatif:
        Suhu: {weather_data['temperature']}°C
        Kelembaban: {weather_data['humidity']}%
        Kecepatan Angin: {weather_data['wind_speed']} km/jam
        Kondisi: {weather_data['description']}
        
        Harap sertakan:
        1. Rangkuman kondisi cuaca saat ini
        2. Bagaimana rasanya di luar
        3. Rekomendasi yang relevan untuk hari ini
        """
        
        try:
            response = self.client.chat.completions.create(
                model="gpt-4",  # This should match your Azure OpenAI deployment name
                messages=[
                    {"role": "system", "content": "Anda adalah reporter cuaca yang memberikan informasi cuaca dalam Bahasa Indonesia yang jelas dan ringkas. Gunakan bahasa yang natural dan mudah dipahami."},
                    {"role": "user", "content": prompt}
                ]
            )
            return response.choices[0].message.content
        except Exception as e:
            return f"Error generating weather report: {str(e)}"

def main():
    parser = argparse.ArgumentParser(description='Get weather report for a city')
    parser.add_argument('city', nargs='?', default='Jakarta', help='City name (default: Jakarta)')
    args = parser.parse_args()

    assistant = WeatherAssistant(args.city)
    weather_data = assistant.get_weather_data()
    
    if isinstance(weather_data, str) and weather_data.startswith('Error'):
        print(f"\nWeather Report:\n--------------\n{weather_data}")
        return

    report = assistant.generate_weather_report(weather_data)
    print(f"\nWeather Report:\n--------------\n{report}")

if __name__ == "__main__":
    main()
