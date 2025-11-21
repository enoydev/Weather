import requests as rq
import redis as redis
import os
import json as json

# https://weather.visualcrossing.com/VisualCrossingWebServices/rest/services/timeline/


def main():

    api_key_weather = os.getenv("WEATHER_API_KEY")
    url = "https://weather.visualcrossing.com/VisualCrossingWebServices/rest/services/timeline"
    location = "Recife, PE" 
    params = {
            "key": api_key_weather,
            "unitGroup": "metric",
            "lang": "pt",
            "include": "current"
        }
    data = get_cached_data(location, url, params)
    print(f"Temperatura atual: {data['currentConditions']['temp']}°C")   
           
    
    
  
def get_cached_data(location, url, parametros):
    r = None
    try:
        r = redis.Redis(host='localhost', port=6379, db=0)
        cache_key = f"weather:{location}"

        cached_data = r.get(cache_key)
        if cached_data:
            print('dados obtidos do cache! ')
            return json.loads(cached_data)
        
    except redis.ConnectionError:
        print('Redis nao iniciado ou indisponivel. ')

    print('tentando setar o cache ')
    data = fetch_from_api(url,location,parametros)
    print(data)
    if data:
        try:
            r.set(cache_key, json.dumps(data), ex=3600)
        except redis.ConnectionError:
            pass

    return data    
    
# checa se a url esta disponivel e verifica o formato de saida (se eh json)
def fetch_from_api(url, location, parametros):
    
    try:
        response = rq.get(f'{url}/{location}', params=parametros, timeout=15)
        if response.ok and response.headers.get("Content-Type", "").startswith("application/json"):
            return response.json()
        return None
    except rq.exceptions.RequestException:
        return None

    

 

if __name__ == "__main__":
    main()