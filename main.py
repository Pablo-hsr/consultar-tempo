from banco import criar_tabela, salvar_cidade, listar_cidades, remover_cidade
from local import buscar_local 
from clima import buscar_previsao, descrever_clima

def mostrar_previsao(cidade):
    dados = buscar_previsao(
        cidade[2],
        cidade[3]
    )
    diario = dados["daily"]
    print(f"\n--- {cidade[1]} ---")

    for i in range(2):
        if i == 0:
            periodo = "Hoje"
        else:
            periodo = "Amanhã"

        data = diario["time"][i]
        minima = diario["temperature_2m_min"][i]
        maxima = diario["temperature_2m_max"][i]
        chuva = diario["precipitation_probability_max"][i]
        codigo = diario["weather_code"][i]

        print(f"\n{periodo} - {data}")
        print(f"Condição: {descrever_clima(codigo)}")
        print(f"Mínima: {minima} °C")
        print(f"Máxima: {maxima} °C")
        print(f"Chance de chuva: {chuva}%")

def main():
    criar_tabela()

    while True:
        print("\n--- MENU ---")
        print("1 - Salvar cidade favorita")
        print("2 - Listar cidades favoritas")
        print("3 - Ver previsão")
        print("4 - Remover cidade dos favoritos")
        print("0 - Sair")

        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            nome = input("Digite a cidade: ")

            local = buscar_local(nome)

            if local is None:
                print("Cidade não encontrada.")
                continue
            salvar_cidade(
                local["name"],
                local["latitude"],
                local["longitude"],
                local.get("country")
            )

            print(f"{local['name']} foi salva.")

        elif opcao == "2":
            cidades = listar_cidades()

            if not cidades:
                print("Nenhuma cidade salva.")
                continue

            for cidade in cidades:
                print(f"{cidade[0]} - {cidade[1]}, {cidade[4]}")

        elif opcao == "3":
            cidades = listar_cidades()

            if not cidades:
                print("Nenhuma cidade salva.")
                continue

            for cidade in cidades:
                print(f"{cidade[0]} - {cidade[1]}")

            try:
                id_escolhido = int(input("Digite o ID da cidade: "))
            except ValueError:
                print("Digite um número.")
                continue

            cidade_escolhida = None

            for cidade in cidades:
                if cidade[0] == id_escolhido:
                    cidade_escolhida = cidade
                    break

            if cidade_escolhida is None:
                print("Cidade não encontrada.")
            else:
                mostrar_previsao(cidade_escolhida)

        elif opcao == "4":
            remover_cidade()

        elif opcao == "0":
            print("Programa encerrado.")
            break

        else:
            print("Opção inválida.")

if __name__ == "__main__":
    main()