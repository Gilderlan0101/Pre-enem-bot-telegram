import random

def quiz_with_points(username, assunto):
    # Pergunta fake com opções (você pode depois colocar reais ou puxar de um banco)
    perguntas = [
        {
            "pergunta": "Qual é a função do ribossomo?",
            "opcoes": [
                "Produzir proteínas",
                "Armazenar DNA",
                "Realizar digestão",
                "Controlar a célula"
            ],
            "resposta": "A",  # Letra da opção correta
            "explicacao": "Ribossomos produzem proteínas na célula."
        },
        {
            "pergunta": "Qual é a fórmula da água?",
            "opcoes": [
                "CO2",
                "H2O",
                "O2",
                "H2"
            ],
            "resposta": "B",
            "explicacao": "A fórmula da água é H2O, composta por dois átomos de hidrogênio e um de oxigênio."
        },
    ]

    pergunta = random.choice(perguntas)

    texto = (
        f"🧠 {username}, vamos testar seus conhecimentos em {assunto.capitalize()}!\n\n"
        f"❓ {pergunta['pergunta']}\n\n"
        f"A) {pergunta['opcoes'][0]}\n"
        f"B) {pergunta['opcoes'][1]}\n"
        f"C) {pergunta['opcoes'][2]}\n"
        f"D) {pergunta['opcoes'][3]}\n\n"
        f"💬 Responda com /responder A, B, C ou D"
    )

    return texto, pergunta  # retorna também a pergunta para você poder armazenar e validar depois
