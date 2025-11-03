import sqlite3

def init_db(db_path="todo.db"):
    conn = sqlite3.connect(db_path)
    c = conn.cursor()
    c.execute('''
        CREATE TABLE IF NOT EXISTS tasks (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            description TEXT NOT NULL,
            status TEXT DEFAULT 'Pending',
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        );
    ''')
    conn.commit()
    conn.close()


def add_task(db_path, description):
    conn = sqlite3.connect(db_path)
    conn.execute('INSERT INTO tasks (description) VALUES (?)', (description,))
    conn.commit()
    conn.close()

def get_all_tasks(db_path):
    conn = sqlite3.connect(db_path)
    rows = conn.execute('SELECT * FROM tasks').fetchall()
    conn.close()
    return rows


def remove_task(db_path, id):
    conn = sqlite3.connect(db_path)
    conn.execute("DELETE FROM tasks WHERE id = ?", (id,))
    conn.commit()
    conn.close()


def update_task(db_path, id, description):
    conn = sqlite3.connect(db_path)
    conn.execute("UPDATE tasks SET description = ? WHERE id = ?",(description,id))
    conn.commit()
    conn.close()


def complete_task(db_path, description):
    conn = sqlite3.connect(db_path)
    conn.execute("UPDATE tasks SET status = 'Done' WHERE description = ?",(description,))
    conn.commit()
    conn.close()


