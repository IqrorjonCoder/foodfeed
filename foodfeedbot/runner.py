from telegram.ext import Updater, CommandHandler, ConversationHandler, MessageHandler, Filters, CallbackQueryHandler
from foodfeedbot.buttons import buttons
from buying import buying


def hello(update, context):
    update.message.reply_text("Salom testing...", parse_mode="Markdown",
                              reply_markup=buttons.starter)

def running():
    updater = Updater(token="5654960371:AAEYokGjPZkAE1Ov5Dmf6JeyipUvxJCh2NM", use_context=True)
    dispatcher = updater.dispatcher

    dispatcher.add_handler(CommandHandler('start', hello))

    dispatcher.add_handler(ConversationHandler(
      entry_points=[MessageHandler(Filters.regex("(Let's buy 🗒)"), buying.start_buying)],
        states={
            1: [CallbackQueryHandler(buying.animals_type)],
            2: [CallbackQueryHandler(buying.animal_item)],
            3: [CallbackQueryHandler(buying.animal_item_type)],
            4: [CallbackQueryHandler(buying.food)],
            5: [CallbackQueryHandler(buying.submit)],
        },
        fallbacks=[CommandHandler('stop', hello)]
    ))

    updater.start_polling()
    updater.idle()


if __name__ == '__main__':
    print("ishga tushdi ...")
    running()