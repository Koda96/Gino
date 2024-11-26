import requests
from auth.db import create_database
from database.economic_db import create_economic_table

def check_api_connection():
    """Simula la conexión con una API externa para datos económicos."""
    print("Usando datos simulados para indicadores económicos.")
    # Aquí podrías añadir lógica para validar un archivo o un sistema de datos locales si es necesario.
    return True

def check_api_connection2(): #cambiar
    """Verifica la conexión con la API externa."""
    try:
        response = requests.get("https://api.example.com/ping")  # Cambiar URL por una válida
        if response.status_code == 200:
            print("Conexión con la API externa exitosa.")
        else:
            print("Advertencia: Problema al conectar con la API.")
    except requests.exceptions.RequestException as e:
        print(f"Error al conectar con la API: {e}")

def initialize_system():
    """Inicializa el sistema asegurándose de que todo esté listo."""
    print("Inicializando sistema...")
    create_database()
    check_api_connection()
    create_economic_table()
    print("Sistema inicializado correctamente.")
