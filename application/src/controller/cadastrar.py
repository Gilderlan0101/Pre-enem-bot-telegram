from telegram.ext import ContextTypes
from telegram import Update
from application.src.models.database import register_user  # ou onde estiver sua função
# certifique-se de que register_user está importável corretamente

async def cadastrar_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    mensagem = register_user(update)
    await update.message.reply_text(mensagem)
