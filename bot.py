# importa l'API de Telegram
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
import skyline
import os
import pickle


def start_message(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text="SkyLineBot\nBenvingut Nil!")


def author_message(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text="SkyLineBot\n@ Nil Fons Miret, 2020")


def help_message(update, context):
    help_text = """
/start - Dóna la benvinguda
/author - Dóna informació sobre l'autor
/help - Mostra les comandes disponibles
/lst - Mostra els identificadors definits i les seves àrees
/clean - Esborra tots els identificadors definits
/save id - Guarda un skyline amb identificador id
/load id - Carrega un skyline amb identificador id

id - Mostra una imatge del skyline amb identificador id, la seva àrea i alçada màxima
id := expr - Guarda en l'identificador id el skyline definit per expr

Creació de skylines:
(xmin, h, xmax) crea un skyline amb un sol edifici
[(xmin1, h1, xmax1), ...] crea un skyline amb diversos edificis
(n, h, w, xmin, xmax) crea n edificis, amb alçades aleatòries entre 0 i h, i amplades aleatòries entre 1 i w, amb inici i final entre xmin i xmax

Operacions amb skylines:
skyline + skyline: unió
skyline * skyline: intersecció
skyline * N: replicació N vegades del skyline
skyline + N: desplaçament a la dreta del skyline N posicions
skyline - N: desplaçament a l'esquerra del skyline N posicions
-skyline: reflexió del skyline
    """
    context.bot.send_message(chat_id=update.effective_chat.id, text=help_text)


def lst(update, context):
    user_id = update.message.chat.id
    create_data_dir(user_id)
    if user_id not in users:
        users[user_id] = {}
    
    skylines = users[user_id]
    if not skylines:
        lst_text = "No hi ha cap skyline desat"
    else:
        lst_text = ""
    for name, skyline in user[user_id].items():
        lst_text += f"Skyline {name}:\n  area: {skyline.area()}\n  alçada: {skyline.height()}\n"

    context.bot.send_message(chat_id=update.effective_chat.id, text=lst_text)


def clean(update, context):
    user_id = update.message.chat.id
    create_data_dir(user_id)
    user[user_id] = {}
    context.bot.send_message(chat_id=update.effective_chat.id, text="Tots els identificadors esborrats")


def create_data_dir(user_id):
    path = os.path.join("data", user_id)
    if not os.path.isdir(path):
        os.makedirs(path)


def save(update, context):
    user_id = update.message.chat.id
    create_data_dir(user_id)
    if user_id not in users:
        users[user_id] = {}
    
    if len(context.args) != 1:
        context.bot.send_message(chat_id=update.effective_chat.id, text="Arguments invàlids. Format: save <id>")
        return

    identifier = context.args[0]

    if identifier not in users[user_id]:
        context.bot.send_message(chat_id=update.effective_chat.id, text="Identificador no trobat")
        return

    path = os.path.join("data", user_id, f"{identifier}.sky")

    with open(path, "wb") as f:
        pickle.dump(skylines[identifier], f)

    context.bot.send_message(chat_id=update.effective_chat.id, text="Skyline desada correctament")


def load(update, context):
    user_id = update.message.chat.id
    create_data_dir(user_id)
    
    if user_id not in users:
        users[user_id] = {}

    if len(context.args) != 1:
        context.bot.send_message(chat_id=update.effective_chat.id, text="Arguments invàlids. Format: load <id>")
        return

    identifier = context.args[0]
    path = os.path.join("data", user_id, f"{identifier}.sky")

    if not os.path.isfile(path):
        context.bot.send_message(chat_id=update.effective_chat.id, text="Identificador no trobat")
        return

    with open(path, "wb") as f:
        skylines[identifier] = pickle.load(f)

    context.bot.send_message(chat_id=update.effective_chat.id, text="Skyline carregada correctament")


def handle_message(update, context):
    # TODO: Parse message
    context.bot.send_message(chat_id=update.effective_chat.id, text=update.message.text)

users = {}

TOKEN = open("token.txt").read().strip()

updater = Updater(token=TOKEN, use_context=True)
dispatcher = updater.dispatcher

dispatcher.add_handler(CommandHandler("start", start_message))
dispatcher.add_handler(CommandHandler("author", author_message))
dispatcher.add_handler(CommandHandler("help", help_message))
dispatcher.add_handler(CommandHandler("lst", lst))
dispatcher.add_handler(CommandHandler("clean", clean))
dispatcher.add_handler(CommandHandler("save", save, pass_args=True))
dispatcher.add_handler(CommandHandler("load", load, pass_args=True))
dispatcher.add_handler(MessageHandler(filters=Filters.text, callback=handle_message))

updater.start_polling()
