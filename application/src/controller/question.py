import asyncio
from application.src.models.user import get_user_data
from application.src.utils.tracker import increment_command_usage
from application.src.views.messages import get_welcome_message
from application.src.utils.get_info_user import with_user_info


@with_user_info
async def responder_handler(update, context,username):
   

    user = update.effective_user
    user_id = user.id
    check_user = get_user_data(user_id)

    if check_user:
        if increment_command_usage(update):


            resposta_user = context.args[0].upper() if context.args else None

            # Verifica se há uma resposta certa armazenada
            resposta_correta = context.user_data.get("quiz_resposta")
            explicacao = context.user_data.get("quiz_explicacao")

            if not resposta_user or resposta_user not in ["A", "B", "C", "D"]:
                await update.message.reply_text("❗Use: /responder A, B, C ou D")
                return

            if not resposta_correta:
                await update.message.reply_text("❗Nenhuma pergunta foi feita ainda. Use /quiz para começar.")
                return

            if resposta_user == resposta_correta:
                pontos = 10  # Pontuação se acertar
                await update.message.reply_text(
                    f"✅ Resposta correta, {user.first_name}! Você ganhou +{pontos} pontos.\n"
                    f"📚 Explicação: {explicacao}"
                )
                # Aqui você pode salvar os pontos no banco ou na memória
                context.user_data["score"] = context.user_data.get("score", 0) + pontos
            else:
                await update.message.reply_text(
                    f"❌ Resposta errada, {username}.\n"
                    f"📚 Explicação: {explicacao}"
                )

            # Atualizando contagem de uso de comandos
            # Limpa os dados para a próxima pergunta
            context.user_data["quiz_resposta"] = None
            context.user_data["quiz_explicacao"] = None

    
    else:
        message_default = get_welcome_message()
        await asyncio.sleep(1)
        await update.message.reply_text(message_default)
