from telegram import ReplyKeyboardRemove, InlineKeyboardMarkup, InlineKeyboardButton
from foodfeedbot.buttons import buttons
import requests


states = {
    "animals_type": 1,
    "animal_item": 2,
    "animal_item_type": 3,
    "food": 4,
    "submit": 5,
}


def start_buying(update, context):
    update.message.reply_text("salom ...", reply_markup=ReplyKeyboardRemove())
    update.message.reply_text("Animalslardan bitini tanlang!", reply_markup=buttons.animals)
    return states["animals_type"]


def animals_type(update, context):
    query = update.callback_query
    context.user_data['animal'] = query.data
    query.message.delete()

    print(buttons.animals_item['bird'])
    if buttons.animals_item[f"{query.data}"] == []:
        query.message.reply_text("Hech narsa yo'q !")
    else:
        query.message.reply_text("Animalitemslardan birini tanlang!", reply_markup=InlineKeyboardMarkup(buttons.animals_item[f"{query.data}"]['keyboard']))
        return states["animal_item"]


def animal_item(update, context):
    query = update.callback_query
    context.user_data['animal_type'] = query.data
    query.message.delete()
    query.message.reply_text(f"{query.data}")

    img_data = requests.get(f"""http://172.20.215.79:8000/{buttons.animals_item[f"{context.user_data['animal']}"]['image']}""").content
    with open('tropical.jpg', 'wb') as handler:
        handler.write(img_data)

    context.bot.send_photo(chat_id=query.message.chat_id,
                           photo=open("./tropical.jpg", 'rb'),
                           caption=f"narxi: *500$*\n"
                                   f"nomi : *this is name*", reply_markup=buttons.animals, parse_mode="Markdown")



def animal_item_type(update, context):
    pass


def food(update, context):
    pass



def submit(update, context):
    pass