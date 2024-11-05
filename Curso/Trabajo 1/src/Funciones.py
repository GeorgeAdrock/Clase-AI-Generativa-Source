import requests

def CrearToken(email): #metodo GET
    url = "https://jhhqwn3twg.execute-api.us-east-1.amazonaws.com/prod/token"
    querystring = {"email":email}
    
    response = requests.get(url, params=querystring)
    
    if response.status_code == 200:
        data = response.json()
        token = data.get("token")
        print(token)
    else:
        print(f"Error: {response.status_code}")
    return token

def CrearGrupo(name,token): #metodo POST
    url = "https://jhhqwn3twg.execute-api.us-east-1.amazonaws.com/prod/groups"
    payload = { "name": name }
    headers = {
        "Authorization": "Bearer "+token,
        "content-type": "application/json"
        }
    response = requests.post(url, json=payload, headers=headers)
    if response.status_code == 200:
        data = response.json()
        IdGroup = data.get("id")
        print(token)
    else:
        print(f"Error: {response.status_code}")
    return IdGroup

def ObtenerGrupos(token): #metodo GET
    url = "https://jhhqwn3twg.execute-api.us-east-1.amazonaws.com/prod/groups"
    
    headers = {"Authorization": "Bearer "+token}

    response = requests.get(url, headers=headers)

    
    if response.status_code == 200:
        data = response.json()
        token = data.get("token")
        print(token)
    else:
        print(f"Error: {response.status_code}")
    return token