import requests


def get_log_lan(name): 

    api_key1 = '4uUyoLy5ce8VM9FrmBCQ2Q==AqeeWxvclDhZllbk'
    api_url = 'https://api.api-ninjas.com/v1/city?name={}'.format(name)
    response = requests.get(api_url, headers={'X-Api-Key': api_key1})

    if response.status_code == requests.codes.ok:
        data = response.json()[0]
        #print(data.get('name'))
    else:
        print("Error:", response.status_code, response.text)

    lat = data.get('latitude')
    lon = data.get('longitude')

    return lat, lon

def get_weather(name):
    lat, lon = get_log_lan(name)
    api_key2 = 'ceecc2e802ac386e9491cb763c174660'
    url = f'https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={api_key2}'

    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()
        temp = data['main']['temp']
        desc = data['weather'][0]['description']
    else:
        print('Error fetching weather data')
    return name, temp, desc


name, temp, desc = get_weather('Providence')
print(name, temp, desc)