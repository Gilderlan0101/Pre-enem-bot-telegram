import asyncio
from telegram.ext import Application, CommandHandler, MessageHandler
from telegram.ext import filters
from application.src.utils.tracker import increment_command_usage

from application.src.controller.cadastrar import cadastrar_handler
from application.src.controller.question import responder_handler
from application.src.controller.quiz import quiz_handler
from application.src.controller.resumo import resumo_handler
from application.src.controller.start import start_handler
from application.src.controller.score import user_score
from application.src.controller.premium import subscribe_premium
from dotenv import load_dotenv

import os

from application.src.models.database import create_database, my_db


load_dotenv()

BOT_TOKEN = os.getenv("TOKEN")

# Função para conta quantidade de vezes que o usuario usou os comandos:
async def track_commands(update, context):
    if update.message.text.startswith("/"):
        await increment_command_usage(update)

def main() -> None:
   
    my_db()
    create_database()
    
    app = Application.builder().token(BOT_TOKEN).build()
    app.add_handler(CommandHandler("start", start_handler))
    app.add_handler(CommandHandler("score", user_score))
    app.add_handler(CommandHandler("premium", subscribe_premium))
    app.add_handler(CommandHandler("resumo", resumo_handler))
    app.add_handler(CommandHandler("quiz", quiz_handler))
    app.add_handler(CommandHandler("responder", responder_handler))
    app.add_handler(CommandHandler("cadastrar", cadastrar_handler))

   



    print("Bot is running...")
    app.run_polling()

    return app


if __name__ == "__main__":
   main()