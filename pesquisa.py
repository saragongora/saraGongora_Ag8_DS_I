print("PESQUISA DE SATISFAÇÃO - TUDOWEB")

excelente = 0
ruim = 0

for i in range(1, 51):
    print(f"\nEntrevistado {i}")

    nome = input("Digite o nome: ")
    idade = int(input("Digite a idade: "))

    print("\n1 - EXCELENTE")
    print("2 - BOM")
    print("3 - RUIM")

    opiniao = int(input("Digite sua opção: "))

    if opiniao == 1:
        excelente += 1
    elif opiniao == 3:
        ruim += 1

print(f"\nEXCELENTE: {excelente}")
print(f"RUIM: {ruim}")