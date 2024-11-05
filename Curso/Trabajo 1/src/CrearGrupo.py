import requests

url = "https://jhhqwn3twg.execute-api.us-east-1.amazonaws.com/prod/groups"

payload = { "name": "Grupo para ejercicio " }
headers = {
    "Authorization": "Bearer ",
    "content-type": "application/json"
}

response = requests.post(url, json=payload, headers=headers)

print(response.json())
