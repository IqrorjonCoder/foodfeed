from telegram import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardButton, InlineKeyboardMarkup
import requests

data = requests.get("http://172.20.215.79:8000/api").json()


starter = ReplyKeyboardMarkup([[KeyboardButton("Let's buy 🗒")],
                               [KeyboardButton("basket")]], resize_keyboard=True)

an = []
for i in data['animals']:
    name = i['animal_name']
    an.append([InlineKeyboardButton(f"{name}", callback_data=f"{name}")])
animals = InlineKeyboardMarkup(an)



animals_item = {
    i['animal_name']: {"keyboard": [[InlineKeyboardButton(j['item_name'], callback_data=f"{j['item_name']}")] for j in data['animal_items'] if j['connected_to_animal'] == i['id']],
                       "image": i['image_2']}
    for i in data['animals']}

print(animals_item)