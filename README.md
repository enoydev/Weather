# Weather
A simple Python script that fetches current weather data from the Visual Crossing Weather API and caches the response in Redis to reduce API calls. It supports metric units and Portuguese language output, with graceful fallbacks when Redis is unavailable.

Weather Cache (Visual Crossing + Redis)


A lightweight Python app that fetches the current weather for a given location using the Visual Crossing Weather API and caches the response in Redis. Caching reduces API calls and speeds up repeated requests. Output is printed in Portuguese with metric units.

Example output:

Temperatura atual: 28.4°C

Features


- Current weather via Visual Crossing Weather API

- Redis caching (1 hour TTL) to minimize API calls

- Graceful fallback when Redis is not available

- Configurable location, language, and units

- Simple, dependency-light script

Requirements


- Python 3.9+

- Redis server (local or remote)

- Visual Crossing API key

Installation


1. Clone the repo
   
```
git clone https://github.com/your-username/weather-cache.git
cd weather-cache
```
2. Install Redis and Requests

```
requests==2.32.3
redis==5.0.8
```
3. Initiate Redis Server
```
sudo systemctl start redis
```
4. Run

Configuration


- Environment variable:
	- WEATHER_API_KEY: Your Visual Crossing API key


- Redis connection defaults:
	- host=localhost, port=6379, db=0


- Default location: Recife, PE

- Default options: unitGroup=metric, lang=pt, include=current

  Set the API key:
  ```
  export WEATHER_API_KEY="your_visual_crossing_api_key"
  # macOS/Linux
  # or on Windows (PowerShell)
  setx WEATHER_API_KEY "your_visual_crossing_api_key"
  ```

  On first run, the app:


- Attempts to read cached data for the location from Redis.

- If not found or Redis is unavailable, it fetches from the API.

- Successful API responses are cached for 1 hour (3600 seconds).

- Prints current temperature in Celsius in Portuguese.

Customization


- Change the default location:
	- In main(), edit location = "Recife, PE"


- Change TTL:
	- In get_cached_data(), adjust ex=3600 when calling r.set


- Change language or units:
	- Update params in main(); see Visual Crossing docs for options:
		- unitGroup: metric, us, uk

		- lang: pt, en, es, etc.
