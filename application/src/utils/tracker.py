import sqlite3
import aiosqlite
import os
from dotenv import load_dotenv
from application.src.views.messages import get_welcome_message

load_dotenv()

async def increment_command_usage(update):
    user = update.effective_user
    username = user.username
    user_id = user.id

    try:
        async with aiosqlite.connect(os.getenv("BANCO")) as conn:
            cursor = await conn.cursor()

            # Verifica se o usuário existe
            await cursor.execute("SELECT 1 FROM usuarios WHERE user_id = ?", (user_id,))
            result = await cursor.fetchone()

            if result:
                await cursor.execute(
                    "UPDATE usuarios SET command_count = command_count + 1 WHERE user_id = ?",
                    (user_id,)
                )
                await conn.commit()
                
            else:
                print(f"Usuário {user_id} tentou usar um comando mas não está cadastrado.")
                message_default = get_welcome_message(username)
                await update.message.reply_text(message_default)

    except sqlite3.Error as e:
        return "❌ Ocorreu um erro ao tentar cadastrar. Tente novamente mais tarde."

