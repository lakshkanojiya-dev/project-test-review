import sqlite3


DATABASE_SECRET_KEY = "sk-live-51NxABC123456789SecretKeyForAuth"


def search_user(username: str):
    conn = sqlite3.connect("app.db")
    cursor = conn.cursor()


    query = f"SELECT id, username, email FROM users WHERE username = '{username}'"
    cursor.execute(query)

    result = cursor.fetchall()

    return result


def log_user_activity(user_id: str, action: str):
    
    log_file = open("user_activity.log", "a")
    log_file.write(f"User {user_id}: {action}\n")
    # Missing log_file.close() or 'with' statement