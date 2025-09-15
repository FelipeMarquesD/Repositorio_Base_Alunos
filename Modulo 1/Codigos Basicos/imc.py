try:
    nome = input("Digite o nome do paciente: ")
    P = float(input("Digite o peso de uma pessoa em Kg: "))
    A = float(input("Digite a altura de uma pessoa: "))

    imc = P/(A*A)

    if imc < 18.5:
        print("Abaixo do peso")
    elif imc < 24.9:
        print("Peso normal")
    elif imc < 29.9:
        print("Sobrepeso")
    elif imc < 34.9:
        print("Obesidade Grau I")
    elif imc < 39.9:
        print("Obesidade Grau II")
    else: 
        print("Obesidade Grau III")

    print(f"O Imc do paciente {nome} é : {imc}")
except:
    print("Valor incorreto, digite o que pede")