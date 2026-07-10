#---CREATE TABLES ---

CREATE_USERS_TABLES = """
    CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        telegram_id INTEGER NOT NULL UNIQUE,
        username TEXT
    )
"""

CREATE_QESTIONS_TABLE = """
    CREATE TABLE IF NOT EXISTS questions (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        question_text TEXT NOT NULL,
        correct_answer TEXT NOT NULL
    )  
"""

CREATE_RESULTS_TABLE = """
    CREATE TABLE IF NOT EXISTS results(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        user_id INTEGER NOT NULL, 
        question_id INTEGER NOT NULL, 
        is_correct BOOLEAN NOT NULL DEFAULT 0, 

        FOREIGN KEY (user_id) REFERENCES users(id) ON DELETE CASCADE,
        FOREIGN KEY (question_id) REFERENCES questions(id) ON DELETE CASCADE 
    )   
"""

# --USERS -- 
GET_USER_BY_TELEGRAM_ID = "SELECT * FROM users WHERE telegram_id = ?"

INSERT_USERS = 'INSERT OR IGNORE INTO users(telegram_id) VALUES (?, ?)'

UPDATE_USERNAME = 'UPDATE users SET username = ? WHERE telegram_id = ? '

DELETE_USER = "DELETE FROM users WHERE telegram_id = ?"


#-- RESULTS --

INSERT_RESULT = "INSERT INTO results(user_id, questions_id, is_correct) VALUES (?,?,?)"

GET_SCORE_BY_USER_ID = "SELECT COUNT(*) as total, SUM(is_correct) as correct FROM results WHERE user_id = ?"


#--HOMEWORK #5 ---
INSERT_QUESTIONS = "INSERT INTO questions(question_text, correct_answer) VALUES (?, ?)"

SELECT_ALL_QUESTIONS = "SELECT * FROM questions "

DELETE_QUESTION = "DELETE FROM questions WHERE id= ?"