import requests

response = requests.get("127.0.0.1:8000/info/")
response.raise_for_status()
print(response.text)
