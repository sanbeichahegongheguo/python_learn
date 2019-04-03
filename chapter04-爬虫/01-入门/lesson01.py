import requests
response = requests.get('https://privacycommons.github.io/')
print(response)
start = '<a>'
end = '</a>'
print(response[len(start):-len(end)])