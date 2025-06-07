def get_user_level(score: int) -> tuple[int, str]:
    if score < 5:
        return  "🧠 Estudante Dedicado"
    elif score < 10:
        return  "📘 Aprendiz Curioso"
    elif score < 20:
        return  "📚 Aluno Persistente"
    elif score < 40:
        return  "🧮 Estudioso de Elite"
    else:
        return  "🧠🔥 Mente Brilhante"
