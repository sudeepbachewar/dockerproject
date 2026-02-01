from flask import Flask, render_template, request, redirect, url_for
import sqlite3
import os

app = Flask(__name__)
DATABASE = "contact.db"


# ---------- Database helper ----------
def get_db_connection():
    conn = sqlite3.connect(DATABASE)
    conn.row_factory = sqlite3.Row
    return conn


# ---------- Create table ----------
def init_db():
    if not os.path.exists(DATABASE):
        conn = get_db_connection()
        conn.execute("""
            CREATE TABLE contacts (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL,
                email TEXT NOT NULL,
                message TEXT NOT NULL
            )
        """)
        conn.commit()
        conn.close()


# ---------- Routes ----------
@app.route("/home")
def home():
    return render_template("home.html")


@app.route("/about")
def about():
    return render_template("about.html")


@app.route("/contact", methods=["GET", "POST"])
def contact():
    if request.method == "POST":
        name = request.form["name"]
        email = request.form["email"]
        message = request.form["message"]

        conn = get_db_connection()
        conn.execute(
            "INSERT INTO contacts (name, email, message) VALUES (?, ?, ?)",
            (name, email, message)
        )
        conn.commit()
        conn.close()

        return redirect(url_for("contact"))

    return render_template("contact.html")

@app.route("/messages")
def messages():
    conn = get_db_connection()
    contacts = conn.execute("SELECT * FROM contacts ORDER BY id DESC").fetchall()
    conn.close()
    return render_template("messages.html", contacts=contacts)


# ---------- Run app ----------
if __name__ == "__main__":
    init_db()
    app.run(debug=True, host="0.0.0.0", port=5000)
