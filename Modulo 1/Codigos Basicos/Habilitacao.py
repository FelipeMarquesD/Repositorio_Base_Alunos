nome = input("Digite seu nome: ")
idade = int(input("Digite sua idade: "))
possui_carteira = input("Possui carteira de motorista? \n (1-Sim / 2-Não)")

if idade >= 18:
    if possui_carteira == "1":
        print("Pode dirigir 🏎️🏎️🏎️ MARCHA!!!")
    else:
        print("Não pode dirigir !PAIZAO! 🚳🚳🚳")
else:
    print("Menor de idade 🔞🔞🔞")