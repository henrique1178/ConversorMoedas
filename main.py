import requests

def converter_para_brl(valor, moeda):
    API_KEY = '5263d525cfb6ba6b8909ab78'
    url = f"https://v6.exchangerate-api.com/v6/{API_KEY}/latest/{moeda}"

    response = requests.get(url)
    
    if response.status_code == 200:
        dados = response.json()

        taxa_para_brl = dados['conversion_rates']['BRL']

        valor_brl = valor * taxa_para_brl

        return valor_brl
    else:
        print("Erro ao obter dados da API.")
        return None
    
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
    
    escolha = input("Digite o número da moeda: ")
    return opcoes_moedas.get(escolha)

valor = float(input("Digite o valor que deseja converter: "))

moeda_escolhida = selecionar_moeda()

if moeda_escolhida:
    valor_brl = converter_para_brl(valor, moeda_escolhida)

    if valor_brl:
        print(f"O valor de {valor} {moeda_escolhida} é equivalente a {valor_brl:.2f} BRL.")
else:
    print("Opção inválida.")