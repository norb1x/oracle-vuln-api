# vulnerable_queries.py
from db import get_connection

def vulnerable_login(username, password):
    conn = get_connection()
    cur = conn.cursor()

    # PODATNE – sklejany string → SQLi
    query = f"""
        SELECT username, role
        FROM users
        WHERE username = '{username}' AND password = '{password}'
    """

    print("[VULN LOGIN QUERY]", query)
    cur.execute(query)
    result = cur.fetchone()

    cur.close()
    conn.close()
    return result


def vulnerable_dump(search):
    """
    Celowo podatne zapytanie pod UNION-based SQLi.  ## ❌ VULNERABLE: UNION SQL Injection possible here
    """
    conn = get_connection()
    cur = conn.cursor()

    query = f"""
        SELECT username, password, role
        FROM users
        WHERE username = '{search}'
    """

    print("[VULN DUMP QUERY]", query)
    cur.execute(query)
    rows = cur.fetchall()

    cur.close()
    conn.close()
    return rows

