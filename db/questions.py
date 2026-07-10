#---HOMEWORK #5 ---
from db.database import get_db 
from db.queries import(INSERT_QUESTIONS, 
                       SELECT_ALL_QUESTIONS,
                       DELETE_QUESTION)

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

def delete_question(id: int):
    conn = get_db()
    conn.execute( DELETE_QUESTION,(id, ))
    conn.commit()
    conn.close()
