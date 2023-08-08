import config
import requests

class WeatherInfo:
    def get_log_lan(self, name): 
        api_url = 'https://api.api-ninjas.com/v1/city?name={}'.format(name)
        response = requests.get(api_url, headers={'X-Api-Key': config.api_key1})
        
        if response.status_code == requests.codes.ok:
            data = response.json()[0]
        else:
            print("Error:", response.status_code, response.text)
            return None, None
        
        lat = data.get('latitude')
        lon = data.get('longitude')
        
        return lat, lon
    
    def get_weather(self, name):
        lat, lon = self.get_log_lan(name)
        if lat is None or lon is None:
            return None
        
        url = f'https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={config.api_key2}'
        
        response = requests.get(url)
        
        if response.status_code == 200:
            data = response.json()
            temp = data['main']['temp']
            desc = data['weather'][0]['description']
        else:
            print('Error fetching weather data')
            return None, None, None
        
        return name, temp, desc


weather_info = WeatherInfo()
city = "London"
name, temp, desc = weather_info.get_weather(city)
print(name, temp, desc)

# if name is not None:
#     print(f"Current weather in {name}:")
#     print(f"Temperature: {temp} K")
#     print(f"Description: {desc}")

# def run(self):
#     with self.output().open("w") as outfile:
#         outfile.write(name, temp, desc)
