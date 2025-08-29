import requests

url = "https://render-restapi.onrender.com/bfhl"
payload = {"data": ["a", "1", "334", "4", "R", "$"]}
response = requests.post(url, json=payload)
print(response.json())
