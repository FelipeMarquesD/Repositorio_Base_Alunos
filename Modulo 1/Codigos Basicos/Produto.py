nome_produto = input("Digite o nome do produto: ")
preco = float(input("Digite o preço do produto: R$"))
desconto = float(input("Digite o percentual de desconto %: "))

valor_desconto = preco * desconto / 100

preco_final = preco - valor_desconto
print("-----------------")
print(f"Produto: {nome_produto}\n Preço final: {preco_final}")
print("-----------------")