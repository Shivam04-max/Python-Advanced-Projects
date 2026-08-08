import requests
request = requests.get('')
data = request.json()

print(data)
