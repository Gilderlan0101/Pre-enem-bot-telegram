
│
├── app/
│   ├── __init__.py
│   ├── main.py          # Inicia o bot e faz os imports
│   │
│   ├── models/          # Modelos e lógica de banco de dados
│   │   ├── __init__.py
│   │   ├── user.py       # Classe User, pontuação etc.
│   │   └── database.py   # Conexão com SQLite ou outro banco
│   │
│   ├── controllers/     # Lógica dos comandos
│   │   ├── __init__.py
│   │   ├── start.py
│   │   ├── resumo.py
│   │   ├── quiz.py
│   │   ├── score.py
│   │   └── premium.py
│   │
│   ├── views/           # Funções que retornam mensagens formatadas
│   │   ├── __init__.py
│   │   ├── messages.py   # Mensagens de boas-vindas, erros etc.
│   │   └── templates.py  # Formatação de texto, markdown, etc.
│   │
│   ├── utils/           # Funções auxiliares
│   │   ├── __init__.py
│   │   ├── helpers.py
│   │   └── scoring.py    # Pontuação, cálculo de XP
│
├── bot_config.py        # Token, variáveis de ambiente
├── requirements.txt     # Dependências
└── README.md# Pre-enem-bot-telegram
