import requests

url = "https://jhhqwn3twg.execute-api.us-east-1.amazonaws.com/prod/groups/01JBDFVQQ09MHBAW4YQHQ1CBKM/join"

payload = {
    "id": "01JBDFVQQ09MHBAW4YQHQ1CBKM",
    "name": "Jorge Araya Vergara"
}
headers = {
    "Authorization": "Bearer ",
    "content-type": "application/json"
}

response = requests.post(url, json=payload, headers=headers)

print(response.json())
