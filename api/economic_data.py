import requests

BASE_URL = "https://api.example.com/economic"  # Cambiar por la API real

def get_economic_indicator(indicator, date):
    """
    Devuelve datos simulados si no hay una API real disponible.
    """
    simulated_data = {
        "dollar": {"2024-11-01": 850.75},
        "euro": {"2024-11-01": 900.25}
    }
    try:
        value = simulated_data[indicator][date]
        return {"indicator": indicator, "date": date, "value": value}
    except KeyError:
        print(f"Datos simulados no disponibles para {indicator} en {date}.")
        return None

def get_economic_indicator2(indicator, date):
    """
    Consulta el valor de un indicador económico para una fecha específica.
    :param indicator: Indicador económico (e.g., "dollar", "euro").
    :param date: Fecha en formato YYYY-MM-DD.
    :return: Diccionario con los datos del indicador o None si falla.
    """
    try:
        response = requests.get(f"{BASE_URL}/{indicator}/{date}")
        response.raise_for_status()  # Lanza excepción si hay error HTTP
        data = response.json()
        return {
            "indicator": indicator,
            "date": date,
            "value": data["value"]
        }
    except requests.exceptions.RequestException as e:
        print(f"Error al consultar el indicador: {e}")
        return None
