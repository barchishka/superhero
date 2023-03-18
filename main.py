import requests

url = "https://akabab.github.io/superhero-api/api/all.json"
resp = requests.get(url)
heroes_list = ['Hulk', 'Captain America', 'Thanos']
response = resp.json()

intelligence = []

for value in response:
    result = value['powerstats']['intelligence']
    if value['name'] in heroes_list:
        intelligence.append(result)

full_heroes_list = dict(zip(heroes_list, intelligence))

maximum = max(full_heroes_list, key=full_heroes_list.get)
print(f'Самый умный супергерой -', maximum)
