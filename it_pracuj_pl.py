import requests
import json


url = "https://massachusetts.pracuj.pl/api/offers?tt=Python&jobBoardVersion=2&rop=20&pn=1"

response = requests.get(url)

data = json.dumps(response.json(),indent=4)

print(data)