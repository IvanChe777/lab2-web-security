
from flask import Flask, request, render_template
import sqlite3
import os

from database import init_db, DB_NAME

app = Flask(__name__)

# True - уязвимый режим
# False - безопасный режим
VULNERABLE = os.getenv("VULNERABLE", "False").lower() == "true"
print("Текущий режим: ", VULNERABLE)

def get_db():
    return sqlite3.connect(DB_NAME)


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/search")
def search():
    query = request.args.get("q", "")

    conn = get_db()
    cursor = conn.cursor()

    cursor.execute(
        "SELECT * FROM products WHERE name LIKE ?",
        (f"%{query}%",)
    )

    products = cursor.fetchall()
    conn.close()

    return render_template(
        "search.html",
        products=products,
        query=query
    )


@app.route("/hello")
def hello():
    name = request.args.get("name", "Гость")

    return render_template(
        "hello.html",
        name=name,
        vulnerable=VULNERABLE
    )


if __name__ == "__main__":
    init_db()

    print("Режим уязвимостей:", VULNERABLE)

    app.run(
        host="127.0.0.1",
        port=5000,
        debug=False
    )
