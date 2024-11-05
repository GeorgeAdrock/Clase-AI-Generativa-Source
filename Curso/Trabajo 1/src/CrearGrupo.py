import requests

url = "https://jhhqwn3twg.execute-api.us-east-1.amazonaws.com/prod/groups"

payload = { "name": "Grupo para ejercicio " }
headers = {
    "Authorization": "Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJlbWFpbCI6ImpvcmdlLmFyYXlhLnZlcmdhcmFAZ21haWwuY29tIiwiaWF0IjoxNzMwMjQ3MjY0LCJleHAiOjE3MzAyNTA4NjR9.G1H77-JTACl2T8o19jimKHu9UUNmGP5FNlNHhNS87no",
    "content-type": "application/json"
}

response = requests.post(url, json=payload, headers=headers)

print(response.json())