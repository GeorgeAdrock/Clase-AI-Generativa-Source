import requests
import pandas as pd

url = "https://jhhqwn3twg.execute-api.us-east-1.amazonaws.com/prod/groups"

headers = {"Authorization": "Bearer "}

response = requests.get(url, headers=headers)


# Convertir datos JSON a DataFrame
df = pd.DataFrame([response])

# Mostrar el DataFrame
print(df.head())
print(response.json())
