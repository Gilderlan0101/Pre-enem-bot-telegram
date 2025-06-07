from application.src.models.database import my_db


def get_user_data(user_id):

    banco, cursor = my_db()

    cursor.execute("""
        SELECT user_id, first_name, data_entrada, plano, score,
               tempo_uso, quantidade_resumos, quantidade_quizzes, ultima_atividade, level, command_count
        FROM usuarios WHERE user_id = ?
    """, (user_id,))

    user = cursor.fetchone()

    banco.close()
    

    if user:
        return {
            "user_id": user[0],
            "name": user[1],
            "start": user[2],
            "plan": user[3],
            "score": user[4],
            "login_time": user[5],
            "quantity_summary": user[6],
            "quantity_quiz": user[7],
            "last_activity": user[8],
            "level":user[9],
            "command_count": user[10]
        }
       
    else:
        return {}
