def calcular_total(itens):
    total = 0
    for item in itens:
        total += item["preco"] * item["quantidade"]
    return total


def aplicar_regras_pagamento(total, forma_pagamento):
    forma_pagamento = forma_pagamento.lower()

    desconto = 0
    pode_parcelar = False

    if forma_pagamento in ["pix", "debito", "dinheiro"] and total > 100:
        desconto = total * 0.03
    elif forma_pagamento == "credito" and total > 100:
        pode_parcelar = True

    return desconto, total - desconto, pode_parcelar


def sistema_caixa():
    itens = []

    print("=== SISTEMA DE CAIXA ===")

    while True:
        nome = input("Nome do produto (ou 'fim' para encerrar): ")

        if nome.lower() == "fim":
            break

        preco = float(input("Preço do produto: "))
        quantidade = int(input("Quantidade: "))

        itens.append({
            "nome": nome,
            "preco": preco,
            "quantidade": quantidade
        })

    if not itens:
        print("Nenhum produto informado.")
        return

    forma_pagamento = input("Forma de pagamento (pix, debito, dinheiro, credito): ")

    total = calcular_total(itens)
    desconto, valor_final, pode_parcelar = aplicar_regras_pagamento(total, forma_pagamento)

    print("\n=== CUPOM FISCAL ===")
    for item in itens:
        total_item = item["preco"] * item["quantidade"]
        print(f"{item['nome']} | {item['quantidade']} x {item['preco']} = {total_item}")

    print("-------------------")
    print(f"Total: R$ {total:.2f}")
    print(f"Desconto: R$ {desconto:.2f}")
    print(f"Valor final: R$ {valor_final:.2f}")
    print(f"Pagamento: {forma_pagamento}")
    print(f"Parcelamento: {'Sim' if pode_parcelar else 'Não'}")


# EXECUÇÃO
sistema_caixa()
