import os
import time

from typing import Final
from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, filters, ContextTypes

RESET = "\033[0m"      # Resetta tutti i colori e gli stili
RED = "\033[91m"       # Testo ERRRORI
GREEN = "\033[92m"     # Testo INFO
YELLOW = "\033[93m"    # Testo 
BLUE = "\033[94m"      # Testo blu
MAGENTA = "\033[95m"   # Testo magenta
CYAN = "\033[96m"      # Testo ciano
WHITE = "\033[97m"     # Testo bianco

TOKEN: Final = "6659808718:AAH3-FaACXlG9QZJO5YIPe5gc7Mk93q-WTs"
BOT_USERNAME: Final = "@LAammitbot"

async def start_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("[ ! ] - BOT STARTED")

async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("[ ! ] - SCRIVI QUALCOSA")

async def custom_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("[ ! ] - QUESTO E UN COMANDO ")


    #RISPOSTE

def handle_ripsoste(text: str) -> str:
    modifica_lower: str = text.lower();

    if "ciao" in modifica_lower:
        return "Hey utente"
    
    if "come va?" in modifica_lower:
        return "bene te?"
    
    return "non capisco"


async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    message_type: str = update.message.chat.type
    text: str = update.message.text

    print(f'User ({update.message.chat.id}) in {message_type}: "{text}: "')

    if message_type == 'group':
        if BOT_USERNAME in text:
            new_text: str = text.replace(BOT_USERNAME, '').strip()
            reponse: str = handle_ripsoste(new_text)
        else:
            return
    else:
        reponse: str = handle_ripsoste(text)

    print("Bot:", reponse)
    await update.message.reply_text(reponse)

async def error(update: Update, context: ContextTypes.DEFAULT_TYPE):
    print(f'Update {update} caused error {context.error}')


if __name__ == '__main__':
    print("Starting Bot...")
    app = Application.builder().token(TOKEN).build()

    app.add_handler(CommandHandler('start', start_command))
    app.add_handler(CommandHandler('help', help_command))
    app.add_handler(CommandHandler('custom', custom_command))

    app.add_handler(MessageHandler(filters.TEXT, handle_message))

    app.add_error_handler(error)
    print("polling...")
    app.run_polling(poll_interval=3)

    

