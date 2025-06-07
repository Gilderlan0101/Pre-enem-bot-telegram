
class Usuario:
    """Objeto de cadastro de usuario."""
    def __init__(self, user_id, username, first_name,
                 data_entrada=None, plano="Gratuito", score=0,
                tempo_uso=0, quantidade_resumo=0, quantidade_quiz=0, ultima_atividade=None ):
        
        
        self.user_id = user_id
        self.username = username or "Sem username"
        self.first_name = first_name
        self.data_entrada = data_entrada or self.data_atual()

        self.plano = plano
        self.score = score
        self.tempo_uso = tempo_uso
        
        self.quantidade_resumo = quantidade_resumo
        self.quantidade_quiz = quantidade_quiz
        self.ultima_atividade = ultima_atividade or self.data_atual()


    def data_atual(self):
        from datetime import datetime
        return datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    