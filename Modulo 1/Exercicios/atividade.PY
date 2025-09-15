num = int(input("Digite o número que deseja ver a tabuada: "))
i = int(input("Digite qual número a tabuada deve começar: "))
fim = int(input("Digite até qual número a tabuada deve ir: " ))

while i <= fim:
    print(f"{i} x {num} = {i * num}")
    i += 1