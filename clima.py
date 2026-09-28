import requests


def buscar_previsao(latitude, longitude):
    url_clima = "https://api.open-meteo.com/v1/forecast"

    parametros_clima = {
        "latitude": latitude,
        "longitude": longitude,
        "current": (
            "temperature_2m,"
            "relative_humidity_2m,"
            "wind_speed_10m,"
            "weather_code"
        ),
        "daily": (
            "temperature_2m_max,"
            "temperature_2m_min,"
            "precipitation_probability_max,"
            "precipitation_sum,"
            "uv_index_max,"
            "wind_speed_10m_max,"
            "weather_code"
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

def gerar_recomendacao(dados):
    diario = dados["daily"]

    temperatura_maxima = diario["temperature_2m_max"][0]
    temperatura_minima = diario["temperature_2m_min"][0]
    chance_chuva = diario["precipitation_probability_max"][0]
    uv = diario["uv_index_max"][0]
    vento = diario["wind_speed_10m_max"][0]
    codigo_clima = diario["weather_code"][0]

    recomendacao = []

    if chance_chuva >= 60:
        recomendacao.append(
            "Leve um guarda-chuva, pois há grande chance de chuva."
        )
    elif chance_chuva >= 30:
        recomendacao.append(
            "Existe alguma chance de chuva. Talvez seja interessante levar um guarda-chuva."
        )
    if temperatura_maxima >= 32:
        recomendacao.append(
            "Está muito quente. Leve água e evite ficar muito tempo no sol."
        )
    elif temperatura_maxima >= 28:
        recomendacao.append(
            "Está quente. Leve água se for ficar muito tempo fora."
        )

    if temperatura_minima <= 15:
        recomendacao.append(
            "A manhã ou a noite pode estar fria. Considere levar um casaco."
        )

    
    if uv >= 8:
        recomendacao.append(
            "O índice UV está alto. Use protetor solar."
        )
    elif uv >= 6:
        recomendacao.append(
            "O índice UV está moderado/alto. Considere usar protetor solar."
        )

    if vento >= 40:
        recomendacao.append(
            "O vento está forte. Tenha cuidado em áreas abertas."
        )

    if codigo_clima in [95, 96, 99]:
        recomendacao.append(
            "Há previsão de tempestade. Talvez seja melhor evitar sair."
        )

    if not recomendacao:
        recomendacao.append(
            "O clima parece tranquilo para sair."
        )

    return recomendacao

def recomendacao_de_sair(dados, nome_cidade):
    diario = dados["daily"]

    temperatura_minima = diario["temperature_2m_min"][0]
    temperatura_maxima = diario["temperature_2m_max"][0]
    chance_chuva = diario["precipitation_probability_max"][0]
    uv = diario["uv_index_max"][0]
    vento = diario["wind_speed_10m_max"][0]

    print(f"\n--- RECOMENDACOES AO SAIR — {nome_cidade} ---")
    print(f"Mínima: {temperatura_minima} °C")
    print(f"Máxima: {temperatura_maxima} °C")
    print(f"Chance de chuva: {chance_chuva}%")
    print(f"Índice UV: {uv}")
    print(f"Vento máximo: {vento} km/h")

    print("\nRecomendações:")

    recomendacoes = gerar_recomendacao(dados)

    for recomendacao in recomendacoes:
        print(f"- {recomendacao}")