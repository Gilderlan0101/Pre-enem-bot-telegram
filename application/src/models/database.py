import sqlite3
from application.src.models.cadastro import Usuario

from telegram import Update
from telegram.ext import ContextTypes

def my_db():
    banco = sqlite3.connect("usuarios.db")
    return banco, banco.cursor()

def create_database():
    banco, cursor = my_db()
    cursor.execute(
        """
        CREATE TABLE IF NOT EXISTS usuarios(
            user_id INTEGER PRIMARY KEY,  -- ID do Telegram, único
            username TEXT,
            first_name TEXT,
            data_entrada TEXT DEFAULT CURRENT_TIMESTAMP,
            plano TEXT DEFAULT 'gratuito',
            level INTEGER DEFAULT 1,
            score INTEGER DEFAULT 0,
            tempo_uso INTEGER DEFAULT 0,  -- em minutos ou segundos
            quantidade_resumos INTEGER DEFAULT 0,
            quantidade_quizzes INTEGER DEFAULT 0,
            ultima_atividade TEXT DEFAULT CURRENT_TIMESTAMP,
            command_count  INTEGER DEFAULT 0
        )
        """
    )
    banco.commit()
    banco.close()


def register_user(update: Update):
        
        user = update._effective_user
        obj_usuario = Usuario(
            user_id=user.id,
            username=user.username,
            first_name=user.first_name
        )

        try:
            banco, cursor = my_db()

            cursor.execute("SELECT * FROM usuarios WHERE user_id = ?",(obj_usuario.user_id,))
            resultado = cursor.fetchone()

            if resultado:
                return "✅ Você já está cadastrado."


            cursor.execute("""
            INSERT INTO usuarios(user_id,username,first_name,data_entrada, plano,
                    score,tempo_uso, quantidade_resumos, quantidade_quizzes, ultima_atividade
                    ) VALUES(?,?,?,?,?,?,?,?,?,?)

            """,(obj_usuario.user_id,obj_usuario.username, obj_usuario.first_name, obj_usuario.data_entrada,
                 obj_usuario.plano, obj_usuario.score, obj_usuario.tempo_uso, obj_usuario.quantidade_resumo,
                 obj_usuario.quantidade_quiz, obj_usuario.ultima_atividade,) )


            banco.commit()
            return "🎉 Cadastro realizado com sucesso!"

        except sqlite3.Error as e:
            print("Erro no cadastro:", e)
            return "❌ Ocorreu um erro ao tentar cadastrar. Tente novamente mais tarde."

        finally:
            banco.close()

