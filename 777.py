from pprint import pprint
import requests

names = ['Hulk', 'Captain America', 'Thanos']
def get_a_seperhero(names):
   best_intel = 0
   best_name = None
   for name in names:
      url = f"https://superheroapi.com/api/2619421814940190/search/{name}"
      response = requests.get(url)
      data = response.json()
      intelligence = data['results'][0]['powerstats']['intelligence']
      pprint(f'Интеллект {name} = {intelligence}')
      if int(intelligence) > int(best_intel):
         best_intel = intelligence
         best_name = name
   pprint(f' Самый умный {best_name}')

get_a_seperhero(names)
