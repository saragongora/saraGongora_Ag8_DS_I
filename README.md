# saraGongora_Ag8_DS_I

# Pesquisa de Satisfação - TudoWeb

## Sobre o projeto
Este projeto foi desenvolvido em Python para realizar uma pesquisa de satisfação com clientes da empresa TudoWeb.

O programa utiliza:
- Estrutura de repetição `for`
- Estruturas de decisão `if` e `elif`
- Entrada de dados com `input()`

## Objetivo
Coletar:
- Nome do entrevistado
- Idade
- Opinião sobre o atendimento

As opções de opinião são:
- 1 = EXCELENTE
- 2 = BOM
- 3 = RUIM

Ao final, o sistema informa:
- Quantidade de respostas EXCELENTE
- Quantidade de respostas RUIM

## Código

```python
print("PESQUISA DE SATISFAÇÃO - TUDOWEB")

excelente = 0
ruim = 0

for i in range(1, 11):
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