from flask import Flask, render_template, request, redirect, url_for
import sqlite3
from datetime import datetime

app = Flask(__name__)

# Função para conectar ao banco de dados
def get_db_connection():
    conn = sqlite3.connect("tasks.db")
    conn.row_factory = sqlite3.Row
    return conn

# Função para inicializar o banco de dados
def init_db():
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS tasks (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            title TEXT NOT NULL,
            description TEXT,
            created_at TEXT NOT NULL,
            status TEXT DEFAULT 'Pendente'
        )
    """)
    conn.commit()
    conn.close()

# Rota principal para listar tarefas
@app.route("/")
def index():
    conn = get_db_connection()
    query = "SELECT * FROM tasks"
    search = request.args.get("search")
    if search:
        query += f" WHERE title LIKE '%{search}%' OR description LIKE '%{search}%'"
    tasks = conn.execute(query).fetchall()
    conn.close()
    return render_template("index.html", tasks=tasks)

# Rota para adicionar uma nova tarefa
@app.route("/add", methods=["POST"])
def add_task():
    title = request.form["title"]
    description = request.form["description"]
    created_at = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    conn = get_db_connection()
    conn.execute("INSERT INTO tasks (title, description, created_at) VALUES (?, ?, ?)", (title, description, created_at))
    conn.commit()
    conn.close()
    return redirect(url_for("index"))

# Rota para atualizar o status de uma tarefa
@app.route("/update/<int:task_id>", methods=["POST"])
def update_task(task_id):
    status = request.form["status"]
    conn = get_db_connection()
    conn.execute("UPDATE tasks SET status = ? WHERE id = ?", (status, task_id))
    conn.commit()
    conn.close()
    return redirect(url_for("index"))

# Rota para excluir uma tarefa
@app.route("/delete/<int:task_id>")
def delete_task(task_id):
    conn = get_db_connection()
    conn.execute("DELETE FROM tasks WHERE id = ?", (task_id,))
    conn.commit()
    conn.close()
    return redirect(url_for("index"))

if __name__ == "__main__":
    init_db()  # Inicializa o banco de dados ao iniciar o servidor
    app.run(debug=True, port=8080)
