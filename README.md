# Weather Report Assistant

A Python-based weather reporting assistant that combines WeatherAPI.com data with Azure OpenAI's GPT-4 to generate natural language weather reports in Indonesian.

## Features

- Fetches real-time weather data using WeatherAPI.com
- Generates natural language weather reports using Azure OpenAI GPT-4
- Supports any city available in WeatherAPI.com's database
- Provides reports in Indonesian language
- Includes temperature, humidity, wind speed, and weather conditions
- Command-line interface for easy city selection

## Prerequisites

- Python 3.9 or higher
- Azure OpenAI API access
- WeatherAPI.com API key

## Installation

1. Clone the repository:
```bash
git clone <repository-url>
cd weather_crew_project
```

2. Create and activate a virtual environment:
```bash
python -m venv venv
source venv/bin/activate  # On Windows, use: venv\Scripts\activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

4. Copy the example environment file and configure your API keys:
```bash
cp .env.example .env
```

5. Update the `.env` file with your API credentials:
```
AZURE_OPENAI_API_KEY=your_azure_openai_key_here
AZURE_OPENAI_ENDPOINT=your_azure_openai_endpoint_here
AZURE_OPENAI_API_VERSION=2024-02-15-preview
WEATHERAPI_KEY=your_weatherapi_key_here
```

## Usage

1. Get weather report for default city (Jakarta):
```bash
python main.py
```

2. Get weather report for a specific city:
```bash
python main.py "New York"
```

The program will output a weather report in Indonesian that includes:
- Current temperature
- Humidity levels
- Wind speed
- Weather conditions
- Natural language description of the weather
- Recommendations based on current conditions

## How It Works

The Weather Report Assistant follows a simple but powerful workflow:

1. **User Input**
   - User provides a city name through command line: `python main.py "Jakarta"`
   - If no city is provided, defaults to "Jakarta"

2. **Weather Data Retrieval**
   ```python
   # Fetches current weather from WeatherAPI
   response = requests.get("http://api.weatherapi.com/v1/current.json", params={
       "key": api_key,
       "q": city,
       "aqi": "no"
   })
   ```
   - Makes API call to WeatherAPI.com
   - Retrieves real-time data including temperature, humidity, wind speed, and conditions
   - Handles any API errors or invalid responses

3. **Natural Language Processing**
   ```python
   # Creates weather report prompt in Indonesian
   prompt = f"""Berdasarkan data cuaca berikut untuk {city}:
   Suhu: {temperature}°C
   Kelembaban: {humidity}%
   Kecepatan Angin: {wind_speed} km/jam
   Kondisi: {conditions}
   """

   # Generates report using Azure OpenAI
   response = client.chat.completions.create(
       model="gpt-4",
       messages=[
           {"role": "system", "content": "Anda adalah reporter cuaca..."},
           {"role": "user", "content": prompt}
       ]
   )
   ```
   - Formats weather data into a structured prompt in Indonesian
   - Uses Azure OpenAI's GPT-4 to generate a natural language report
   - Includes current conditions, feel-like conditions, and daily recommendations

4. **Output**
   - Displays a formatted weather report in Indonesian
   - Report includes:
     - Current weather summary
     - How it feels outside
     - Practical recommendations based on conditions

### Data Flow
```
User Input (city name)
     ↓
WeatherAPI (real-time data)
     ↓
Data Processing
     ↓
Azure OpenAI (natural language)
     ↓
Indonesian Weather Report
```

### Example Output
```
Weather Report:
--------------
Selamat pagi! Berikut laporan cuaca untuk Jakarta:

Saat ini suhu udara mencapai 27.8°C dengan kondisi berawan sebagian. 
Kelembaban udara cukup tinggi yakni 71%, yang membuat udara terasa lebih 
hangat dari suhu sebenarnya. Angin bertiup dengan kecepatan 19.4 km/jam.

Dengan kondisi seperti ini, akan terasa cukup hangat di luar dengan sedikit 
kesejukan dari hembusan angin. Namun, kelembaban yang tinggi mungkin membuat 
udara terasa agak pengap.

Rekomendasi untuk hari ini:
- Kenakan pakaian yang ringan dan menyerap keringat
- Bawalah air minum untuk menjaga hidrasi
- Siapkan payung untuk antisipasi cuaca yang berubah-ubah
```

## Project Structure

- `main.py`: Main application file containing the WeatherAssistant class
- `requirements.txt`: Python dependencies
- `.env`: Configuration file for API keys (not tracked in git)
- `.env.example`: Example configuration file
- `README.md`: Project documentation

## Dependencies

- `openai`: For Azure OpenAI API integration
- `requests`: For making HTTP requests to WeatherAPI
- `python-dotenv`: For loading environment variables

## Error Handling

The application includes error handling for:
- Invalid API keys
- Network connection issues
- City not found
- API rate limits
- Invalid responses

## Security

- API keys are stored in `.env` file
- `.env` is included in `.gitignore` to prevent accidental commits
- Example configuration provided in `.env.example`

## Contributing

1. Fork the repository
2. Create a feature branch
3. Commit your changes
4. Push to the branch
5. Create a Pull Request

## License

This project is licensed under the MIT License - see the LICENSE file for details.
