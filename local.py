import requests

def buscar_local(nome_cidade):
    url_local = "https://geocoding-api.open-meteo.com/v1/search"

    parametros_local = {
            "name": nome_cidade,
            "count": 1,
            "language": "pt",
            "format": "json"
        }

    response = requests.get(
    url_local,
    params=parametros_local,
    timeout=10
    )
    response.raise_for_status()

    dados = response.jason()

    if "results" not in dados:
        return None

    return dados["results"][0]