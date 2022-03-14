import requests
  
def get_poke_info(name):
    istek = requests.get(f'https://pokeapi.co/api/v2/pokemon/{name}')
    if istek.ok:
        data = istek.json()
        po_name = data['name']
        weight = data['weight']
        height = data['height']
        abilities = {i['ability']['name'] for i in data['abilities']} 
        types = {i['type']['name'] for i in data['types']}
        images = data['sprites']['other']['official-artwork']['front_default']
        return po_name
    else:
        return istek.status_code

