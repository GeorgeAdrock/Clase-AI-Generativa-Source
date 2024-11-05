import requests
import pandas as pd

url = "https://jhhqwn3twg.execute-api.us-east-1.amazonaws.com/prod/groups"

headers = {"Authorization": "Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJlbWFpbCI6ImpvcmdlLmFyYXlhLnZlcmdhcmFAZ21haWwuY29tIiwiaWF0IjoxNzMwNjc3Njk4LCJleHAiOjE3MzA2ODEyOTh9.S6R8aVoSCH1VmF9VQes1zhaER9hQ0_D9XeiSoQ51Jqc"}

response = requests.get(url, headers=headers)


# Convertir datos JSON a DataFrame
df = pd.DataFrame([response])

# Mostrar el DataFrame
print(df.head())
print(response.json())