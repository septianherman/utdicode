import requests
api_url = "http://127.0.0.1:5000/employees"
todo = [{"id": 1, "name": "Toni"}]
response = requests.post(api_url, json=todo)
print(response.json())
print(response.status_code)