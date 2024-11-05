import requests

url = "https://jhhqwn3twg.execute-api.us-east-1.amazonaws.com/prod/groups/01JBDFVQQ09MHBAW4YQHQ1CBKM/join"

payload = {
    "id": "01JBDFVQQ09MHBAW4YQHQ1CBKM",
    "name": "Jorge Araya Vergara"
}
headers = {
    "Authorization": "Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJlbWFpbCI6ImpvcmdlLmFyYXlhLnZlcmdhcmFAZ21haWwuY29tIiwiaWF0IjoxNzMwNjc3Njk4LCJleHAiOjE3MzA2ODEyOTh9.S6R8aVoSCH1VmF9VQes1zhaER9hQ0_D9XeiSoQ51Jqc",
    "content-type": "application/json"
}

response = requests.post(url, json=payload, headers=headers)

print(response.json())