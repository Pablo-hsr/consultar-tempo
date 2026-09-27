import requests


def buscar_previsao(latitude, longitude):
    url_clima = "https://api.open-meteo.com/v1/forecast"

    parametros_clima = {
        "latitude": latitude,
        "longitude": longitude,
        "daily": (
            "weather_code,"
            "temperature_2m_max,"
            "temperature_2m_min,"
            "precipitation_probability_max,"
            "precipitation_sum"
        ),
        "forecast_days": 2,
        "timezone": "auto"
    }

    response_clima = requests.get(
            url_clima,
            params=parametros_clima,
            timeout=10
        )

    response_clima.raise_for_status()
    return response_clima.json()

def descrever_clima(codigo):
    descricoes = {
        0: "Céu limpo",
        1: "Predominantemente limpo",
        2: "Parcialmente nublado",
        3: "Nublado",
        45: "Neblina",
        48: "Neblina com geada",
        51: "Garoa fraca",
        53: "Garoa moderada",
        55: "Garoa forte",
        61: "Chuva fraca",
        63: "Chuva moderada",
        65: "Chuva forte",
        80: "Pancadas de chuva fracas",
        81: "Pancadas de chuva moderadas",
        82: "Pancadas de chuva fortes",
        95: "Tempestade"
    }

    return descricoes.get(codigo, "Condição desconhecida")