import requests

# Função que faz a conversão de qualquer moeda para BRL
def converter_para_brl(valor, moeda):
    API_KEY = '5263d525cfb6ba6b8909ab78'
    url = f"https://v6.exchangerate-api.com/v6/{API_KEY}/latest/{moeda}"

    try:
        # Definindo um timeout de 10 segundos para evitar espera indefinida
        response = requests.get(url, timeout=10)
        response.raise_for_status()  # Lança uma exceção se a resposta não for 200 OK
        
        # Verifica se a API retornou os dados esperados
        dados = response.json()
        if 'conversion_rates' not in dados or 'BRL' not in dados['conversion_rates']:
            raise ValueError("Dados inesperados da API.")
        
        # Calcula o valor convertido
        taxa_para_brl = dados['conversion_rates']['BRL']
        valor_brl = valor * taxa_para_brl
        return valor_brl

    except requests.exceptions.RequestException as e:
        print(f"Erro de conexão: {e}")
    except ValueError as e:
        print(f"Erro ao processar dados: {e}")
    except Exception as e:
        print(f"Ocorreu um erro inesperado: {e}")
    
    return None

# Função que exibe um menu para o usuário selecionar a moeda
def selecionar_moeda():
    print("Escolha uma moeda para converter para BRL:")
    print("1. Dólar americano (USD)")
    print("2. Euro (EUR)")
    print("3. Iene (JPY)")
    print("4. Libra Esterlina (GBP)")
    print("5. Franco Suíço (CHF)")
    print("6. Dólar Canadense (CAD)")
    print("7. Dólar Australiano (AUD)")
    print("8. Rand (ZAR)")
    print("9. Yuan (CNY)")
    print("10. Peso Argentino (ARS)")
    
    opcoes_moedas = {
        "1": "USD",
        "2": "EUR",
        "3": "JPY",
        "4": "GBP",
        "5": "CHF",
        "6": "CAD",
        "7": "AUD",
        "8": "ZAR",
        "9": "CNY",
        "10": "ARS"
    }

    while True:
        escolha = input("Digite o número da moeda: ").strip()
        if escolha in opcoes_moedas:
            return opcoes_moedas[escolha]
        else:
            print("Opção inválida. Tente novamente.")

# Função que valida a entrada do valor
def obter_valor():
    while True:
        try:
            valor = float(input("Digite o valor que deseja converter: ").strip())
            if valor <= 0:
                raise ValueError("O valor deve ser maior que zero.")
            return valor
        except ValueError as e:
            print(f"Entrada inválida: {e}. Por favor, tente novamente.")

# Função principal
def main():
    valor = obter_valor()
    moeda_escolhida = selecionar_moeda()

    valor_brl = converter_para_brl(valor, moeda_escolhida)
    if valor_brl is not None:
        print(f"O valor de {valor} {moeda_escolhida} é equivalente a {valor_brl:.2f} BRL.")
    else:
        print("Não foi possível realizar a conversão.")

if __name__ == "__main__":
    main()
