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
