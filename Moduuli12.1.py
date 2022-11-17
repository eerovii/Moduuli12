import requests

request = requests.get('https://dad-jokes.p.rapidapi.com/random/joke')
result = request.json()

print(result['value'])
