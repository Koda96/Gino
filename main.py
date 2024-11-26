from auth.user import register_user, login_user
from config.settings import initialize_system
from api.economic_data import get_economic_indicator
from database.economic_db import save_indicator_data

# Inicializar sistema
initialize_system()

if __name__ == "__main__":
    # Registro de usuario
    register_user("admin", "securepassword123", "admin")
    # Intentar login
    role = login_user("admin", "securepassword123")
    if role:
        print(f"Usuario autenticado con rol: {role}")
        # Consulta de indicadores económicos
        indicator = "dollar"
        date = "2024-11-01"
        result = get_economic_indicator(indicator, date)
        if result:
            print(f"Indicador consultado: {result}")
            # Guardar en la base de datos
            save_indicator_data(
                user="admin",
                indicator=result["indicator"],
                date=result["date"],
                value=result["value"],
                source="Simulated Data"
            )
