import requests
response = requests.get('https://uk.wikipedia.org/')
print(type(response.text))