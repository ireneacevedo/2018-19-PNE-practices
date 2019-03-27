import http.client
import json

# -- API information
HOSTNAME = "api.github.com"
ENDPOINT = "/users/"
GITHUB_ID = input('Introduce a valid user:')
METHOD = "GET"

headers = {'User-Agent': 'http-client'}

conn = http.client.HTTPSConnection(HOSTNAME)

conn.request(METHOD, ENDPOINT + GITHUB_ID, None, headers)

r1 = conn.getresponse()

# -- Print the status
print()
print("Response received: ", end='')
print(r1.status, r1.reason)

text_json = r1.read().decode("utf-8")
conn.close()

# -- Generate the object from the json file
user = json.loads(text_json)

# -- Get some data
login = user['login']
name = user['name']
bio = user['bio']
repos = user['public_repos']

print()
print("User: {}".format(login))
print("Name: {}".format(name))
print("Number of repositories: {}".format(repos))
print("Biography: \n{}".format(bio))