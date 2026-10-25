from flask import Flask, request, jsonify
import sqlite3

app = Flask(__name__)


def get_db_connection():
    conn = sqlite3.connect("app.db")
    conn.row_factory = sqlite3.Row
    return conn


@app.route("/login", methods=["POST"])
def login():
    username = request.form.get("username", "")
    password = request.form.get("password", "")

    conn = get_db_connection()

    # Build the query by concatenating user input directly into the SQL string.
    query = "SELECT * FROM users WHERE username = '" + username + "' AND password = '" + password + "'"

    # Execute it as-is.
    result = conn.execute(query).fetchone()
    conn.close()

    if result is None:
        return jsonify({"error": "Invalid username or password"}), 401

    return jsonify({"message": "Login successful", "user": result["username"]}), 200


if __name__ == "__main__":
    app.run(debug=True)
