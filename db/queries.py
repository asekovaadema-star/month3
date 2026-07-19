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

#--LESSON 6 ---
GET_QUESTION_BY_ID = 'SELECT * FROM questions WHERE id = ?'

#--HOMEWORK#6 --
UPDATE_USER_SCORE = 'INSERT INTO users (telegram_id, username, score) VALUES (?, ?, 1) ON CONFLICT(telegram_id) DO UPDATE SET score = score + 1'

SELECT_TOP_USERS = "SELECT username, score FROM users ORDER BY score DESC LIMIT 3"



GET_HISTORY = '''
        SELECT q.question_text, r.is_correct 
        FROM results AS r
        INNER JOIN users AS u 
            ON u.id = r.user_id 
        
        INNER JOIN question AS q
            ON q.id = r.question_id
        
        WHERE r.telegram_id = ?
        ORDER BY r.id DESC 
        LIMIT 5
 '''