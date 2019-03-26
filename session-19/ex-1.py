import http.client
import json



def info(HOSTNAME,ENDPOINT,METHOD):
    headers = {'User-Agent': 'http-client'}

# -- Connect to the server

    conn = http.client.HTTPConnection(HOSTNAME)

# -- Send the request
    conn.request(METHOD, ENDPOINT, None, headers)

# -- Wait for the server's response
    r1 = conn.getresponse()

# -- Print the status
    print()
    print("Response received: ", end='')
    print(r1.status, r1.reason)

# -- Read the response's body and close
# -- the connection
    text_json = r1.read().decode("utf-8")
    conn.close()

# -- Generate the object from the json file
    data = json.loads(text_json)

    return data


HOSTNAME = "api.icndb.com"
METHOD = "GET"

randomjoke = info(HOSTNAME,'/jokes/random',METHOD,)
joke = randomjoke['value']['joke']

totaljokes = info(HOSTNAME,'/jokes/count',METHOD)
number = totaljokes['value']

categories = info(HOSTNAME,'/categories',METHOD)
j_categories = categories['value']


# -- Print the received URL
print("Random joke:{} ".format(joke))
print('Number of total jokes available:{}'.format(number))
print('Number of different jokes categories:{}'.format(j_categories))
