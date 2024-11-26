import sqlite3
from bcrypt import hashpw, gensalt, checkpw
from auth.db import create_database

# Registrar usuario
def register_user(username, password, role):
    """Registra un nuevo usuario con contraseña cifrada."""
    create_database()  # Asegurarse de que la base de datos exista
    conn = sqlite3.connect('system.db')
    cursor = conn.cursor()
    hashed_password = hashpw(password.encode(), gensalt())
    try:
        cursor.execute('INSERT INTO users (username, password, role) VALUES (?, ?, ?)', 
                       (username, hashed_password, role))
        conn.commit()
        print(f"Usuario '{username}' registrado con éxito.")
    except sqlite3.IntegrityError:
        print(f"Error: El usuario '{username}' ya existe.")
    finally:
        conn.close()

# Validar login
def login_user(username, password):
    """Valida el login del usuario."""
    conn = sqlite3.connect('system.db')
    cursor = conn.cursor()
    cursor.execute('SELECT password, role FROM users WHERE username = ?', (username,))
    result = cursor.fetchone()
    conn.close()
    if result:
        hashed_password, role = result
        if checkpw(password.encode(), hashed_password):
            print(f"Bienvenido, {username}.")
            return role
        else:
            print("Error: Contraseña incorrecta.")
    else:
        print("Error: Usuario no encontrado.")
    return None
