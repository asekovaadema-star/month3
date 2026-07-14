#---HOMEWORK #5 ---
from db.database import get_db 
from db.queries import(INSERT_QUESTIONS, 
                       SELECT_ALL_QUESTIONS,
                       DELETE_QUESTION,
                       GET_QUESTION_BY_ID,
                       UPDATE_USER_SCORE,
                       SELECT_TOP_USERS)

def add_question(question_text:str, corrcet_answer:str):
    conn = get_db()
    conn.execute(INSERT_QUESTIONS, (question_text, corrcet_answer))
    conn.commit()
    conn.close()

def get_all_questions():
    conn = get_db()
    rows = conn.execute(SELECT_ALL_QUESTIONS, ()). fetchall()
    conn.close()
    return [dict(r) for r in rows]

def get_question(question_id: int):
    conn = get_db()
    row = conn.execute(GET_QUESTION_BY_ID, (question_id, )).fetchone()
    conn.close()
    return dict(row) if row else None

def delete_question(id: int):
    conn = get_db()
    conn.execute( DELETE_QUESTION,(id, ))
    conn.commit()
    conn.close()

