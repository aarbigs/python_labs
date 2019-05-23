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

#This prints the 'first_name' in the 0 element(1st dictionary) of data
print(data['data'][0]['first_name'])

#but I can't figure out how to print the 'first_name' of each in the list of dictionaries?
for dict in data['data']:
    for key, value in dict:
        print(dict[key])




