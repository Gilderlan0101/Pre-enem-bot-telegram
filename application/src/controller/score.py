from application.src.models.user import get_user_data
from application.src.utils.level import get_user_level
from application.src.views.messages import get_welcome_message
from application.src.views.user_score import get_score_message, user_not_register
from application.src.utils.tracker import increment_command_usage
import asyncio



async def user_score(update, context):
    user = update.effective_user
    user_id = user.id

    # Busca os dados do banco
    score_data = get_user_data(user_id) or {}

    if score_data:


        # Tratamento seguro dos dados
        score_value = score_data.get("score")
        level = score_data.get("level")
        commands_used = score_data.get("commands_used")  
        time_in_bot = score_data.get("login_time", "Algum tempo")
        command_count = score_data.get('command_count')

        # Determina o rank com base no score
        rank = get_user_level(score_value)

        # Monta o dicionário com dados tratados
        dates = {
            "score": score_value,
            "commands_used": commands_used,
            "level": level,
            "time_in_bot": time_in_bot,
            "rank": rank,
            "command_count": command_count
        }

        # Gera a mensagem final
        message = get_score_message(user.first_name or "Estudante", dates)

        # Envia a resposta
        await update.message.reply_text(message)
        # Atualizando contador 
        await increment_command_usage(update)

    else:
        message = user_not_register()
        message_default = get_welcome_message()
        await update.message.reply_text(message)
        await asyncio.sleep(1)
        await update.message.reply_text(message_default)
