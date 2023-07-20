import requests
import json

url = "https://nofluffjobs.com/api/search/posting?page=2&salaryCurrency=PLN&salaryPeriod=month&region=pl"

json_payload = {
	"criteriaSearch":
		{
			"city":[],
			"company":[],
			"category":["devops"],
			"country":[],
			"employment":[],
			"seniority":[],
			"requirement":[],
			"salary":[],
			"more":[],
			"keyword":[],
			"jobLanguage":[],
			"jobPosition":[],
			"province":[],
			"id":[]
		}}



response = requests.post(url, json=json_payload)

data = json.dumps(response.json(),indent=4)

print(data)