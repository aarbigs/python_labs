'''
Using the requests package, make a GET request to the api behind this endpoint:

    http://demo.codingnomads.co:8080/tasks_api/users

Print out:

    - the status code
    - the encoding of the response
    - the text of the response body



'''

import requests
from pprint import pprint
#
base_url = "http://demo.codingnomads.co:8080/tasks_api/users"
response = requests.get(base_url)
# print(response.status_code)

params = {
    "email": "ryan@codingnomads.co"
}


data = response.json()
pprint(data)

for k in (data['data'].keys):
    print(k)
# print(data['data'][2]['first_name'])


