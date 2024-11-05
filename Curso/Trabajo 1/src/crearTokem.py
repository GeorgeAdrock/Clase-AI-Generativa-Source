import requests

url = "https://jhhqwn3twg.execute-api.us-east-1.amazonaws.com/prod/token"

querystring = {"email":"jorge.araya.vergara@gmail.com"}

response = requests.get(url, params=querystring)

if response.status_code == 200:
    data = response.json()
    token = data.get("token")
    print(token)
else:
    print(f"Error: {response.status_code}")

print(token)
    