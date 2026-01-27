def calcular_total(itens):
    total = 0

    for item in itens:
        total_item = item["preco"] * item["quantidade"]
        total += total_item

    return total


def aplicar_regras_pagamento(total, forma_pagamento):
    forma_pagamento = forma_pagamento.lower()

    desconto = 0
    pode_parcelar = False

    if forma_pagamento in ["pix", "debito", "dinheiro"] and total > 100:
        desconto = total * 0.03

    elif forma_pagamento == "credito" and total > 100:
        pode_parcelar = True

    valor_final = total - desconto

    return desconto, valor_final, pode_parcelar


def gerar_cupom(itens, forma_pagamento):
    if not itens:
        print("Carrinho vazio.")
        return

    total = calcular_total(itens)
    desconto, valor_final, pode_parcelar = aplicar_regras_pagamento(total, forma_pagamento)

    print("\n=== CUPOM FISCAL ===")
    for item in itens:
        total_item = item["preco"] * item["quantidade"]
        print(f"{item['nome']} | {item['quantidade']} x {item['preco']} = {total_item}")

    print("-------------------")
    print(f"Total: R$ {total}")
    print(f"Desconto: R$ {desconto}")
    print(f"Valor final: R$ {valor_final}")
    print(f"Pagamento: {forma_pagamento}")
    print(f"Parcelamento: {'Sim' if pode_parcelar else 'Não'}")


# SIMULAÇÃO
itens = [
    {"nome": "Cimento", "preco": 40, "quantidade": 2},
    {"nome": "Luva", "preco": 10, "quantidade": 3}
]

forma_pagamento = "pix"
gerar_cupom(itens, forma_pagamento)




