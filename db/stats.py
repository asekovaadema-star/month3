from db.database import get_db 
from db.queries import GET_HISTORY

def get_history(telegam_id: int):
    conn = get_db()
    rows = conn.execute(GET_HISTORY, (telegam_id, )).fetchall()
    conn.close()
    return [dict(r) for r in rows]
