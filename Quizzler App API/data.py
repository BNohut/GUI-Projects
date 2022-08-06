import requests
parameters = {
    "amount": "10",
    "type": "boolean"
}

response = requests.get(url=f"https://opentdb.com/api.php", params=parameters)
question_data = response.json()["results"]
