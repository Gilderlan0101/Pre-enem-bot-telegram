from application.src.models.database import register_user

from telegram import Update
from telegram.ext import ContextTypes

def get_welcome_message(username):
    if username != None:
        return f"👋 Olá, {username}!\nSeja bem-vindo ao PreEnemBot!\nUse /resumo, /quiz, /premium, /score ou /cadastrar para começar."
    else:
        return f"👋 Olá!\nSeja bem-vindo(a) ao PreEnemBot!\nUse /cadastrar para começar."


# envio de resposta ao usuario que esta se cadastrando
# Caso não tenha erros (Mensagem positiva) Caso tenha erro (Mensagem negativa)
async def comando_cadastrar(update: Update, context: ContextTypes.DEFAULT_TYPE):
    mensagem = register_user(update)
    await update.message.reply_text(mensagem)
