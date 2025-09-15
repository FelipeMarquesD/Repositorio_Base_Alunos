import time

print("---------------------------------")
print("******🚚 MERCADO LIVRE 🚚 ******")
print("---------------------------------")

usuario = input ("Digite o nome de usuário: ")
senha = input("Digite a senha: ")

print("Carregando ...........")
time.sleep(3)


if usuario == "ADM" and senha == "1234":
    print("Login bem -sucedido!")
    print("---------------------------------")
    print(f"Bem vindo aomercado livre")
    print("---------------------------------")
else:
    print("Usuário ou senha incorretos. ❌❌❌")