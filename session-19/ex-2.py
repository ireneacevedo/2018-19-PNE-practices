import http.client
import json

# -- API information
HOSTNAME = "www.metaweather.com"
city = input('Enter the name of a capital city:')
city = city.lower()
ENDPOINT = "/api/location/search/?query={}".format(city)
METHOD = "GET"

headers = {'User-Agent': 'http-client'}

conn = http.client.HTTPSConnection(HOSTNAME)

conn.request(METHOD, ENDPOINT, None, headers)

r1 = conn.getresponse()

# -- Print the status
print()
print("Response received: ", end='')
print(r1.status, r1.reason)

# -- Read the response's body and close
text_json = r1.read().decode("utf-8")
conn.close()

# -- Generate the object from the json file
weather = json.loads(text_json)

# -- Get the data
woeid = weather[0]['woeid']


HOSTNAME = "www.metaweather.com"
ENDPOINT = "/api/location/{}".format(woeid)
LOCATION_WOEID = str(woeid)
METHOD = "GET"

headers = {'User-Agent': 'http-client'}

conn = http.client.HTTPSConnection(HOSTNAME)


conn.request(METHOD, ENDPOINT + LOCATION_WOEID + '/', None, headers)

r1 = conn.getresponse()


print()
print("Response received: ", end='')
print(r1.status, r1.reason)


text_json = r1.read().decode("utf-8")
conn.close()

weather = json.loads(text_json)

time = weather['time']

temp0 = weather['consolidated_weather'][0]
description = temp0['weather_state_name']
temp = temp0['the_temp']
place = weather['title']

print()
print("Place: {}".format(place))
print("Time: {}".format(time))
print("Weather description: {}".format(description))
print("Current temp: {} degrees".format(temp))
