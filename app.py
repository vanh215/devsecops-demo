import os
import sqlite3

# LỖI BẢO MẬT 1: Hardcode Secret Key (Gitleaks sẽ tóm cái này)
SECRET_API_KEY = "AKIAIOSFODNN7EXAMPLE"

def get_user(username):
    conn = sqlite3.connect('database.db')
    cursor = conn.cursor()
    # LỖI BẢO MẬT 2: SQL Injection (CodeQL sẽ tóm cái này)
    query = f"SELECT * FROM users WHERE username = '{username}'"
    cursor.execute(query)
    return cursor.fetchall()

if __name__ == "__main__":
    print(f"Hệ thống khởi động với Key: {SECRET_API_KEY}")
    get_user("admin")