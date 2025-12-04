import logging
import os

from dotenv import load_dotenv
from openai import OpenAI
from telegram.ext import ContextTypes

from application.src.controller.command_limiter import CommandLimiter
from application.src.controller.premium import SubscribePremium
from application.src.models.user import get_user_data
from application.src.utils.db_tools import incrementar_coluna
from application.src.utils.get_info_user import with_user_info
from config import request_plan_free

# Carregando variaves de ambiente
load_dotenv()


def gerar_resumo_com_fallback(username, assunto):
    prompt = (
        f'Olá, meu nome é {username}. Preciso de um resumo claro e direto sobre o tema "{assunto}".\n'
        'Explique como se fosse para um estudante do ensino médio revisando para o ENEM.\n'
        'Use **somente português**, com no máximo 10 linhas, linguagem acessível e objetiva.\n'
        'Evite termos técnicos difíceis. Não escreva absolutamente nada em inglês.'
    )

    client = OpenAI(
        base_url='https://openrouter.ai/api/v1',
        api_key=os.getenv('API_KEY_IA'),
        timeout=20,
        project='PreEnemBot',
    )

    modelos = ['openai/codex-mini', 'openai/gpt-3.5-turbo']

    for modelo in modelos:
        try:
            response = client.chat.completions.create(
                model=modelo,
                messages=[{'role': 'user', 'content': prompt}],
                max_tokens=500,
            )

            content = getattr(
                response.choices[0].message, 'content', ''
            ).strip()
            if content:
                print(f'✅ Modelo usado: {modelo}')
                return content, None

        except Exception as e:
            logging.warning(f"[Fallback IA] Modelo '{modelo}' falhou: {e}")

    return (
        '⚠️ Não foi possível gerar um resumo no momento. Tente novamente mais tarde.',
        None,
    )


@with_user_info
async def resum_of_IA(update, context, username, user_id=None, assunto=None):
    try:
        if not user_id:
            return '❌ Erro: usuário não identificado.', None

        # ✅ Verificar se o usuário atingiu o limite
        limitador = CommandLimiter(user_id)
        liberado = limitador.user_quota_resum
        if not liberado:
            await SubscribePremium().subscribe(update=update, context=context)
            return

        # ✅ Verifica o plano (extra segurança)
        user_data = get_user_data(user_id=user_id)
        plano = user_data.get('plan', '')

        if plano != 'Gratuito':
            return request_plan_free['message_plan'], None

        if not assunto:
            return '❌ Assunto não especificado.', None

        # ✅ Geração com fallback
        content, erro = gerar_resumo_com_fallback(username, assunto)
        if erro:
            return content, erro

        # ✅ Atualizar contagem
        incrementar_coluna(
            nome_tabela='usuarios',
            coluna='quantidade_resumos',
            user_id=user_id,
            incremento=1,
        )

        return content, None

    except Exception as e:
        logging.error(f'[Erro em resum_of_IA]: {e}')
        return (
            '❌ Erro interno ao gerar o resumo. Tente novamente mais tarde.',
            None,
        )


def ResponseQuiz(context: ContextTypes, resposta_usuario=None, UserID=None):
    try:
        if not UserID:
            return '❌ Erro: usuário não identificado.', None

        user_data = get_user_data(user_id=UserID)
        plano = user_data.get('plan', '')

        if plano != 'Gratuito':
            return request_plan_free['message_plan'], None

        client = OpenAI(
            base_url='https://openrouter.ai/api/v1',
            api_key=os.getenv('API_KEY_IA'),
            timeout=20,
            project='PreEnemBot',
        )

        # Recuperar dados da pergunta
        pergunta = context.user_data.get('pergunta')
        resposta_correta = context.user_data.get('quiz_resposta')

        if not pergunta or not resposta_correta:
            return (
                '❌ Não foi possível recuperar a questão enviada anteriormente.',
                None,
            )

        if not resposta_usuario:
            return (
                '❌ Você precisa informar sua resposta (ex: A, B, C ou D).',
                None,
            )

        # 🧠 Novo prompt: IA explica apenas a alternativa correta
        prompt = (
            f'Você é um professor explicando a questão de um simulado do ENEM.\n\n'
            f"🔸 Pergunta: {pergunta['pergunta']}\n"
            f'🔸 Opções:\n'
            f"   A) {pergunta['opcoes'][0]}\n"
            f"   B) {pergunta['opcoes'][1]}\n"
            f"   C) {pergunta['opcoes'][2]}\n"
            f"   D) {pergunta['opcoes'][3]}\n\n"
            f'✅ A resposta correta é: {resposta_correta}\n'
            f'📚 Explique por que essa alternativa está certa de forma clara, direta e educativa para um estudante de ensino médio.'
        )

        response = client.chat.completions.create(
            model='openai/gpt-3.5-turbo',
            messages=[{'role': 'user', 'content': prompt}],
            max_tokens=600,
        )

        content = getattr(response.choices[0].message, 'content', '').strip()
        if not content:
            return (
                '⚠️ Não foi possível gerar uma explicação agora. Tente novamente em breve.',
                None,
            )

        return content, None

    except Exception as e:
        logging.error(f'[Erro em ResponseQuiz]: {e}')
        return (
            '❌ Erro interno ao gerar o feedback. Tente novamente mais tarde.',
            None,
        )
