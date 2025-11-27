# db.py
import oracledb

def get_connection():
    return oracledb.connect(
        user="secuser",
        password="SecPass123",
        dsn="localhost:1521/xepdb1"
    )
