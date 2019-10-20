import requests
import json
import os

def temperature(city):
    city = city
    cityCode = 0
    #path = os.path.abspath('cityList')
    with open ('/Users/pavankolisetty/Desktop/hackru/cityList.json') as dictEntry:
        dict = json.load(dictEntry)

    for x in dict:
        if(x['name'] == city):
            cityCode = x['id']
            break

    #print(cityCode)

    #cityCode = 4167147

    url = 'http://api.openweathermap.org/data/2.5/weather?id={}&APPID=8d33b075ec7a547f8130fda8388da047'.format(cityCode)

    res = requests.get(url)

    data = res.json()

    temp = ((data['main']['temp'])-273.25)*9/5+32
    wind_speed = data['wind']['speed']*2.237

    description = data['weather'][0]['description']
    rain = data['weather'][0]['main']

    return 'Temperature: {}'.format(temp)

def wind_speed(city):
    city = city
    cityCode = 0
    # path = os.path.abspath('cityList')
    with open('/Users/pavankolisetty/Desktop/hackru/cityList.json') as dictEntry:
        dict = json.load(dictEntry)

    for x in dict:
        if (x['name'] == city):
            cityCode = x['id']
            break

    # print(cityCode)

    # cityCode = 4167147

    url = 'http://api.openweathermap.org/data/2.5/weather?id={}&APPID=8d33b075ec7a547f8130fda8388da047'.format(cityCode)

    res = requests.get(url)

    data = res.json()

    temp = ((data['main']['temp']) - 273.25) * 9 / 5 + 32
    wind_speed = data['wind']['speed'] * 2.237

    description = data['weather'][0]['description']
    rain = data['weather'][0]['main']

    return 'Wind Speed: {} mph'.format(wind_speed)

def weather_description(city):
    city = city
    cityCode = 0
    # path = os.path.abspath('cityList')
    with open('/Users/pavankolisetty/Desktop/hackru/cityList.json') as dictEntry:
        dict = json.load(dictEntry)

    for x in dict:
        if (x['name'] == city):
            cityCode = x['id']
            break

    # print(cityCode)

    # cityCode = 4167147

    url = 'http://api.openweathermap.org/data/2.5/weather?id={}&APPID=8d33b075ec7a547f8130fda8388da047'.format(cityCode)

    res = requests.get(url)

    data = res.json()

    temp = ((data['main']['temp']) - 273.25) * 9 / 5 + 32
    wind_speed = data['wind']['speed'] * 2.237

    description = data['weather'][0]['description']
    rain = data['weather'][0]['main']

    return 'Weather : {}'.format(description)


# Main Function:

city = input("Enter City Name: ")
temp = temperature(city)
temp = str(temp)
temp = temp.split(" ")
print(float(temp[1]))

wind = wind_speed(city)
wind = wind.split(" ")
print(wind[2])

weatherDescription = weather_description(city)
weatherDescription = weatherDescription.split(" ")
print(weatherDescription[2])


if temp <= 32:
    if weatherDescripition == "Clear Sky" or weatherDescription == "Broken Clouds" or weatherDescription == "Scattered Clouds" or weatherDescription == "Few Clouds" or weatherDescription == "Snow":
        clothing = ["coat", "jacket", "shirt", "jeans", "pants"]
        for x in clothing and y in wardrobe:
            if clothing[x] == wardrobe[y]:
                print(wardrobe[y])
    elif weatherDescription == "Snow":
        clothing = ["Coat","T-Shirt","Jeans","Pants"]
        for x in clothing and y in wardrobe:
            if clothing[x] == wardrobe[y]:
                print(wardrobe[y])


if temp >= 33 and temp <= 54:
    if weatherDescripition == "Clear Sky" or weatherDescription == "Broken Clouds" or weatherDescription == "Scattered Clouds" or weatherDescription == "Few Clouds":
        clothing = ["Coat", "Jacket", "Shirt", "T-shirt", "Jeans", "Pants"]
        for x in clothing and y in wardrobe:
            if clothing[x] == wardrobe[y]:
                print(wardrobe[y])
    elif weatherDescripition == "Light rain" or weatherDescription == "fog" or weatherDescription == "Moderate rain" or weatherDescription == "shower rain":
        clothing = ["Raincoat", "Coat", "Jacket", "Shirt", "T-Shirt", "Jeans", "Pants"]
        for x in clothing and y in wardrobe:
            if clothing[x] == wardrobe[y]:
                print(wardrobe[y])
    elif weatherDescription == "Heavy rain" or weatherDescription == "thunderstorm":
        clothing = ["Raincoat", "Coat", "Jacket", "Shirt", "Jeans", "Pants"]
        for x in clothing and y in wardrobe:
            if clothing[x] == wardrobe[y]:
                print(wardrobe[y])

if temp >= 55 and temp <= 79:
    if weatherDescripition == "Clear Sky" or weatherDescription == "Broken Clouds" or weatherDescription == "Scattered Clouds" or weatherDescription == "Few Clouds":
        clothing = ["Shirt", "T-Shirt", "Trousers", "Jeans", "Pants", "Shorts"]
        for x in clothing and y in wardrobe:
            if clothing[x] == wardrobe[y]:
                print(wardrobe[y])
    elif weatherDescription == "Light rain" or weatherDescription == "fog" or weatherDescription == "Moderate rain" or weatherDescription == "shower rain":
        clothing = ["Raincoat", "T-Shirt", "Shirt", "Trousers", "Jeans", "Pants", "Shorts"]
        for x in clothing and y in wardrobe:
            if clothing[x] == wardrobe[y]:
                print(wardrobe[y])
    elif weatherDescription == "Heavy rain" or weatherDescription == "thunderstorm":
        clothing = ["Raincoat", "Shirt", "T-Shirt", "Jeans", "Pants"]
        for x in clothing and y in wardrobe:
            if clothing[x] == wardrobe[y]:
                print(wardrobe[y])

if temp <= 80:
    if weatherDescripition == "Clear Sky" or weatherDescription == "Broken Clouds" or weatherDescription == "Scattered Clouds" or weatherDescription == "Few Clouds":
        clothing = ["Shirt", "T-Shirt", "Trousers", "Shorts"]
        for x in clothing and y in wardrobe:
            if clothing[x] == wardrobe[y]:
                print(wardrobe[y])
    elif weatherDescription == "Light rain" or weatherDescription == "fog" or weatherDescription == "Moderate rain" or weatherDescription == "shower rain":
        clothing = ["Raincoat", "T-Shirt", "Shorts"]
        for x in clothing and y in wardrobe:
            if clothing[x] == wardrobe[y]:
                print(wardrobe[y])
    elif weatherDescription == "Heavy rain" or weatherDescription == "thunderstorm":
        clothing = ["Raincoat", "T-Shirt", "Pants"]
        for x in clothing and y in wardrobe:
            if clothing[x] == wardrobe[y]:
                print(wardrobe[y])

