🤖 PrepENEMBot

PrepENEMBot é um bot para Telegram projetado para auxiliar estudantes na preparação para o ENEM (Exame Nacional do Ensino Médio). Ele oferece recursos como geração de resumos de estudos, quizzes interativos, e gerenciamento de pontuação e progresso do usuário, utilizando recursos de Inteligência Artificial para conteúdos educativos.

⚙️ Instalação e Configuração

O projeto utiliza o Poetry para gerenciamento de dependências e ambientes virtuais.

1. Pré-requisitos

Certifique-se de ter o Python (versão 3.12 ou superior) e o Poetry instalados.

2. Configuração do Ambiente

Clone o repositório:

git clone [URL_DO_SEU_REPOSITÓRIO]
cd PrepENEMBot


Instale as dependências com Poetry:

poetry install


Ative o ambiente virtual:

poetry shell


3. Variáveis de Ambiente (.env)

Crie um arquivo .env na raiz do projeto para armazenar chaves de API e configurações sensíveis:

# Chave de acesso do seu bot no Telegram (BotFather)
TOKEN="SEU_TELEGRAM_BOT_TOKEN"

# Chave de API para serviços de Inteligência Artificial (OpenAI ou OpenRouter)
API_KEY_IA="SUA_CHAVE_DE_API_PARA_IA"

# Caminho para o banco de dados SQLite (padrão: prep_enem_bot.db)
BANCO="prep_enem_bot.db"


4. Dependências Principais

As dependências listadas no pyproject.toml são instaladas automaticamente pelo Poetry:

Pacote

Função

python-telegram-bot

Framework principal para interação com a API do Telegram.

aiosqlite

Biblioteca assíncrona para operações de banco de dados SQLite.

openai

Utilizado para comunicação com a API de LLMs (via OpenRouter neste projeto).

python-dotenv

Carrega variáveis de ambiente do arquivo .env.

requests

Biblioteca HTTP para chamadas gerais.

🏗️ Arquitetura do Projeto

O bot é organizado seguindo o padrão Controller/View/Model (CVM), focado na separação de responsabilidades para controle de comandos (Controller), lógica de banco de dados (Model) e mensagens ao usuário (View).

Módulos Principais

Arquivo

Categoria

Descrição

main.py

Execução/Core

Ponto de entrada do bot. Inicializa o DB e registra todos os CommandHandlers (rotas) do Telegram, como /start, /resumo, e /quiz.

question.py

Controller/Quiz

Processa o comando /responder. Verifica a resposta do usuário, chama a IA para gerar a explicação e atualiza o score no banco de dados.

resumoIA.py

Controller/IA

Contém as funções de interação com LLMs. Inclui gerar_resumo_com_fallback (com modelos alternativos) e ResponseQuiz para gerar explicações detalhadas das questões. Aplica a limitação de uso.

command_limiter.py

Controller/Limites

Implementa a classe CommandLimiter, responsável por verificar e impor a cota diária de uso para funcionalidades premium (ex: /resumo) para usuários no plano Gratuito.

Módulos de Utilidade e Dados

Arquivo

Categoria

Descrição

perfil.py

Controller/Dados

Define a classe InfoUser que centraliza a busca e formatação dos dados completos do usuário (score, plano, contadores) a partir do banco de dados.

tracker.py

Utils/DB

Função assíncrona increment_command_usage que registra o uso de qualquer comando pelo usuário na coluna command_count do DB.

db_tools.py

Utils/DB

Função genérica incrementar_coluna para atualizar dinamicamente contadores no banco de dados (ex: somar +1 à quantidade de resumos gerados).

get_info_user.py

Utils/Decoração

O decorador @with_user_info injeta automaticamente dados do usuário (user_id, username) nos handlers que o utilizam, simplificando a assinatura das funções.

start.py

Controller/Start

O handler para o comando /start, responsável por saudar o usuário e enviar a mensagem inicial.

messages.py

View/Mensagens

Contém funções de formatação de mensagens, como get_welcome_message e comando_cadastrar, para garantir consistência na comunicação com o usuário.

help.py

View/Ajuda

A função bot_helpers retorna o menu formatado de comandos de ajuda disponíveis no bot.

resumo.py

View/Formatação

Contém a função resum para formatar o texto bruto da IA em um template de resposta amigável para o Telegram.

🚀 Como Executar

Após a instalação das dependências e configuração do arquivo .env, execute o bot a partir do terminal (dentro do ambiente Poetry):

python main.py


O bot será inicializado e começará a escutar comandos no Telegram.
