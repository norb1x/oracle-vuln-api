# app.py
from flask import Flask, request, jsonify
from vulnerable_queries import vulnerable_login, vulnerable_dump
from secure_queries import secure_login


app = Flask(__name__)

@app.route("/login_vuln", methods=["POST"])
def login_vuln():
    data = request.json
    username = data.get("username")
    password = data.get("password")

    user = vulnerable_login(username, password)
    if user:
        return jsonify({"status": "OK", "message": "Logged in (VULN)", "user": user[0], "role": user[1]})
    else:
        return jsonify({"status": "ERROR", "message": "Invalid credentials"}), 401


@app.route("/login_secure", methods=["POST"])
def login_secure_route():
    data = request.json
    username = data.get("username")
    password = data.get("password")

    user = secure_login(username, password)
    if user:
        return jsonify({"status": "OK", "message": "Logged in (SECURE)", "user": user[0], "role": user[1]})
    else:
        return jsonify({"status": "ERROR", "message": "Invalid credentials"}), 401

@app.route("/dump_vuln", methods=["POST"])
def dump_vuln():
    data = request.json or {}
    search = data.get("search", "")

    rows = vulnerable_dump(search)

    result = [
        {"username": r[0], "password": r[1], "role": r[2]}
        for r in rows
    ]

    return jsonify({
        "status": "OK",
        "rows": result,
        "count": len(result)
    })

if __name__ == "__main__":
    app.run(debug=True)
