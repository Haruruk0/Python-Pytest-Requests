import requests

URL = 'https://api.pokemonbattle.me/v2'
TOKEN = 'USER_TOKEN'
HEADER = {'Content-Type':'application/json','trainer_token':TOKEN}
body_registration= {
    "trainer_token": TOKEN,
    "email": "harurugity@gmail.com",
    "password": "2NQ-emF-VKq-vCw"
}

body_confirmation = {
    "trainer_token": "96fec3181f746766dabd3a40b563a1e3"
}
body_create = {
    
    "name": "generate",
    "photo": "generate"

}
body_newname = {
    
    "pokemon_id": "146790",
    "name": "meow",
    "photo": "https://dolnikov.ru/pokemons/albums/008.png"

}
body_pokeboll = {
    
    "pokemon_id": "146790"

}
response = requests.post(url = f'{URL}/trainers/reg',headers = HEADER,json = body_registration)
print(response.text)
response_confirmation = requests.post(url = f'{URL}/trainers/confirm_email',headers = HEADER,json = body_confirmation)
print(response_confirmation.text)
response_create = requests.post(url = f'{URL}/pokemons',headers = HEADER,json = body_create)
print(response_create.text)
response_newname = requests.put(url = f'{URL}/pokemons',headers = HEADER,json = body_newname)
print(response_newname.text)
response_pokeboll = requests.post(url = f'{URL}/trainers/add_pokeball',headers = HEADER,json = body_pokeboll)
print(response_pokeboll.text)