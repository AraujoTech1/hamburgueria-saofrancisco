from produtos import hamburgueres, milkshakes, refrigerantes, agua

def mostrar_cardapio():
    print("\n🍽️ BEM-VINDO AO AUTOATENDIMENTO DA HAMBURGUERIA SÃO FRANCISCO!\n")

    print("🍔 HAMBÚRGUERES")
    for item in hamburgueres:
        print(f"{item['id']}. {item['sabor']} - R$ {item['preco']:.2f}")

    print("\n🥤 MILKSHAKES")
    for item in milkshakes:
        print(f"{item['id'] + 5}. {item['sabor']} - R$ {item['preco']:.2f}")

    print("\n🧃 REFRIGERANTES")
    for item in refrigerantes:
        print(f"{item['id'] + 7}. {item['sabor']} - R$ {item['preco']:.2f}")

    print("\n💧 ÁGUA")
    for item in agua:
        print(f"{item['id'] + 10}. {item['sabor']} - R$ {item['preco']:.2f}")

def calcular_pedido(itens_escolhidos):
    return sum(item['preco'] for item in itens_escolhidos)

# Execução principal
mostrar_cardapio()
opcoes = input("\nDigite os números dos itens que deseja (separados por vírgula): ")

ids_escolhidos = [int(i.strip()) for i in opcoes.split(",") if i.strip().isdigit()]
itens_escolhidos = []

# Mapeando os IDs corretamente
for id_ in ids_escolhidos:
    if 1 <= id_ <= 5:
        itens_escolhidos.append(hamburgueres[id_-1])
    elif 6 <= id_ <= 7:
        itens_escolhidos.append(milkshakes[id_-6])
    elif 8 <= id_ <= 10:
        itens_escolhidos.append(refrigerantes[id_-8])
    elif 11 == id_:
        itens_escolhidos.append(agua[0])

print("\n🧾 RESUMO DO PEDIDO")
for item in itens_escolhidos:
    print(f"- {item['sabor']} - R$ {item['preco']:.2f}")

total = calcular_pedido(itens_escolhidos)
print(f"\n💰 TOTAL: R$ {total:.2f}")
print("🔔 Seu pedido foi realizado com sucesso! Retire no balcão! 😋")
