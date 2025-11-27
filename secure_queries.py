# secure_queries.py
from db import get_connection

def secure_login(username, password):
    conn = get_connection()
    cur = conn.cursor()

    query = """
        SELECT username, role
        FROM users
        WHERE username = :u AND password = :p
    """

    cur.execute(query, {"u": username, "p": password})
    result = cur.fetchone()

    cur.close()
    conn.close()
    return result
