# app/views/score.py

def get_score_message(name, data):

    
    score = data.get("score", 0)
    level = data.get("level", 0)
    rank = data.get("rank", "Iniciante")
    commands_used = data.get("command_count", 0)
    time_in_bot = data.get("time_in_bot", "Algum tempo")

    
    return (
        f"📊 Score de {name}:\n\n"
        f"🏆 Pontuação: {score}\n"
        f"📈 Nível: {level} ({rank})\n"
        f"🕹️ Comandos usados: {commands_used}\n"
        f"⏳ Tempo no bot: {time_in_bot}\n\n"
        f"💡 Dica: Use mais comandos e resumos para aumentar seu nível!"
    )

def user_not_register():
    return "👋 Ei! Parece que você ainda não se cadastrou. " \
           " É só usar o comando /cadastrar — rapidinho, coisa de 10 segundos, e já tá pronto pra começar! 🚀"
