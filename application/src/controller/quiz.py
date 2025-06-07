import asyncio
from application.src.models.user import get_user_data
from application.src.utils.get_info_user import with_user_info
from application.src.views.messages import get_welcome_message
from application.src.views.quiz import quiz_with_points
from application.src.utils.tracker import increment_command_usage


@with_user_info
async def quiz_handler(update, context, user_id, username, first_name):
    assunto = "biologia" 
    check_user = get_user_data(user_id)

    if check_user:
            await increment_command_usage(update)
            texto, pergunta = quiz_with_points(first_name, assunto)

            # Salva a resposta correta temporariamente no contexto
            context.user_data["quiz_resposta"] = pergunta["resposta"]
            context.user_data["quiz_explicacao"] = pergunta["explicacao"]

            await update.message.reply_text(texto)
            await increment_command_usage(update)

    else:
        message_default = get_welcome_message(username)
        await asyncio.sleep(1)
        await update.message.reply_text(message_default)
