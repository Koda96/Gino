import sqlite3


def create_economic_table():
    """Crea la tabla para indicadores económicos si no existe."""
    conn = sqlite3.connect('system.db')
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS economic_indicators (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            user TEXT NOT NULL,
            indicator TEXT NOT NULL,
            date TEXT NOT NULL,
            value REAL NOT NULL,
            source TEXT NOT NULL,
            timestamp DATETIME DEFAULT CURRENT_TIMESTAMP
        )
    ''')
    conn.commit()
    conn.close()

def save_indicator_data(user, indicator, date, value, source):
    """Guarda los datos de un indicador económico en la base de datos."""
    conn = sqlite3.connect('system.db')
    cursor = conn.cursor()
    try:
        print(f"Insertando datos: User={user}, Indicator={indicator}, Date={date}, Value={value}, Source={source}")
        cursor.execute('''
            INSERT INTO economic_indicators (user, indicator, date, value, source)
            VALUES (?, ?, ?, ?, ?)
        ''', (user, indicator, date, value, source))
        conn.commit()
        print(f"Datos del indicador '{indicator}' guardados correctamente.")
    except sqlite3.Error as e:
        print(f"Error al guardar los datos: {e}")
    finally:
        conn.close()