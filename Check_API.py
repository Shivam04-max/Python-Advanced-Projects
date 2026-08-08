import requests
request = requests.get('https://learnwithshivamhiray.pythonanywhere.com')
data = request.json()

print(data)