import requests
import json

# Send a GET request to the desired API URL
response = requests.get('https://justjoin.it/api/offers')

# Parse the response and print it
data = response.json()
print(data)

# # Using a JSON string
# with open('json_data.json', 'w') as outfile:
#     outfile.write(str(x.content))

my_list = []

with open('fff.json', 'r') as json_file:
    data = json.load(json_file)
    # print(type(json_file))
    # print(json_file.read())
    # my_file = json_file.read()
    s = json.dumps(data, indent=4)
    # print(len(s))

for offer in data:
    print(offer['title'])
    my_list.append(offer['title'])

print(len(my_list))

