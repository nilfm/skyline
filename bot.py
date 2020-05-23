from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
import telegram
from cl.SkylineLexer import SkylineLexer
from cl.SkylineParser import SkylineParser
from cl.EvalVisitor import EvalVisitor
from Skyline import Skyline, Point, WrongArgumentException
import os
import pickle
import sys
from antlr4 import *


def start_message(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text="SkyLineBot\nBenvingut Nil!")


def author_message(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text="SkyLineBot\nNil Fons Miret, 2020\nnil.fons@est.fib.upc.edu")


def help_message(update, context):
    help_text = """
*Comandes*
`/start` - Dóna la benvinguda
`/author` - Dóna informació sobre l'autor
`/help` - Mostra les comandes disponibles
`/lst` - Mostra els identificadors definits i les seves àrees
`/clean` - Esborra tots els identificadors definits
`/save id` - Guarda un skyline amb identificador `id`
`/load id` - Carrega un skyline amb identificador `id`

`expr` - Mostra una imatge del skyline definit per `expr`, la seva àrea i alçada màxima
`id` - Mostra una imatge del skyline amb identificador `id`, la seva àrea i alçada màxima
`id := expr` - Guarda en l'identificador `id` el skyline definit per `expr`

*Creació de skylines*
`(xmin, h, xmax)` crea un skyline amb un sol edifici
`[(xmin1, h1, xmax1), ...]` crea un skyline amb diversos edificis
`(n, h, w, xmin, xmax)` crea `n` edificis, amb alçades aleatòries entre 0 i `h`, i amplades aleatòries entre 1 i `w`, amb inici i final entre `xmin` i `xmax`

*Operacions amb skylines*
`skyline + skyline`: unió
`skyline \* skyline`: intersecció
`skyline \* N`: replicació `N` vegades del skyline
`skyline + N`: desplaçament a la dreta del skyline `N` posicions
`skyline - N`: desplaçament a l'esquerra del skyline `N` posicions
`-skyline`: reflexió del skyline
    """
    context.bot.send_message(chat_id=update.effective_chat.id, text=help_text, parse_mode=telegram.ParseMode.MARKDOWN)


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

    for name, sky in skylines.items():
        lst_text += f"Skyline {name}:\n    area: {sky.area()}\n    alçada: {sky.height()}\n"

    context.bot.send_message(chat_id=update.effective_chat.id, text=lst_text)


def clean(update, context):
    user_id = update.message.chat.id
    create_data_dir(user_id)
    users[user_id].clear()
    context.bot.send_message(chat_id=update.effective_chat.id, text="Tots els identificadors esborrats")


def create_data_dir(user_id):
    path = os.path.join("data", str(user_id))
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

    path = f"data/{user_id}/{identifier}.sky"

    with open(path, "wb") as f:
        pickle.dump(users[user_id][identifier], f, protocol=pickle.HIGHEST_PROTOCOL)

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
    path = f"data/{user_id}/{identifier}.sky"

    if not os.path.isfile(path):
        context.bot.send_message(chat_id=update.effective_chat.id, text="Identificador no trobat")
        return

    with open(path, "rb") as f:
        users[user_id][identifier] = pickle.load(f)

    context.bot.send_message(chat_id=update.effective_chat.id, text="Skyline carregada correctament")


def parse_text(text, skylines):
    input_stream = InputStream(text)

    lexer = SkylineLexer(input_stream)
    token_stream = CommonTokenStream(lexer)
    parser = SkylineParser(token_stream)
    tree = parser.root()

    visitor = EvalVisitor(skylines)
    return visitor.visit(tree)


def handle_message(update, context):
    user_id = update.message.chat.id
    create_data_dir(user_id)

    if user_id not in users:
        users[user_id] = {}

    text = update.message.text
    try:
        sky = parse_text(text, users[user_id])
        response = f"area: {sky.area()}\nalçada: {sky.height()}"
        context.bot.send_photo(chat_id=update.effective_chat.id, photo=sky.plot())
        context.bot.send_message(chat_id=update.effective_chat.id, text=response)
    except WrongArgumentException as e:
        context.bot.send_message(chat_id=update.effective_chat.id, text=f"Error: {e}")
    except Exception as e:
        context.bot.send_message(chat_id=update.effective_chat.id, text="No he entès el teu missatge :(")


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
